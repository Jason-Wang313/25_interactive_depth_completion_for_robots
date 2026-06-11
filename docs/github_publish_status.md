# GitHub Publish Status

Started from C:\Users\wangz\robotics_60_paper_batch\25_interactive_depth_completion_for_robots

## Git status before commit
Command: git status --short
```
?? .gitignore
?? README.md
?? child_status.md
?? data/
?? docs/
?? experiments/
?? paper/
?? plan.md
?? requirements.txt
?? scripts/
```
Exit code: 0

## Git add
Command: git add -A
```
git.exe : warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
At C:\Users\wangz\robotics_60_paper_batch\25_interactive_depth_completion_for_robots\scripts\publish_github.ps1:16 
char:12
+     $out = & $Command @ArgsList 2>&1
+            ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
warning: in the working copy of 'child_status.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/github_publish_status.md', LF will be replaced by CRLF the next time Git touches 
it
warning: in the working copy of 'paper/iclr2026_conference.bst', LF will be replaced by CRLF the next time Git touches 
it
warning: in the working copy of 'paper/iclr2026_conference.sty', LF will be replaced by CRLF the next time Git touches 
it
warning: in the working copy of 'paper/main.tex', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'plan.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'requirements.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/fetch_literature.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/finalize_audit.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/make_paper.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/publish_github.ps1', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/run_experiment.py', LF will be replaced by CRLF the next time Git touches it
```
Exit code: 0

## Git commit
Command: git commit -m Initial HCPP paper package
```
[master (root-commit) f18fa47] Initial HCPP paper package
 34 files changed, 66446 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 child_status.md
 create mode 100644 data/literature_progress.txt
 create mode 100644 data/openalex_works.jsonl
 create mode 100644 data/top_references.bib
 create mode 100644 docs/claims.md
 create mode 100644 docs/github_publish_status.md
 create mode 100644 docs/hostile_prior_work.md
 create mode 100644 docs/literature_map.md
 create mode 100644 docs/novelty_boundary_map.md
 create mode 100644 docs/novelty_decision.md
 create mode 100644 docs/related_work_matrix.csv
 create mode 100644 docs/reviewer_attacks.md
 create mode 100644 experiments/results/baseline_sensitivity.png
 create mode 100644 experiments/results/episode_results.csv
 create mode 100644 experiments/results/example_scene.png
 create mode 100644 experiments/results/rmse_by_method.png
 create mode 100644 experiments/results/summary.json
 create mode 100644 experiments/results/summary.md
 create mode 100644 paper/iclr2026.zip
 create mode 100644 paper/iclr2026_conference.bst
 create mode 100644 paper/iclr2026_conference.sty
 create mode 100644 paper/main.pdf
 create mode 100644 paper/main.tex
 create mode 100644 paper/references.bib
 create mode 100644 paper/template_source.txt
 create mode 100644 plan.md
 create mode 100644 requirements.txt
 create mode 100644 scripts/fetch_literature.py
 create mode 100644 scripts/finalize_audit.py
 create mode 100644 scripts/make_paper.py
 create mode 100644 scripts/publish_github.ps1
 create mode 100644 scripts/run_experiment.py
```
Exit code: 0

## GitHub auth status
Command: gh auth status
```
github.com
  ✓ Logged in to github.com account Jason-Wang313 (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_************************************
  - Token scopes: 'gist', 'read:org', 'repo'
```
Exit code: 0
GitHub login: Jason-Wang313

## Check repo exists
Command: gh repo view Jason-Wang313/25_interactive_depth_completion_for_robots
```
gh.exe : GraphQL: Could not resolve to a Repository with the name 
'Jason-Wang313/25_interactive_depth_completion_for_robots'. (repository)
At C:\Users\wangz\robotics_60_paper_batch\25_interactive_depth_completion_for_robots\scripts\publish_github.ps1:16 
char:12
+     $out = & $Command @ArgsList 2>&1
+            ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (GraphQL: Could ...'. (repository):String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
```
Exit code: 1

## Create public repo
Command: gh repo create 25_interactive_depth_completion_for_robots --public --source . --remote origin --description Anonymous ICLR-style paper package for interactive robot depth completion
```
https://github.com/Jason-Wang313/25_interactive_depth_completion_for_robots
```
Exit code: 0

## Push branch
Command: git push -u origin HEAD
```
git.exe : remote: warning: See https://gh.io/lfs for more information.        
At C:\Users\wangz\robotics_60_paper_batch\25_interactive_depth_completion_for_robots\scripts\publish_github.ps1:16 
char:12
+     $out = & $Command @ArgsList 2>&1
+            ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (remote: warning...mation.        :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
remote: warning: File data/openalex_works.jsonl is 90.33 MB; this is larger than GitHub's recommended maximum file 
size of 50.00 MB        
remote: warning: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com. 
       
To https://github.com/Jason-Wang313/25_interactive_depth_completion_for_robots.git
 * [new branch]      HEAD -> master
branch 'master' set up to track 'origin/master'.
```
Exit code: 0

GitHub URL: https://github.com/Jason-Wang313/25_interactive_depth_completion_for_robots
