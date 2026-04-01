# MusicGen macOS Port


## Status

[![macOS](https://img.shields.io/badge/macOS-Apple%20Silicon-brightgreen)](https://github.com/salvitas/musicgen-macos-port)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Torch](https://img.shields.io/badge/PyTorch-2.5.1-ee4c2c)](https://pytorch.org/)

Apple Silicon-friendly local MusicGen setup built from a patched Audiocraft fork.

## What works
- MusicGen import on macOS / Apple Silicon
- Generation with `facebook/musicgen-small`
- No xformers runtime dependency on macOS

## Quick start

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e vendor/audiocraft --no-deps
python generate_shark.py
```

## Notes

- This port patches Audiocraft to avoid xformers on Darwin.
- `shark_cue.wav` is generated locally at 32 kHz mono.
- For community sharing, keep the vendored fork and this patch set together.

## What changed
- Patched Audiocraft for macOS / Apple Silicon
- Removed xformers runtime path on Darwin
- Added a lightweight shark-cue generator script
- Pinned a working dependency set for local generation

## Contributor notes
- Keep the macOS fallback path free of xformers hard requirements
- If you update model loading, verify `facebook/musicgen-small` still generates locally

## Security note

GitHub Dependabot may flag the pinned PyTorch version in this port. The repo keeps a tested, Apple Silicon-friendly stack so generation continues to work locally. If you upgrade Torch for security reasons, re-test the patched Audiocraft fork and generation path before publishing a change.
