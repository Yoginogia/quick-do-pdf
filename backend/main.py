from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pdf2docx import Converter
import pdfplumber
import pandas as pd
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
        
        all_tables = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    # Filter out None values that pdfplumber sometimes inserts for empty cells
                    cleaned_table = [
                        ['' if cell is None else str(cell) for cell in row]
                        for row in table
                    ]
                    if len(cleaned_table) > 1:
                        df = pd.DataFrame(cleaned_table[1:], columns=cleaned_table[0])
                    else:
                        df = pd.DataFrame(cleaned_table)
                    all_tables.append(df)
                    
        if not all_tables:
            df = pd.DataFrame([["No structured tables could be detected in this PDF."]])
            all_tables.append(df)
            
        with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
            for i, df in enumerate(all_tables):
                sheet_name = f"Table_{i+1}"
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
