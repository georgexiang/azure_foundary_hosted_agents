# PROJECT: Azure AI Foundry Hosted Agents — Skillable Agent Extension

## Vision
在现有 Azure AI Foundry Hosted Agent 示例集合中，新增一个支持安装外部标准 Skill（SKILL.md 格式，兼容 OpenClaw/ClawHub 生态）的代理子项目。

## Problem
当前项目有 12 个代理示例，覆盖了工具集成、RAG、多代理工作流、HITL 等场景，但缺少 **Skill 可组合架构** 的示例。用户无法通过声明式配置加载外部知识/能力包（Skill），每次修改代理行为都需要改代码。

## Solution
创建 `agent-framework/agent-with-skills/` 子项目：
- 支持 SKILL.md 标准格式（YAML frontmatter + Markdown 正文）
- 支持三种来源：本地目录、ClawHub API、直接 URL
- 通过环境变量 `AGENT_SKILLS` 声明式配置 Skill 组合
- 使用 Agent Framework (ChatAgent) 构建，部署到 Azure AI Foundry

## Tech Stack
- Python 3.12
- `azure-ai-agentserver-agentframework==1.0.0b10`
- `python-frontmatter>=1.1.0` (SKILL.md 解析)
- `httpx>=0.27.0` (ClawHub/URL 下载)
- Docker + Azure AI Foundry Hosted Agent

## Success Criteria
- Agent 能从 `skills/` 目录加载内置 SKILL.md
- Agent 能从 ClawHub API 下载并加载外部 Skill
- 修改 `AGENT_SKILLS` 环境变量即可切换 Skill 组合（无需重建镜像）
- 代理响应能体现已加载 Skill 的知识/行为
