$ErrorActionPreference = 'Continue'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
$Paper = Join-Path $Root 'paper'
$DownloadsPdf = 'C:\Users\wangz\Downloads\25.pdf'
$Status = Join-Path $Paper 'build_status.txt'

Set-Content -LiteralPath $Status -Value "Build started at $((Get-Date).ToString('o'))" -Encoding UTF8

function Run-Step {
    param(
        [string] $Name,
        [string] $Command,
        [string[]] $ArgsList
    )
    Add-Content -LiteralPath $Status -Value "RUN ${Name}: $Command $($ArgsList -join ' ')"
    $psi = [System.Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $Command
    $psi.Arguments = $ArgsList -join ' '
    $psi.WorkingDirectory = $Paper
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $process = [System.Diagnostics.Process]::Start($psi)
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()
    $lines = (($stdout + $stderr) -split "`r?`n") | ForEach-Object { $_.TrimEnd() }
    while (($lines.Count -gt 0) -and ($lines[$lines.Count - 1] -eq '')) {
        if ($lines.Count -eq 1) {
            $lines = @()
        } else {
            $lines = $lines[0..($lines.Count - 2)]
        }
    }
    Set-Content -LiteralPath (Join-Path $Paper "${Name}.output.txt") -Value $lines -Encoding UTF8
    $code = $process.ExitCode
    Add-Content -LiteralPath $Status -Value "EXIT ${Name}: $code"
    return $code
}

Push-Location $Paper
$c1 = Run-Step 'pdflatex1' 'pdflatex' @('-interaction=nonstopmode', '-halt-on-error', 'main.tex')
$cb = Run-Step 'bibtex' 'bibtex' @('main')
$c2 = Run-Step 'pdflatex2' 'pdflatex' @('-interaction=nonstopmode', '-halt-on-error', 'main.tex')
$c3 = Run-Step 'pdflatex3' 'pdflatex' @('-interaction=nonstopmode', '-halt-on-error', 'main.tex')
Pop-Location

$LocalPdf = Join-Path $Paper 'main.pdf'
if (($c1 -eq 0) -and ($cb -eq 0) -and ($c2 -eq 0) -and ($c3 -eq 0) -and (Test-Path -LiteralPath $LocalPdf)) {
    Copy-Item -LiteralPath $LocalPdf -Destination $DownloadsPdf -Force
    Add-Content -LiteralPath $Status -Value "PDF copied to $DownloadsPdf"
    Remove-Item -LiteralPath $LocalPdf -Force
    Add-Content -LiteralPath $Status -Value "Local paper/main.pdf removed after canonical copy"
    Add-Content -LiteralPath $Status -Value "Build finished at $((Get-Date).ToString('o'))"
    exit 0
}

Add-Content -LiteralPath $Status -Value "Build failed or PDF missing"
Add-Content -LiteralPath $Status -Value "Build finished at $((Get-Date).ToString('o'))"
exit 1
