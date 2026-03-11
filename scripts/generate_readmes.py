#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
CONTENT_PATH = ROOT / "content" / "site.json"
README_EN_PATH = ROOT / "README.md"
README_ZH_PATH = ROOT / "README.zh-CN.md"

LANGS = {
    "en": README_EN_PATH,
    "zh-CN": README_ZH_PATH,
}

TEXT = {
    "en": {
        "generated_notice": "AUTO-GENERATED FILE. Edit `content/site.json` or `scripts/generate_readmes.py` instead.",
        "start_here": "Start Here",
        "at_a_glance": "At A Glance",
        "featured": "Featured Plugins",
        "featured_intro": "Use this section for the plugins you want people to notice first. Keep it short and visual.",
        "coming_soon": "Coming Soon",
        "plugin": "Plugin",
        "type": "Type",
        "repository": "Repository",
        "demo": "Demo",
        "status": "Status",
        "summary": "Summary",
        "add_repo": "Add GitHub link",
        "add_demo": "Add video link",
        "planned": "Planned",
        "placeholder_summary": "Short one-line value proposition",
        "featured_template": "Template",
        "featured_template_block": "### Plugin Name\n\n- Plugin: `plugin-id`\n- Type: `Widget / Launcher / Daemon / Desktop`\n- Repository: [GitHub](https://github.com/<user>/<repo>)\n- Demo: [Video](https://example.com/demo)\n- Status: `Active`\n- Summary: one-line explanation of what makes the plugin useful",
        "directory": "Plugin Directory",
        "directory_intro": "Add one row per public or released plugin.",
        "dms": "DMS",
        "directory_row_template": "| Plugin Name | Widget / Launcher / Daemon / Desktop | [GitHub](https://github.com/<user>/<repo>) | [Video](https://example.com/demo) | 1.4+ | Active | Short one-line description |",
        "template_for_row": "Template for a new row",
        "recommended_statuses": "Recommended status labels",
        "status_active": "Active",
        "status_beta": "Beta",
        "status_archived": "Archived",
        "demo_media": "Demo And Media",
        "demo_media_intro": "Each public plugin entry should eventually have:",
        "media_repo": "one repository link",
        "media_demo": "one demo video link",
        "media_summary": "one concise summary",
        "media_compat": "one compatibility note if needed",
        "media_local": "Optional local media can live under `assets/` using the plugin id or repository name:",
        "media_coverage": "Recommended demo coverage:",
        "coverage_entry": "show the widget or entry point in the first few seconds",
        "coverage_flow": "show the main workflow in under 30 to 60 seconds",
        "coverage_real": "show one real interaction instead of only static screenshots",
        "standards": "Standards",
        "standards_intro": "Shared development standards for all plugins are maintained in [AGENTS.md](./AGENTS.md).",
        "core_rules": "Core rules",
        "rule_root": "this root repository tracks standards and navigation only",
        "rule_repo": "each plugin must have its own independent Git repository",
        "rule_workflow": "plugin repositories should follow the shared DMS workflow documented in `AGENTS.md`",
        "rule_commit": "commit messages use the format `<type>: <summary>`",
        "examples": "Examples",
        "example_1": "`feat: add weather plugin entry`",
        "example_2": "`docs: update plugin publishing rules`",
        "example_3": "`fix: correct repository link for launcher plugin`",
        "release_model": "Release Model",
        "release_steps": [
            "build and maintain the plugin in its own repository",
            "document installation and usage in that plugin repository",
            "publish demo material",
            "link the repository and video back here",
            "update compatibility and status when the plugin changes"
        ],
        "repo_layout": "Repository Layout",
        "roadmap": "Roadmap",
        "language_en": "English",
        "language_zh": "简体中文"
    },
    "zh-CN": {
        "generated_notice": "此文件为自动生成，请修改 `content/site.json` 或 `scripts/generate_readmes.py`。",
        "start_here": "快速入口",
        "at_a_glance": "仓库结构总览",
        "featured": "精选插件",
        "featured_intro": "这里用于展示你最希望访客优先看到的插件，尽量保持简洁和可视化。",
        "coming_soon": "即将加入",
        "plugin": "插件",
        "type": "类型",
        "repository": "仓库",
        "demo": "演示",
        "status": "状态",
        "summary": "简介",
        "add_repo": "补充 GitHub 链接",
        "add_demo": "补充视频链接",
        "planned": "计划中",
        "placeholder_summary": "一句话说明这个插件的价值",
        "featured_template": "模板",
        "featured_template_block": "### 插件名称\n\n- 插件: `plugin-id`\n- 类型: `Widget / Launcher / Daemon / Desktop`\n- 仓库: [GitHub](https://github.com/<user>/<repo>)\n- 演示: [Video](https://example.com/demo)\n- 状态: `活跃`\n- 简介: 用一句话说明这个插件为什么有用",
        "directory": "插件目录",
        "directory_intro": "每个公开或已发布的插件都在这里保留一行条目。",
        "dms": "DMS",
        "directory_row_template": "| 插件名称 | Widget / Launcher / Daemon / Desktop | [GitHub](https://github.com/<user>/<repo>) | [Video](https://example.com/demo) | 1.4+ | 活跃 | 一句话描述 |",
        "template_for_row": "新增条目模板",
        "recommended_statuses": "推荐状态标签",
        "status_active": "活跃",
        "status_beta": "测试中",
        "status_archived": "已归档",
        "demo_media": "演示与素材",
        "demo_media_intro": "每个公开插件条目最终最好都包含：",
        "media_repo": "一个仓库链接",
        "media_demo": "一个演示视频链接",
        "media_summary": "一条简洁摘要",
        "media_compat": "必要时补一条兼容性说明",
        "media_local": "可选的本地素材可以按插件 id 或仓库名放在 `assets/` 下：",
        "media_coverage": "推荐的演示内容：",
        "coverage_entry": "前几秒先展示组件或入口位置",
        "coverage_flow": "30 到 60 秒内完整展示一条主流程",
        "coverage_real": "尽量展示真实交互，而不是只放静态截图",
        "standards": "统一规范",
        "standards_intro": "所有插件共享的开发规范都维护在 [AGENTS.md](./AGENTS.md) 中。",
        "core_rules": "核心规则",
        "rule_root": "根仓库只跟踪规范、导航和展示信息",
        "rule_repo": "每个插件都必须拥有独立 Git 仓库",
        "rule_workflow": "插件仓库应遵循 `AGENTS.md` 中的共享 DMS 工作流",
        "rule_commit": "提交信息统一使用 `<type>: <summary>` 格式",
        "examples": "示例",
        "example_1": "`feat: add weather plugin entry`",
        "example_2": "`docs: update plugin publishing rules`",
        "example_3": "`fix: correct repository link for launcher plugin`",
        "release_model": "发布模型",
        "release_steps": [
            "在各自独立仓库中开发和维护插件",
            "在插件仓库中记录安装方式和使用说明",
            "发布演示素材",
            "将仓库链接和视频链接回填到这里",
            "在插件变化时同步更新兼容性和状态"
        ],
        "repo_layout": "仓库结构",
        "roadmap": "后续计划",
        "language_en": "English",
        "language_zh": "简体中文"
    }
}

