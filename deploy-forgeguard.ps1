# ============================================================
# ForgeGuard Dual-Remote Safe Deployment Script
# ============================================================
# Ensures:
# 1. origin (NDMC-BSCS-THESIS-PREP) receives the Master Academic Thesis Hub README
# 2. forgeguard (ForgeGuard) receives the Software Engineering System README
# ============================================================

param(
    [string]$Message = "chore: synchronize thesis workspace and system deployment"
)

$ErrorActionPreference = "Stop"
$repoRoot = $PSScriptRoot

Write-Host ">>> [1/5] Checking Git workspace status..." -ForegroundColor Cyan
Set-Location $repoRoot

# Ensure academic README is backed up
$academicReadme = Get-Content (Join-Path $repoRoot "README.md") -Raw
$systemReadme = Get-Content (Join-Path $repoRoot "thesis-system\README.md") -Raw

# 1. Commit any current workspace changes with Academic README to origin
Write-Host ">>> [2/5] Staging and pushing academic thesis prep to origin..." -ForegroundColor Cyan
git add -A
$status = git status --porcelain
if ($status) {
    git commit -m $Message
}
git push origin main
Write-Host "[OK] origin (NDMC-BSCS-THESIS-PREP) updated with Academic Thesis Hub README." -ForegroundColor Green

# 2. Swap in System README for forgeguard deployment
Write-Host ">>> [3/5] Preparing system deployment for forgeguard..." -ForegroundColor Cyan
Set-Content -Path (Join-Path $repoRoot "README.md") -Value $systemReadme -NoNewline
git add README.md
$status = git status --porcelain
if ($status) {
    git commit -m "chore(deploy): set system README for ForgeGuard production release"
}
git push forgeguard main:main
Write-Host "[OK] forgeguard (ForgeGuard) updated with Software Engineering System README." -ForegroundColor Green

# 3. Restore Academic README on main
Write-Host ">>> [4/5] Restoring Academic Thesis Hub README for local main and origin..." -ForegroundColor Cyan
Set-Content -Path (Join-Path $repoRoot "README.md") -Value $academicReadme -NoNewline
git add README.md
$status = git status --porcelain
if ($status) {
    git commit -m "docs: restore master academic thesis workspace README"
    git push origin main
}
Write-Host "[OK] Local main and origin successfully restored to Academic Thesis Hub README." -ForegroundColor Green

Write-Host ">>> [5/5] Dual-Remote Synchronization Complete! Zero interference." -ForegroundColor Yellow
