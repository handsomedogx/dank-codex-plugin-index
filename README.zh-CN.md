<!-- 此文件为自动生成，请修改 `content/site.json` 或 `scripts/generate_readmes.py`。 -->

<p align="center">
  <img src="./assets/icons/index.svg" width="92" alt="DMS Plugin Index icon" />
</p>

# DMS Plugin Index

> 独立 DMS 插件，共享开发规范，统一公开目录。

[English](./README.md) | **简体中文**

`DMS Plugin Index` 是我维护的 Dank Linux / DankMaterialShell 插件生态公开入口页。
这个仓库用于维护共享规范、插件索引链接、演示视频入口，以及高层级兼容性说明。
插件源码不放在这里。每个插件都会在各自独立的仓库中开发和发布。

## 快速入口

- [开发规范](./AGENTS.md)
- [DMS 文档](https://danklinux.com/docs/)
- [插件开发指南](https://danklinux.com/docs/dankmaterialshell/plugin-development)
- [官方插件注册表](https://plugins.danklinux.com/)

## 仓库结构总览

<table>
<tr>
<td width="25%" valign="top">
<img src="./assets/icons/repo.svg" width="20" alt="一插件一仓库" />

<strong>一插件一仓库</strong><br />
每个公开插件都维护在独立源码仓库中，并独立进行发布。
</td>
<td width="25%" valign="top">
<img src="./assets/icons/rules.svg" width="20" alt="统一开发规范" />

<strong>统一开发规范</strong><br />
这个根仓库集中维护工作流、约定和发布规范。
</td>
<td width="25%" valign="top">
<img src="./assets/icons/video.svg" width="20" alt="视频优先展示" />

<strong>视频优先展示</strong><br />
每个插件条目都可以链接到一个展示真实工作流的简短演示视频。
</td>
<td width="25%" valign="top">
<img src="./assets/icons/spark.svg" width="20" alt="公开插件目录" />

<strong>公开插件目录</strong><br />
仓库链接、兼容性说明和插件摘要会统一收敛在一个公开目录里。
</td>
</tr>
</table>

## 精选插件

这里用于展示你最希望访客优先看到的插件，尽量保持简洁和可视化。

### 即将加入

- 插件: `TBD`
- 类型: `Widget`
- 仓库: 补充 GitHub 链接
- 演示: 补充视频链接
- 状态: `计划中`
- 简介: 一句话说明这个插件的价值

**模板**

```md
### 插件名称

- 插件: `plugin-id`
- 类型: `Widget / Launcher / Daemon / Desktop`
- 仓库: [GitHub](https://github.com/<user>/<repo>)
- 演示: [Video](https://example.com/demo)
- 状态: `活跃`
- 简介: 用一句话说明这个插件为什么有用
```

## 插件目录

每个公开或已发布的插件都在这里保留一行条目。

| 插件 | 类型 | 仓库 | 演示 | DMS | 状态 | 简介 |
| --- | --- | --- | --- | --- | --- | --- |
| _即将加入_ | Widget | 补充 GitHub 链接 | 补充视频链接 | 1.4+ | 计划中 | 一句话说明这个插件的价值 |

**新增条目模板**

```md
| 插件名称 | Widget / Launcher / Daemon / Desktop | [GitHub](https://github.com/<user>/<repo>) | [Video](https://example.com/demo) | 1.4+ | 活跃 | 一句话描述 |
```

**推荐状态标签**

- `计划中`
- `活跃`
- `测试中`
- `已归档`

## 演示与素材

每个公开插件条目最终最好都包含：

- 一个仓库链接
- 一个演示视频链接
- 一条简洁摘要
- 必要时补一条兼容性说明

可选的本地素材可以按插件 id 或仓库名放在 `assets/` 下：

```text
assets/
└── <plugin-id>/
    ├── cover.png
    ├── thumb.png
    └── notes.txt
```

**推荐的演示内容：**

- 前几秒先展示组件或入口位置
- 30 到 60 秒内完整展示一条主流程
- 尽量展示真实交互，而不是只放静态截图

## 统一规范

所有插件共享的开发规范都维护在 [AGENTS.md](./AGENTS.md) 中。

**核心规则**

- 根仓库只跟踪规范、导航和展示信息
- 每个插件都必须拥有独立 Git 仓库
- 插件仓库应遵循 `AGENTS.md` 中的共享 DMS 工作流
- 提交信息统一使用 `<type>: <summary>` 格式

**示例**

- `feat: add weather plugin entry`
- `docs: update plugin publishing rules`
- `fix: correct repository link for launcher plugin`

## 发布模型

1. 在各自独立仓库中开发和维护插件
2. 在插件仓库中记录安装方式和使用说明
3. 发布演示素材
4. 将仓库链接和视频链接回填到这里
5. 在插件变化时同步更新兼容性和状态

## 仓库结构

```text
.
├── AGENTS.md
├── README.md
├── README.zh-CN.md
├── content/
│   └── site.json
├── scripts/
│   └── generate_readmes.py
└── assets/
    ├── .gitkeep
    └── icons/
```

## 后续计划

- 在插件仓库迁移完成后补充真实条目
- 补充带仓库链接和视频链接的精选插件
- 为每个公开插件补充缩略图或封面图
- 补充跨 DMS 版本的兼容性说明
- 补充每个插件的发布页和更新日志链接
