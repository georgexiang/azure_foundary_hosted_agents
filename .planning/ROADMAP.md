# Roadmap — v1 Skillable Agent MVP

## Milestone: v1 — Skillable Agent

**Goal:** 构建可安装外部标准 Skill 的 Agent Framework 代理，部署到 Azure AI Foundry

**Requirements:**
- SKILL-01: 解析 SKILL.md 格式（YAML frontmatter + Markdown body）
- SKILL-02: 从本地目录加载 Skill
- SKILL-03: 从 ClawHub API 下载并加载 Skill
- SKILL-04: 从直接 URL 下载并加载 Skill
- SKILL-05: 组合多个 Skill 到 agent instructions，支持 token 统计
- SKILL-06: 通过环境变量 AGENT_SKILLS 声明式配置 Skill 列表
- SKILL-07: 使用 Agent Framework ChatAgent 集成
- SKILL-08: Azure AI Foundry 部署就绪（agent.yaml, Dockerfile, requirements.txt）

---

### Phase 01: skillable-agent

**Goal:** 完整实现 agent-with-skills 子项目（Skill 解析 + 加载 + Agent 集成 + 部署配置）
**Requirements:** [SKILL-01, SKILL-02, SKILL-03, SKILL-04, SKILL-05, SKILL-06, SKILL-07, SKILL-08]
**Plans:** 2 plans

Plans:
- [ ] 01-01-PLAN.md — Skill Manager 核心实现 + 示例 Skill 文件
- [ ] 01-02-PLAN.md — Agent 入口集成 + 部署配置 + 文档
