"""MCP Tools registration for research operations."""

from typing import Any

from fastmcp import FastMCP

from research.tools.analyze_youtube_video_tool import analyze_youtube_video_tool
from research.tools.compile_research_tool import compile_research_tool
from research.tools.deep_research_tool import deep_research_tool


def register_mcp_tools(mcp: FastMCP) -> None:
    """Register all MCP tools with the server instance."""

    # ========================================================================
    # DEEP RESEARCH
    # ========================================================================

    @mcp.tool()
    async def deep_research(working_dir: str, query: str) -> dict[str, Any]:
        """Research a topic using Gemini with Google Search grounding.

        Takes a topic or query, calls Gemini's grounded search API, and returns
        structured research findings with sources.

        Args:
            working_dir: Path to the working directory.
            query: The research topic or question to investigate.
        """

        return await deep_research_tool(working_dir, query)

    # ========================================================================
    # YOUTUBE VIDEO ANALYSIS
    # ========================================================================

    @mcp.tool()
    async def analyze_youtube_video(
        working_dir: str, youtube_url: str
    ) -> dict[str, Any]:
        """Analyze a YouTube video using Gemini's native video understanding.

        Takes a YouTube URL, passes it to Gemini using FileData(file_uri=url)
        for native video understanding, and returns a structured transcript
        with key insights.

        Args:
            working_dir: Path to the working directory.
            youtube_url: The YouTube video URL to analyze.
        """

        return await analyze_youtube_video_tool(working_dir, youtube_url)

    # ========================================================================
    # COMPILE RESEARCH
    # ========================================================================

    @mcp.tool()
    async def compile_research(working_dir: str) -> dict[str, Any]:
        """Aggregate all collected research into a single markdown research brief.

        Combines all research results and YouTube transcripts from .memory/
        into a structured research.md file.

        Args:
            working_dir: Path to the working directory containing .memory/ data.
        """

        return compile_research_tool(working_dir)
