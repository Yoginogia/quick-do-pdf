param(
    [string]$File,
    [string]$Title,
    [string]$Desc,
    [string]$H1,
    [string]$Subtitle
)

$content = Get-Content -Raw -Path $File

# Replace Title
$content = $content -replace '<title>.*?</title>', "<title>$Title</title>"

# Replace Meta Description
$content = $content -replace '<meta name="description"[\s\S]*?>', "<meta name=`"description`"`n    content=`"$Desc`">"

# Replace H1
$content = $content -replace '<h1>(.*?)</h1>', "<h1>$H1</h1>"

# Replace Subtitle (assuming it's <p class="page-subtitle">...</p>)
$content = $content -replace '<p class="page-subtitle">[\s\S]*?</p>', "<p class=`"page-subtitle`">$Subtitle</p>"

Set-Content -Path $File -Value $content -NoNewline
Write-Host "Updated $File"
