$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$taskSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
  $taskVoices = @($taskSynthesizer.GetInstalledVoices() | Where-Object { $_.Enabled -and $_.VoiceInfo.Culture.Name -like 'en-*' })
  if ($taskVoices.Count -eq 0) { throw 'No installed English speech voice is available.' }
  $taskSelectedVoice = $taskVoices | Sort-Object @{Expression={if ($_.VoiceInfo.Culture.Name -eq 'en-GB') {0} else {1}}}, @{Expression={$_.VoiceInfo.Name}} | Select-Object -First 1
  $taskSynthesizer.SelectVoice($taskSelectedVoice.VoiceInfo.Name)
  $taskOutput = Join-Path (Split-Path $PSScriptRoot -Parent) 'dist/ielts/audio'
  New-Item -ItemType Directory -Path $taskOutput -Force | Out-Null
  $taskClips = @(
    @{id='be-demonstration'; text='I am a student. You are my teacher. Emma is a student. Alex is a teacher. We are in room fourteen. They are not late. Is Emma a teacher? No, she is not. Are you a student? Yes, I am.'},
    @{id='name-and-room'; text='Hello. My name is Emma. Emma. E. M. M. A. I am a student. My class is in room fourteen. Fourteen. One. Four. Alex is the teacher. We are ready.'},
    @{id='corrected-number'; text='Is your room thirteen? No. My room is thirty. Thirty. Three. Zero. Is your teacher Emma? No. My teacher is Alex. A. L. E. X. The class is ready.'}
  )
  $taskManifest = @()
  foreach ($taskClip in $taskClips) {
    foreach ($taskVersion in @(@{name='guided'; rate=-2}, @{name='natural-rate'; rate=0})) {
      $taskFilename = $taskClip.id + '-' + $taskVersion.name + '.wav'
      $taskTarget = Join-Path $taskOutput $taskFilename
      $taskSynthesizer.Rate = $taskVersion.rate
      $taskSynthesizer.SetOutputToWaveFile($taskTarget)
      $taskSynthesizer.Speak($taskClip.text)
      $taskSynthesizer.SetOutputToNull()
      $taskManifest += @{id=$taskClip.id; version=$taskVersion.name; file=$taskFilename; transcript=$taskClip.text; rate=$taskVersion.rate; voice=$taskSelectedVoice.VoiceInfo.Name; culture=$taskSelectedVoice.VoiceInfo.Culture.Name; origin='Original synthetic teaching audio; not an official IELTS recording'; generatedAtUtc=[DateTime]::UtcNow.ToString('o')}
    }
  }
  ConvertTo-Json -InputObject @($taskManifest) -Depth 4 | Set-Content -LiteralPath (Join-Path $taskOutput 'manifest.json') -Encoding UTF8
  Write-Output ('Generated ' + $taskManifest.Count + ' original clips with ' + $taskSelectedVoice.VoiceInfo.Name)
} finally { $taskSynthesizer.Dispose() }
