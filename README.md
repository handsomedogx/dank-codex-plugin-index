# DMS Plugin Index

> Public home for my Dank Linux / DankMaterialShell plugin ecosystem.

This repository is the index, documentation hub, and showcase entry for my DMS plugins.
It does not host plugin source code directly.
Each plugin lives in its own repository and is linked here together with its demo video and compatibility notes.

## Quick Links

- Development rules: [AGENTS.md](./AGENTS.md)
- DMS docs: <https://danklinux.com/docs/>
- Plugin development guide: <https://danklinux.com/docs/dankmaterialshell/plugin-development>
- Official plugin registry: <https://plugins.danklinux.com/>

## Purpose

Use this repository to:

- publish shared plugin development standards
- maintain a public plugin directory
- link to plugin repositories
- link to demo videos, screenshots, and previews
- track compatibility and release notes at a high level

Do not use this repository to:

- store plugin source code
- keep temporary plugin working trees
- mix multiple plugin implementations into one monorepo

## Plugin Directory

Add one row per public or released plugin.

| Plugin | Type | Repository | Demo | DMS | Status | Summary |
| --- | --- | --- | --- | --- | --- | --- |
| _Coming soon_ | Widget | Add repo link | Add video link | 1.4+ | Planned | Public plugin repositories will appear here after migration |

Template for a new entry:

```md
| Plugin Name | Widget / Launcher / Daemon / Desktop | [GitHub](https://github.com/<user>/<repo>) | [Video](https://example.com/demo) | 1.4+ | Active | Short one-line description |
```

Recommended status labels:

- `Planned`
- `Active`
- `Beta`
- `Archived`

## Demo And Media Conventions

Each public plugin entry should eventually have:

- one repository link
- one video demo link
- one short summary line
- one compatibility note if needed

Optional local media can live under `assets/` using the plugin id or repo name:

```text
assets/
└── <plugin-id>/
    ├── cover.png
    ├── thumb.png
    └── notes.txt
```

Recommended demo coverage:

- show the widget or entry point
- show the main workflow in under 30 to 60 seconds
- show one real interaction, not only static screenshots

## Standards

Shared development standards for all plugins are maintained in [AGENTS.md](./AGENTS.md).

Core rules:

- this root repository tracks standards and navigation only
- each plugin must have its own independent Git repository
- plugin repositories should follow the shared DMS workflow documented in `AGENTS.md`
- commit messages use the format `<type>: <summary>`

Examples:

- `feat: add weather plugin entry`
- `docs: update plugin publishing rules`
- `fix: correct repository link for launcher plugin`

## Maintenance Workflow

When a new plugin becomes public:

1. create or publish the plugin in its own repository
2. add the repository link to the directory table above
3. add the demo video link
4. add screenshots or thumbnails under `assets/` if you want local previews
5. update compatibility or status if needed

## Repository Layout

```text
.
├── AGENTS.md
├── README.md
└── assets/
    └── .gitkeep
```

## Roadmap

- add live plugin entries after repository migration
- add thumbnails or covers for each public plugin
- add compatibility notes across DMS versions
- add release and changelog links for each plugin
