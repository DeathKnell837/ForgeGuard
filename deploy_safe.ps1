# ============================================================
# ForgeGuard Safe Deployment Forwarder
# ============================================================
param(
    [string]$Message = "chore: synchronize thesis workspace and system deployment"
)

& "$PSScriptRoot\deploy-forgeguard.ps1" -Message $Message