STATUS_TEXT = {
    "planned": {"en": "Planned", "zh-CN": "计划中"},
    "active": {"en": "Active", "zh-CN": "活跃"},
    "beta": {"en": "Beta", "zh-CN": "测试中"},
    "archived": {"en": "Archived", "zh-CN": "已归档"},
}


def load_content() -> dict[str, Any]:
    return json.loads(CONTENT_PATH.read_text(encoding="utf-8"))


def localize(value: Any, lang: str) -> str:
    if isinstance(value, dict):
        if lang in value:
            return value[lang]
        if "en" in value:
            return value["en"]
    if isinstance(value, str):
        return value
    raise TypeError(f"Unsupported localized value: {value!r}")


def icon(name: str, alt: str, width: int = 18) -> str:
    return f'<img src="./assets/icons/{name}" width="{width}" alt="{alt}" />'


def link(label: str, href: str) -> str:
    return f"[{label}]({href})"


def maybe_link(label: str, href: str, fallback: str) -> str:
    return link(label, href) if href else fallback


def status_label(status_key: str, lang: str) -> str:
    return localize(STATUS_TEXT.get(status_key, STATUS_TEXT["planned"]), lang)


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_language_switch(lang: str) -> str:
    t = TEXT[lang]
    if lang == "en":
        return f"**{t['language_en']}** | [简体中文](./README.zh-CN.md)"
    return f"[English](./README.md) | **{t['language_zh']}**"


def render_highlights(content: dict[str, Any], lang: str) -> str:
    cells = []
    for item in content["highlights"]:
        title = localize(item["title"], lang)
        text = localize(item["text"], lang)
        cells.append(
            "\n".join(
                [
                    '<td width="25%" valign="top">',
                    f'{icon(item["icon"], title, 20)}',
                    "",
                    f"<strong>{title}</strong><br />",
                    text,
                    "</td>",
                ]
            )
        )
    return "\n".join(["<table>", "<tr>", *cells, "</tr>", "</table>"])


def render_featured(content: dict[str, Any], lang: str) -> list[str]:
    t = TEXT[lang]
    lines = [f"## {t['featured']}", "", t["featured_intro"], ""]
    if not content["featured"]:
        lines.extend(
            [
                f"### {t['coming_soon']}",
                "",
                f"- {t['plugin']}: `TBD`",
                f"- {t['type']}: `Widget`" if lang == "en" else f"- {t['type']}: `Widget`",
                f"- {t['repository']}: {t['add_repo']}",
                f"- {t['demo']}: {t['add_demo']}",
                f"- {t['status']}: `{t['planned']}`",
                f"- {t['summary']}: {t['placeholder_summary']}",
                "",
            ]
        )
    else:
        for item in content["featured"]:
            lines.extend(
                [
                    f"### {item['name']}",
                    "",
                    f"- {t['plugin']}: `{item['plugin_id']}`",
                    f"- {t['type']}: `{localize(item['type'], lang)}`",
                    f"- {t['repository']}: {maybe_link('GitHub', item.get('repository_url', ''), t['add_repo'])}",
                    f"- {t['demo']}: {maybe_link('Video', item.get('demo_url', ''), t['add_demo'])}",
                    f"- {t['status']}: `{status_label(item.get('status', 'planned'), lang)}`",
                    f"- {t['summary']}: {localize(item['summary'], lang)}",
                    "",
                ]
            )

    lines.extend([f"**{t['featured_template']}**", "", "```md", t["featured_template_block"], "```"])
    return lines


