# Dreamina Novel Plugin

This community plugin packages eight short-drama skills from `dreamina-skills` for Codex, ZCode, and Kimi. The installed `jimeng-novel` CLI performs the work; the plugin contains no account credentials. This is a release candidate. The GitHub repository exists; the plugin release and marketplace listing are published separately.

## Capabilities

- Start from an idea, novel, script, storyboard, or existing media and reuse the provided context and local assets.
- Cover script development, cast and locations, storyboards, sample clips, batch generation, local revision, subtitles, and final composition.
- Quote each paid generation batch and wait for approval. Resume uncertain tasks by querying their original identity.

## Local use

Check `jimeng-novel --help`, `jimeng-novel version`, and `jimeng-novel status`. If the CLI is missing, follow `dreamina-novel-cli-setup` and its official installation source. A host can load the plugin from this directory's `skills/`; marketplace installation requires a published repository and release.

## Verification

```bash
python3 -m unittest discover -s tests -q
python3 scripts/verify_vendored_skills.py
```

The skills are pinned to dreamina-skills commit `87c7f92d38fab1e937ae1c1231a229f7237b1ec0`. Command and model availability must be checked against the installed CLI. Local tests do not establish paid generation, host installation, or final film quality.
