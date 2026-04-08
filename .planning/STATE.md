# Project State

## Current Position
- **Milestone:** v1 — Skillable Agent MVP
- **Phase:** 01-skillable-agent (PLANNING)
- **Status:** Planning phase, no implementation started

## Decisions
- D-01: 使用 Agent Framework (ChatAgent)，不用 LangGraph
- D-02: Skill = SKILL.md prompt 扩展（不是 function tool）
- D-03: 使用 `python-frontmatter` 解析 YAML frontmatter
- D-04: 使用 `httpx` 做 HTTP 下载
- D-05: 通过 `AGENT_SKILLS` 环境变量声明式配置
- D-06: 兼容 OpenClaw/ClawHub SKILL.md 标准格式

## Blockers
None

## Pending Todos
None
