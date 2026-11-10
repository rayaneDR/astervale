param([Parameter(Mandatory=$true)][string]$Serial, [string]$OutputDirectory = '.\private\inventory')
$ErrorActionPreference='Stop'
# Read-only, narrow metadata. No notification, EFS, account or full log dump.
New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
$fields=@('ro.product.model','ro.product.device','ro.bootloader','gsm.version.baseband','ro.build.fingerprint','ro.build.version.security_patch','ro.boot.verifiedbootstate','ro.crypto.state')
$report=[ordered]@{label='untested'; collected_utc=[DateTime]::UtcNow.ToString('o')}
foreach($field in $fields) { $report[$field]=(& adb -s $Serial shell getprop $field | Out-String).Trim(); if($LASTEXITCODE -ne 0){throw "adb failed reading $field"} }
$report['kernel']=(& adb -s $Serial shell uname -a | Out-String).Trim()
$report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $OutputDirectory 'device.json') -Encoding utf8
Write-Output 'Private metadata saved. Review before sharing; no device setting was changed.'
