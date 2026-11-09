# Dreamina Novel Plugin

This community plugin packages eight short-drama skills from `dreamina-skills` for Codex, ZCode, and Kimi. The installed `jimeng-novel` CLI performs the work; the plugin contains no account credentials. This is a local development candidate. The GitHub repository, release tag, and marketplace listing have not been published.

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

The skills are pinned to dreamina-skills commit `bbd13f8ba5ae6c85133d72ca07330e8496c3cfaa`. Command and model availability must be checked against the installed CLI. Local tests do not establish paid generation, host installation, or final film quality.
