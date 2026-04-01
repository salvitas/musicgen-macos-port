# MusicGen macOS Port

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
