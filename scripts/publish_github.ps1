$ErrorActionPreference = "Continue"
$RepoName = "25_interactive_depth_completion_for_robots"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$StatusPath = Join-Path $Root "docs/github_publish_status.md"
Set-Location $Root

function Add-Line($Text) {
  Add-Content -Path $StatusPath -Value $Text
}

function Run-Step($Label, $Command, $ArgsList) {
  Add-Line ""
  Add-Line "## $Label"
  Add-Line ("Command: {0} {1}" -f $Command, ($ArgsList -join ' '))
  try {
    $out = & $Command @ArgsList 2>&1
    $code = $LASTEXITCODE
    if ($out) { Add-Line '```'; Add-Line ($out | Out-String).Trim(); Add-Line '```' }
    Add-Line "Exit code: $code"
    return $code
  } catch {
    Add-Line "Exception: $($_.Exception.Message)"
    return 999
  }
}

Set-Content -Path $StatusPath -Value "# GitHub Publish Status`n"
Add-Line "Started from $Root"

Run-Step "Git status before commit" "git" @("status", "--short") | Out-Null
Run-Step "Git add" "git" @("add", "-A") | Out-Null
$commitCode = Run-Step "Git commit" "git" @("commit", "-m", "Initial HCPP paper package")
if ($commitCode -ne 0) {
  Add-Line "Commit may have failed because there were no changes or git identity is missing; continuing to repo creation/push."
}

$authCode = Run-Step "GitHub auth status" "gh" @("auth", "status")
if ($authCode -ne 0) {
  Add-Line "GitHub auth is not available; cannot create or push public repo in this environment."
  exit 0
}

$login = ""
try {
  $login = (& gh api user --jq ".login" 2>$null).Trim()
} catch {
  $login = ""
}
if (-not $login) {
  Add-Line "Could not determine GitHub login; cannot publish."
  exit 0
}
Add-Line "GitHub login: $login"

$viewCode = Run-Step "Check repo exists" "gh" @("repo", "view", "$login/$RepoName")
if ($viewCode -ne 0) {
  Run-Step "Create public repo" "gh" @("repo", "create", $RepoName, "--public", "--source", ".", "--remote", "origin", "--description", "Anonymous ICLR-style paper package for interactive robot depth completion") | Out-Null
} else {
  $remote = (& git remote get-url origin 2>$null)
  if (-not $remote) {
    Run-Step "Add origin remote" "git" @("remote", "add", "origin", "https://github.com/$login/$RepoName.git") | Out-Null
  }
}

Run-Step "Push branch" "git" @("push", "-u", "origin", "HEAD") | Out-Null
Add-Line ""
Add-Line "GitHub URL: https://github.com/$login/$RepoName"
exit 0
