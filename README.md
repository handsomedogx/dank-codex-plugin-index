# DMS Plugin Index

This repository is the public index and standards hub for my Dank Linux / DankMaterialShell plugin ecosystem.

It does not host plugin source code directly.
Each plugin lives in its own repository and is linked from here together with its demo video.

## What This Repository Contains

- development rules in `AGENTS.md`
- a public-facing plugin directory
- links to plugin repositories
- links to demo videos and previews

## Plugin Directory

Add one row per released or public plugin.

| Plugin | Repository | Demo Video | Status | Notes |
| --- | --- | --- | --- | --- |
| _Coming soon_ | Add repo link | Add video link | Planned | Plugin repositories will be linked here after migration |

Template for new entries:

```md
| Plugin Name | [GitHub](https://github.com/<user>/<repo>) | [Video](https://example.com/demo) | Active | Short description |
```

## Development Rules

Development standards for all plugins are maintained in [AGENTS.md](./AGENTS.md).

Core policy:

- this root repository tracks standards and navigation only
- each plugin must have its own independent Git repository
- plugin repositories should follow the shared DMS workflow documented in `AGENTS.md`
- commit messages use the format `<type>: <summary>`

## Repository Layout

```text
.
├── AGENTS.md
├── README.md
└── assets/            # optional screenshots, thumbnails, shared media
```

## Planned Additions

- plugin repository links
- demo video links
- screenshots or thumbnails
- release and compatibility notes
