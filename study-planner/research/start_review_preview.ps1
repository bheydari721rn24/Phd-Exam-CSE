$studyPreviewRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../dist')).Path
$studyPreviewListener = Get-NetTCPConnection -LocalPort 8795 -State Listen -ErrorAction SilentlyContinue
if (-not $studyPreviewListener) {
    $studyPreviewProcess = Start-Process -FilePath 'C:/Users/bheydari/miniconda3/python.exe' -ArgumentList @('-m','http.server','8795','--bind','127.0.0.1','--directory',$studyPreviewRoot) -WindowStyle Hidden -PassThru
    Write-Output "Local study preview started on port 8795."
}
