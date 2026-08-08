# DFS Assets Local Sync Workflow

## For End-of-Session Backup to GitHub

### Quick Sync (after each session):
```bash
cd C:\Users\corry\dfs-assets-local
git add .
git commit -m "[SESSION] $(date '+%Y-%m-%d %H:%M') - Session updates"
git push origin main
```

### Or using this PowerShell script (Windows):
```powershell
# Save as: C:\Users\corry\sync-dfs.ps1
cd "C:\Users\corry\dfs-assets-local"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
git add .
git commit -m "[SESSION] $timestamp - Session updates"
git push origin main
```

Run after work:
```powershell
& "C:\Users\corry\sync-dfs.ps1"
```

## Token Efficiency

✅ **Local clone = massive token savings**:
- Avoid re-reading entire KB via GitHub API each session
- Just load local files (instant access)
- Only push changes at end of session
- No repeated Composio API calls for same content

## File Structure (Local)
```
C:\Users\corry\dfs-assets-local\
├── dfs-blog-base.css          (locked CSS)
├── dfs-blog-template-LOCKED.html (template)
├── validate-blog.js           (validator)
├── .git-hooks-pre-commit      (git hook)
├── BLOG-CREATION-PROCESS.md   (docs)
├── WORKLOG.md                 (session log)
├── [51 HTML files]            (blogs + landing pages)
└── .git/                       (version control)
```

## Workflow Benefits

1. **Fast**: Local file access = instant context (no API calls)
2. **Safe**: Git tracks all changes with full history
3. **Synced**: Push to GitHub at end of session
4. **Offline**: Work without internet (commit locally first)
5. **Collaborative**: GitHub is source of truth

## First Sync
Your local clone is already up-to-date with GitHub main branch.
