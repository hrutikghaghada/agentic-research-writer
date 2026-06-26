"""YouTube video analysis tool implementation."""

from typing import Any


async def analyze_youtube_video_tool(working_dir: str, query: str) -> dict[str, Any]:
    return {
        "status": "not_implemented",
        "tool": "analyze_youtube_video_tool",
        "working_dir": working_dir,
        "message": "Shell only — implementation lands in task #003.",
    }
