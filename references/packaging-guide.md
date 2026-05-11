# Reference Audit Suite — Packaging Guide

## Overview

This document describes the packaging pattern used for the `reference-audit` skill suite,
a collection of 10 academic reference auditing modules bundled into a single GitHub-ready repository.

## Why Bundle Multiple Skills?

**User preference**: "整合包装成一个skill，方便封装成发布给github" (integrate and package as a single skill for easy GitHub publication).

**Benefits of bundling**:
- Single install command (`hermes skills install <url>`)
- Unified versioning and changelog
- Consistent dependencies and configuration
- Easier GitHub release management
- Reduced clutter in `~/.hermes/skills/`

## Bundle Structure

```
reference-audit/
├── SKILL.md                    # Main entry point, unified interface
├── INDEX.md                    # Module catalog with usage examples
├── README.md                   # English documentation
├── README.zh.md                # Chinese documentation
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT license
├── .gitignore                  # Git ignore rules
├── install.py                  # One-click install/uninstall script
├── Makefile                    # Build commands (install, test, clean)
├── check_repo.py               # Repository integrity validator
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml
│       └── feature_request.yml
├── modules/                    # OR: keep at root level
│   ├── cross-reference-audit.md
│   ├── citation-format-audit.md
│   ├── author-name-standardization.md
│   ├── doi-url-validation.md
│   ├── journal-name-consistency.md
│   ├── reference-existence-check.md
│   ├── year-version-consistency.md
│   ├── citation-context-verification.md
│   ├── academic-tone-audit.md
│   └── language-compliance.md
└── references/                 # Optional: session-specific details
    ├── api-quirks.md
    └── known-issues.md
```

## SKILL.md Pattern (Main Entry Point)

The main `SKILL.md` uses a **facade pattern**:

1. **Frontmatter**: Declares the suite as a single skill with version, description, and `related_skills` pointing to individual modules.
2. **Unified interface**: Provides a single command interface that dispatches to the appropriate module.
3. **Module registry**: Lists all included modules with brief descriptions.
4. **Quick start**: Shows how to use the suite as a whole.
5. **Module index**: References `INDEX.md` for detailed per-module documentation.

**Example frontmatter**:
```yaml
---
name: reference-audit
description: "Academic reference auditing suite: 10 professional modules for citation validation, format checking, and bibliography quality control."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [academic, research, writing, bibliography, citation, validation]
    related_skills: [academic-writing]
---
```

## INDEX.md Pattern (Module Catalog)

`INDEX.md` serves as the table of contents for the bundle:

- **Module list** with one-line descriptions
- **Usage matrix**: Which module to use for which task
- **Quick examples**: Copy-paste ready invocations
- **Workflow guides**: How to combine multiple modules in sequence

**Example structure**:
```markdown
# Reference Audit Suite — Module Index

## Available Modules

| # | Module | Purpose | Invocation |
|---|--------|---------|------------|
| 1 | cross-reference-audit | In-text citations match bibliography | `reference_audit("cross_reference", ...)` |
| 2 | citation-format-audit | Validate citation style (APA/MLA/GB-T) | `reference_audit("citation_format", ...)` |
...

## Quick Workflows

### Pre-submission audit (all modules)
```
reference_audit("all", paper_text="...")
```

### Fix broken citations only
```
reference_audit(["cross_reference", "reference_existence"], ...)
```
```

## Packaging for GitHub

### 1. Repository Initialization

```bash
cd ~/.hermes/skills/reference-audit
git init
git add .
git commit -m "feat: initial reference-audit suite v1.0.0"
```

### 2. GitHub Release

```bash
# Create repo on GitHub, then:
git remote add origin https://github.com/<user>/reference-audit.git
git push -u origin main

# Tag a release
git tag v1.0.0
git push origin v1.0.0
```

### 3. Install from GitHub

Users install the suite with:
```bash
hermes skills install https://github.com/<user>/reference-audit.git
```

Or install a specific release:
```bash
hermes skills install https://github.com/<user>/reference-audit/archive/refs/tags/v1.0.0.tar.gz
```

## Best Practices for Skill Bundles

1. **Single responsibility at module level**: Each module file should be independently usable.
2. **Clear separation**: Keep modules in a subdirectory (`modules/`) or use consistent naming (`*-audit.md`).
3. **Unified entry point**: `SKILL.md` should be the only file users need to read to understand the suite.
4. **Version together**: All modules share the same version number in the main `SKILL.md` frontmatter.
5. **Changelog at suite level**: Document changes across all modules in a single `CHANGELOG.md`.
6. **Test together**: Use `check_repo.py` to validate all module files are present and properly formatted.

## Converting Individual Skills to a Bundle

If you have existing individual skills and want to consolidate:

1. **Create bundle directory**: `mkdir -p ~/.hermes/skills/reference-audit/modules`
2. **Move skill files**: `mv skill1.md skill2.md modules/`
3. **Create main SKILL.md**: Copy frontmatter and unified interface from an existing skill.
4. **Create INDEX.md**: Document all modules with usage examples.
5. **Update frontmatter**: Add `related_skills` pointing to included modules.
6. **Test**: Run `check_repo.py` to verify integrity.
7. **Publish**: Follow GitHub release steps above.

## When to Bundle vs. Keep Separate

| Bundle | Separate |
|--------|----------|
| Tightly related modules (e.g., all reference checks) | Unrelated functionality |
| Shared configuration or dependencies | Independent lifecycles |
| Users typically use multiple modules together | Users use only one module |
| Want single install command | Want selective installation |
| Unified versioning makes sense | Modules evolve at different rates |

## Reference Files

- `references/system-health-check.md` — Monitoring and health check script pattern
- `references/tts-repair-20260507.md` — TTS troubleshooting workflow
- `references/qqbot-setup.md` — QQ Bot configuration guide
