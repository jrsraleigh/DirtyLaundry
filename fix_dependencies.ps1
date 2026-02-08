Write-Host "===============================" -ForegroundColor Cyan
Write-Host " OSINT Dependency Auto-Fixer" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan

# Use current Python
$PY = "python"

# Upgrade core tools
Write-Host "[+] Updating pip..." -ForegroundColor Yellow
& $PY -m pip install --upgrade pip setuptools wheel

# ---------------- SHERLOCK ----------------

Write-Host "`n[+] Fixing Sherlock..." -ForegroundColor Green
Set-Location "$env:USERPROFILE\OSINT_Tools\sherlock"

if (Test-Path "requirements.txt") {
    & $PY -m pip install -r requirements.txt
}

# Extra common deps
& $PY -m pip install `
    requests `
    certifi `
    urllib3 `
    beautifulsoup4 `
    lxml `
    colorama `
    rich `
    pysocks `
    fake-useragent `
    tqdm

# ---------------- MAIGRET ----------------

Write-Host "`n[+] Fixing Maigret..." -ForegroundColor Green
Set-Location "$env:USERPROFILE\OSINT_Tools\maigret"

if (Test-Path "requirements.txt") {
    & $PY -m pip install -r requirements.txt
}

# Extra common deps
& $PY -m pip install `
    requests `
    aiohttp `
    certifi `
    urllib3 `
    beautifulsoup4 `
    lxml `
    colorama `
    rich `
    pysocks `
    fake-useragent `
    tqdm `
    aiocsv `
    aiodns `
    ujson `
    pycountry `
    python-dateutil

# ---------------- DONE ----------------

Write-Host "`n===============================" -ForegroundColor Cyan
Write-Host " All Dependencies Installed" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan

Pause
