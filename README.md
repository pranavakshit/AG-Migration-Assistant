# AG Migration Assistant

This helper migrates legacy Antigravity data into Antigravity IDE.

It copies:

- `C:\Users\prana\.gemini\antigravity\conversations`
- `C:\Users\prana\.gemini\antigravity\brain`

into:

- `C:\Users\prana\.gemini\antigravity-ide\conversations`
- `C:\Users\prana\.gemini\antigravity-ide\brain`

Existing files and folders are skipped.

## Usage

```powershell
python -m ag_migration_assistant --dry-run
python -m ag_migration_assistant
```

You can also override the paths:

```powershell
python -m ag_migration_assistant --source "C:\path\to\antigravity" --target "C:\path\to\antigravity-ide"
```

## Release binaries

GitHub Actions builds Windows executables for:

- `win-x86`
- `win-x64`
- `win-arm64`

Download the matching asset from the GitHub Releases page.

## Safety

Back up both folders before running the migrator:

- `C:\Users\prana\.gemini\antigravity`
- `C:\Users\prana\.gemini\antigravity-ide`

