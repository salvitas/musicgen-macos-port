# Contributing

This repo is a practical Apple Silicon port of AudioCraft/MusicGen.

## Before opening a PR
- Test generation on macOS Apple Silicon if possible
- Keep patches small and focused
- Avoid reintroducing xformers as a hard dependency on Darwin
- Update the README if you change setup or model-loading behavior

## Suggested workflow
1. Create an issue or describe the problem
2. Patch the fork in `vendor/audiocraft`
3. Run `python generate_shark.py`
4. Include logs and environment details in the PR

## Notes
- This repo aims for a reproducible local generation path on macOS.
- If you improve compatibility, include the exact dependency/version change.