def render_plugin_rows(content: dict[str, Any], lang: str) -> list[str]:
    t = TEXT[lang]
    lines = [
        f"## {t['directory']}",
        "",
        t["directory_intro"],
        "",
        f"| {t['plugin']} | {t['type']} | {t['repository']} | {t['demo']} | {t['dms']} | {t['status']} | {t['summary']} |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    if not content["plugins"]:
        lines.append(
            f"| _{t['coming_soon']}_ | Widget | {t['add_repo']} | {t['add_demo']} | 1.4+ | {t['planned']} | {t['placeholder_summary']} |"
        )
    else:
        for item in content["plugins"]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        escape_cell(item["name"]),
                        escape_cell(localize(item["type"], lang)),
                        escape_cell(maybe_link("GitHub", item.get("repository_url", ""), t["add_repo"])),
                        escape_cell(maybe_link("Video", item.get("demo_url", ""), t["add_demo"])),
                        escape_cell(item.get("dms", "1.4+")),
                        escape_cell(status_label(item.get("status", "planned"), lang)),
                        escape_cell(localize(item["summary"], lang)),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            f"**{t['template_for_row']}**",
            "",
            "```md",
            t["directory_row_template"],
            "```",
            "",
            f"**{t['recommended_statuses']}**",
            "",
            f"- `{t['planned']}`",
            f"- `{t['status_active']}`",
            f"- `{t['status_beta']}`",
            f"- `{t['status_archived']}`",
        ]
    )
    return lines


def render_readme(content: dict[str, Any], lang: str) -> str:
    t = TEXT[lang]
    lines = [
        f"<!-- {t['generated_notice']} -->",
        "",
        '<p align="center">',
        f'  <img src="./assets/icons/index.svg" width="92" alt="{content["title"]} icon" />',
        "</p>",
        "",
        f"# {content['title']}",
        "",
        f"> {localize(content['tagline'], lang)}",
        "",
        render_language_switch(lang),
        "",
    ]

    lines.extend(localize(content["intro"], lang))
    lines.extend(["", f"## {t['start_here']}", ""])

    for item in content["quick_links"]:
        lines.append(f"- {link(localize(item['label'], lang), item['href'])}")

    lines.extend(["", f"## {t['at_a_glance']}", "", render_highlights(content, lang), ""])
    lines.extend(render_featured(content, lang))
    lines.extend([""])
    lines.extend(render_plugin_rows(content, lang))
    lines.extend(
        [
            "",
            f"## {t['demo_media']}",
            "",
            t["demo_media_intro"],
            "",
            f"- {t['media_repo']}",
            f"- {t['media_demo']}",
            f"- {t['media_summary']}",
            f"- {t['media_compat']}",
            "",
            t["media_local"],
            "",
            "```text",
            "assets/",
            "└── <plugin-id>/",
            "    ├── cover.png",
            "    ├── thumb.png",
            "    └── notes.txt",
            "```",
            "",
            f"**{t['media_coverage']}**",
            "",
            f"- {t['coverage_entry']}",
            f"- {t['coverage_flow']}",
            f"- {t['coverage_real']}",
            "",
            f"## {t['standards']}",
            "",
            t["standards_intro"],
            "",
            f"**{t['core_rules']}**",
            "",
            f"- {t['rule_root']}",
            f"- {t['rule_repo']}",
            f"- {t['rule_workflow']}",
            f"- {t['rule_commit']}",
            "",
            f"**{t['examples']}**",
            "",
            f"- {t['example_1']}",
            f"- {t['example_2']}",
            f"- {t['example_3']}",
            "",
            f"## {t['release_model']}",
            "",
        ]
    )

    for index, step in enumerate(t["release_steps"], start=1):
        lines.append(f"{index}. {step}")

    lines.extend(
        [
            "",
            f"## {t['repo_layout']}",
            "",
            "```text",
            ".",
            "├── AGENTS.md",
            "├── README.md",
            "├── README.zh-CN.md",
            "├── content/",
            "│   └── site.json",
            "├── scripts/",
            "│   └── generate_readmes.py",
            "└── assets/",
            "    ├── .gitkeep",
            "    └── icons/",
            "```",
            "",
            f"## {t['roadmap']}",
            "",
        ]
    )

    for item in localize(content["roadmap"], lang):
        lines.append(f"- {item}")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    content = load_content()
    for lang, path in LANGS.items():
        path.write_text(render_readme(content, lang), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
