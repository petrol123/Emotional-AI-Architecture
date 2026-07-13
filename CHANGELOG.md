# Changelog

All notable changes to **Emotional-AI-Architecture** will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

---

## [Unreleased]

### Planned for v1.1.0
- Unified CI/CD pipeline with GitHub Actions across all 12 modules
- Cross-module integration test suite under `tests/`
- Auto-generated API documentation via Sphinx / MkDocs, published to GitHub Pages
- Docker-based development environment (`Dockerfile` + `docker-compose.yml`)
- `CONTRIBUTING.md` — formal contribution guidelines, branch conventions, and RFC process

---

## [1.0.0] — 2026-07-13

### Summary
First stable release of the **Emotional-AI-Architecture** monorepo. This release consolidates 12 previously independent repositories into a single unified codebase using Git subtree merges, with full commit history preserved for all components.

### Added
- Unified monorepo structure under `modules/` containing all 12 component modules:
  - `modules/affect-engine`
  - `modules/emotion-classifier`
  - `modules/sentiment-bridge`
  - `modules/cognitive-appraisal`
  - `modules/mood-state-machine`
  - `modules/empathy-models`
  - `modules/social-signal-processing`
  - `modules/valence-arousal-core`
  - `modules/facial-affect-parser`
  - `modules/multimodal-fusion`
  - `modules/dialogue-emotion-tracker`
  - `modules/affective-memory`
- `shared/` directory for cross-module schemas, utilities, and type definitions
- `docs/` directory with `architecture/` and `api/` subdirectories
- `tests/` directory (root-level, reserved for cross-module integration tests in v1.1.0)
- `scripts/` directory for developer tooling and release automation
- Root-level `README.md` — project overview, module index, and getting-started guide
- `MONOREPO_STRUCTURE.md` — complete layout documentation, module purposes, and inter-module relationships
- `CHANGELOG.md` — this file
- `pyproject.toml` — top-level project configuration
- Unified semantic versioning (`v1.0.0`) applied across all 12 modules

### Merge Strategy
All 12 repositories were incorporated via `git subtree add`, preserving full commit history inline. No history was squashed. Each component's history is accessible via `git log --follow modules/<module-name>/`.

| Module Directory | Original Repository |
|---|---|
| `modules/affect-engine` | `org/affect-engine-lib` |
| `modules/emotion-classifier` | `org/emotion-classifier-core` |
| `modules/sentiment-bridge` | `org/sentiment-bridge-adapter` |
| `modules/cognitive-appraisal` | `org/cognitive-appraisal-engine` |
| `modules/mood-state-machine` | `org/mood-state-machine-lib` |
| `modules/empathy-models` | `org/empathy-models-research` |
| `modules/social-signal-processing` | `org/social-signal-proc` |
| `modules/valence-arousal-core` | `org/vad-core-lib` |
| `modules/facial-affect-parser` | `org/facial-affect-parser` |
| `modules/multimodal-fusion` | `org/multimodal-fusion-layer` |
| `modules/dialogue-emotion-tracker` | `org/dialogue-emotion-tracker` |
| `modules/affective-memory` | `org/affective-memory-store` |

### Migration Notes
Users of any predecessor standalone repository should update import paths to the unified package:

```python
# Before
from affect_engine.core import AffectRuntime

# After
from emotional_ai_architecture.modules.affect_engine.core import AffectRuntime
