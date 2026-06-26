"""Gemini grounded research tool implementation."""

from typing import Any


async def deep_research_tool(working_dir: str, query: str) -> dict[str, Any]:
    return {
        "status": "not_implemented",
        "tool": "deep_research_tool",
        "working_dir": working_dir,
        "message": "Shell only — implementation lands in task #004.",
    }
