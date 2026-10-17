$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$taskSpeaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
  $taskVoices = @($taskSpeaker.GetInstalledVoices() | Where-Object { $_.Enabled -and $_.VoiceInfo.Culture.Name -like 'en-*' })
  if ($taskVoices.Count -eq 0) { throw 'No English speech voice is available.' }
  $taskVoice = $taskVoices | Sort-Object @{Expression={$_.VoiceInfo.Name}} | Select-Object -First 1
  $taskSpeaker.SelectVoice($taskVoice.VoiceInfo.Name)
  $taskAudioPath = Join-Path (Split-Path $PSScriptRoot -Parent) 'dist/ielts/audio'
  $taskClips = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'ielts/session3-audio.json') -Raw | ConvertFrom-Json
  $taskItems = @()
  foreach ($taskClip in $taskClips) {
    foreach ($taskRate in @(@{name='guided'; rate=-2}, @{name='ordinary'; rate=0})) {
      $taskName = $taskClip.id + '-' + $taskRate.name + '.wav'
      $taskSpeaker.Rate = $taskRate.rate
      $taskSpeaker.SetOutputToWaveFile((Join-Path $taskAudioPath $taskName))
      $taskSpeaker.Speak($taskClip.text)
      $taskSpeaker.SetOutputToNull()
      $taskItems += @{file=$taskName; transcript=$taskClip.text; voice=$taskVoice.VoiceInfo.Name; rate=$taskRate.rate; origin='Original synthetic teaching audio; not an official IELTS recording'}
    }
  }
  ConvertTo-Json -InputObject @($taskItems) -Depth 4 | Set-Content -LiteralPath (Join-Path $taskAudioPath 'session3-manifest.json') -Encoding UTF8
  Write-Output ('Generated ' + $taskItems.Count + ' original Session3 clips.')
} finally { $taskSpeaker.Dispose() }
