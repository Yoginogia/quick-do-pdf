param (
    [string]$SourceFile = 'compress.html',
    [string]$TargetFiles = 'compress-pdf-100kb.html,compress-pdf-200kb.html,compress-pdf-under-1mb.html,compress-pdf-for-email.html,compress-pdf-without-losing-quality.html'
)

$targetArray = $TargetFiles -split ','

# Read the content of the source file
$sourceContent = Get-Content -Path $SourceFile -Raw

# We need to extract the new <script> imports from the <head>, the new option-grid UI, and the new compressPDF() logic from compress.html.
# Because the scripts were all identical copies of compress.html previously, we can isolate the `<script>` imports natively.

$headPattern = '(?s)<title>.*?</title>\s*<!-- PDF.js.*?<link rel="stylesheet" href="tools\.css\?v=2">'
$uiPattern = '(?s)<h4>Compression Target</h4>.*?</div>\s*</div>'
$scriptPattern = '(?s)async function compressPDF\(\) \{.*?</script>'

# Extract from source
$headMatch = [regex]::Match($sourceContent, $headPattern)
$uiMatch = [regex]::Match($sourceContent, $uiPattern)
$scriptMatch = [regex]::Match($sourceContent, $scriptPattern)

if ($headMatch.Success -and $uiMatch.Success -and $scriptMatch.Success) {
    Write-Host "Successfully extracted new logic from compress.html"
    
    foreach ($file in $targetArray) {
        if (Test-Path $file) {
            $content = Get-Content $file -Raw
            
            # Replace old head imports
            $content = $content -replace '(?s)<title>.*?</title>\s*<script src="https://unpkg\.com/pdf-lib@.*?\.js"></script>\s*<link rel="stylesheet" href="tools\.css\?v=2">', $headMatch.Value
            
            # Replace old UI
            $content = $content -replace '(?s)<h4>Compression Level</h4>.*?</div>\s*</div>', $uiMatch.Value
            
            # Replace old script
            $content = $content -replace '(?s)async function compressPDF\(\) \{.*?</script>', $scriptMatch.Value
            
            Set-Content -Path $file -Value $content -Encoding UTF8
            Write-Host "Updated $($file)"
        }
        else {
            Write-Host "File not found: $($file)"
        }
    }
}
else {
    Write-Host "Failed to extract required sections from compress.html"
}
