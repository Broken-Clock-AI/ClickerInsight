param(
    [string]$Url,
    [string]$OutDir
)

# Create the output directory if it doesn't exist
if (-not (Test-Path -Path $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

# Download the main HTML file
$htmlFile = Join-Path -Path $OutDir -ChildPath "index.html"
Invoke-WebRequest -Uri $Url -OutFile $htmlFile

# Get the base URL
$baseUri = [System.Uri]$Url

# Parse the HTML to find all linked assets
$htmlContent = Get-Content -Path $htmlFile -Raw
$regex = '(?i)(?:href|src)=["''](?!https?://)([^"']+)["'']'
$matches = $htmlContent | Select-String -Pattern $regex -AllMatches

foreach ($match in $matches.Matches) {
    $assetUrl = $match.Groups[1].Value
    $absoluteAssetUrl = [System.Uri]$baseUri, $assetUrl
    $assetPath = Join-Path -Path $OutDir -ChildPath ($assetUrl -replace '/', '\')
    $assetDir = Split-Path -Path $assetPath -Parent

    # Create the directory for the asset if it doesn't exist
    if (-not (Test-Path -Path $assetDir)) {
        New-Item -ItemType Directory -Path $assetDir | Out-Null
    }

    # Download the asset
    try {
        Invoke-WebRequest -Uri $absoluteAssetUrl -OutFile $assetPath
    } catch {
        Write-Warning "Could not download $($absoluteAssetUrl)"
    }
}

# Rewrite the links in the HTML to be relative
$rewrittenHtml = $htmlContent
$matches | ForEach-Object {
    $oldLink = $_.Groups[1].Value
    $newLink = $oldLink -replace '/', '\' # Corrected: escaped backslash
    $rewrittenHtml = $rewrittenHtml -replace $oldLink, $newLink
}

$rewrittenHtml | Set-Content -Path $htmlFile
