from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pdf2docx import Converter
import pdfplumber
import pandas as pd
import pikepdf
import os
import uuid
import tempfile

app = FastAPI(title="Quick Do PDF Local API")

# Allow CORS for local frontend testing & Production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def cleanup_files(*file_paths):
    for path in file_paths:
        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"Cleaned up {path}")
        except Exception as e:
            print(f"Error cleaning up {path}: {e}")

@app.post("/api/convert/pdf-to-word")
async def convert_pdf_to_word(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
        
    session_id = str(uuid.uuid4())
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f"temp_{session_id}.pdf")
    docx_path = os.path.join(temp_dir, f"temp_{session_id}.docx")
    
    try:
        # Save uploaded PDF to disk
        contents = await file.read()
        with open(pdf_path, "wb") as f:
            f.write(contents)
            
        print(f"Started converting {file.filename} -> DOCX...")
        # Convert using pdf2docx
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        
        # Check if conversion succeeded
        if not os.path.exists(docx_path):
            raise Exception("Conversion failed to produce a DOCX file.")
            
        print(f"Conversion successful! Returning DOCX...")
            
        # Clean up both files after the response is sent back to the browser
        background_tasks.add_task(cleanup_files, pdf_path, docx_path)
        
        # Output filename
        final_filename = file.filename.rsplit('.', 1)[0] + ".docx"
        
        return FileResponse(
            path=docx_path, 
            filename=final_filename,
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        # If error occurs, cleanup immediately to avoid junk accumulation
        cleanup_files(pdf_path, docx_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/convert/pdf-to-excel")
async def convert_pdf_to_excel(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
        
    session_id = str(uuid.uuid4())
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f"temp_excel_{session_id}.pdf")
    xlsx_path = os.path.join(temp_dir, f"temp_excel_{session_id}.xlsx")
    
    try:
        contents = await file.read()
        with open(pdf_path, "wb") as f:
            f.write(contents)
            
        print(f"Started converting {file.filename} -> EXCEL...")
        
        all_rows = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                # Use text-based layout parsing to capture the entire document into a grid, not just bordered tables
                tables = page.extract_tables({
                    "vertical_strategy": "text",
                    "horizontal_strategy": "text",
                    "snap_tolerance": 3,
                    "join_tolerance": 3
                })
                
                # Fallback: if 'text' strategy fails to find any structured tables, we use a custom line-by-line extractor
                if not tables:
                    text_layout = page.extract_text(layout=True)
                    if text_layout:
                        import re
                        raw_rows = []
                        for line in text_layout.split('\n'):
                            if line.strip():
                                # Try to maintain some semblance of columns by splitting by 2+ spaces
                                cols = re.split(r'\s{2,}', line.strip())
                                raw_rows.append(cols)
                        if raw_rows:
                            tables = [raw_rows]

                for table in tables:
                    for row in table:
                        # Convert all cells to strings and handle None values
                        cleaned_row = ['' if cell is None else str(cell) for cell in row]
                        all_rows.append(cleaned_row)
                    # Add an empty row between separate tables or pages for readability
                    all_rows.append([])
                    
        if not all_rows:
            all_rows = [["No structured data could be detected in this PDF."]]
            
        # Create a single DataFrame without headers so columns aren't mismatched
        df = pd.DataFrame(all_rows)
        
        with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
            # Disable pandas index and header row, write everything to one continuous sheet
            df.to_excel(writer, sheet_name="Sheet1", index=False, header=False)
                
        if not os.path.exists(xlsx_path):
            raise Exception("Conversion failed to produce an XLSX file.")
            
        print("Excel extraction successful! Returning XLSX...")
            
        background_tasks.add_task(cleanup_files, pdf_path, xlsx_path)
        final_filename = file.filename.rsplit('.', 1)[0] + ".xlsx"
        
        return FileResponse(
            path=xlsx_path, 
            filename=final_filename,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
    except Exception as e:
        print(f"Error during Excel conversion: {e}")
        cleanup_files(pdf_path, xlsx_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/security/protect-pdf")
async def protect_pdf(background_tasks: BackgroundTasks, file: UploadFile = File(...), password: str = Form(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
        
    session_id = str(uuid.uuid4())
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f"temp_protect_{session_id}.pdf")
    out_path = os.path.join(temp_dir, f"protected_{session_id}.pdf")
    
    try:
        contents = await file.read()
        with open(pdf_path, "wb") as f:
            f.write(contents)
            
        print(f"Applying password to {file.filename}...")
        
        pdf = pikepdf.Pdf.open(pdf_path)
        # Apply 256-bit AES encryption
        pdf.save(out_path, encryption=pikepdf.Encryption(user=password, owner=password))
        pdf.close()
            
        background_tasks.add_task(cleanup_files, pdf_path, out_path)
        final_filename = "protected_" + file.filename
        
        return FileResponse(
            path=out_path, 
            filename=final_filename,
            media_type='application/pdf'
        )
    except Exception as e:
        print(f"Error during protection: {e}")
        cleanup_files(pdf_path, out_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/security/unlock-pdf")
async def unlock_pdf(background_tasks: BackgroundTasks, file: UploadFile = File(...), password: str = Form(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
        
    session_id = str(uuid.uuid4())
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f"temp_unlock_{session_id}.pdf")
    out_path = os.path.join(temp_dir, f"unlocked_{session_id}.pdf")
    
    try:
        contents = await file.read()
        with open(pdf_path, "wb") as f:
            f.write(contents)
            
        print(f"Removing password from {file.filename}...")
        
        # Open with the provided password
        try:
            pdf = pikepdf.Pdf.open(pdf_path, password=password)
        except pikepdf.PasswordError:
            raise HTTPException(status_code=401, detail="Incorrect Password")
            
        # Saving without encryption parameter removes the password
        pdf.save(out_path)
        pdf.close()
            
        background_tasks.add_task(cleanup_files, pdf_path, out_path)
        final_filename = "unlocked_" + file.filename
        
        return FileResponse(
            path=out_path, 
            filename=final_filename,
            media_type='application/pdf'
        )
    except HTTPException:
        cleanup_files(pdf_path, out_path)
        raise
    except Exception as e:
        print(f"Error during unlocking: {e}")
        cleanup_files(pdf_path, out_path)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
