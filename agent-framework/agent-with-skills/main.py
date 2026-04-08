"""
Skillable Agent — An AI agent that supports installing and composing
external standard skills (agentskills.io specification).

Skills are loaded at startup based on the AGENT_SKILLS environment variable.
Supports: local directory, git repo, ClawHub marketplace, and direct URL.
"""

import logging
import os

from skill_manager import SkillManager

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    # 1. Validate required environment variables
    required_env_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME",
    ]
    for env_var in required_env_vars:
        assert env_var in os.environ and os.environ[env_var], (
            f"{env_var} environment variable must be set."
        )

    # 2. Read skill configuration
    agent_skills_env = os.environ.get("AGENT_SKILLS", "")
    base_instructions = os.environ.get(
        "AGENT_BASE_INSTRUCTIONS",
        "You are a helpful assistant enhanced with specialized skills.",
    )
    max_skill_tokens = int(os.environ.get("AGENT_MAX_SKILL_TOKENS", "4000"))

    # 3. Load skills
    sm = SkillManager()

    if agent_skills_env:
        skill_specs = [s.strip() for s in agent_skills_env.split(",") if s.strip()]
        logger.info("Loading skills from AGENT_SKILLS: %s", skill_specs)
        skills = sm.load_skills(skill_specs)
    else:
        # Default: load all built-in skills from skills/ directory
        skills_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills")
        if os.path.isdir(skills_dir):
            logger.info("Loading built-in skills from %s", skills_dir)
            skills = sm.load_from_directory(skills_dir)
        else:
            skills = []

    logger.info(
        "Loaded %d skill(s): %s",
        len(skills),
        ", ".join(s.name for s in skills) if skills else "(none)",
    )

    # 4. Compose instructions
    instructions = sm.compose_instructions(
        base_instructions, skills, max_tokens=max_skill_tokens
    )

    # 5. Optional Foundry tools (web_search, MCP)
    tools = []
    if os.environ.get("ENABLE_WEB_SEARCH", "").lower() == "true":
        tools.append({"type": "web_search_preview"})
    if conn_id := os.environ.get("AZURE_AI_PROJECT_TOOL_CONNECTION_ID"):
        tools.append({"type": "mcp", "project_connection_id": conn_id})

    # 6. Create Agent  (imports deferred to avoid early init failures)
    from agent_framework.azure import AzureOpenAIChatClient
    from azure.ai.agentserver.agentframework import (
        FoundryToolsChatMiddleware,
        from_agent_framework,
    )
    from azure.identity import DefaultAzureCredential

    middleware = FoundryToolsChatMiddleware(tools) if tools else None
    chat_client = AzureOpenAIChatClient(
        credential=DefaultAzureCredential(),
        middleware=middleware,
    )
    agent = chat_client.create_agent(
        name="SkillableAgent",
        instructions=instructions,
    )

    # 7. Start HTTP service
    logger.info("Starting SkillableAgent on http://localhost:8088")
    from_agent_framework(agent).run()


if __name__ == "__main__":
    main()
