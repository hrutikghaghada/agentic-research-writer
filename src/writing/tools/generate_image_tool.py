"""LinkedIn post image generation tool."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


async def generate_image_tool(working_dir: str) -> dict[str, Any]:
    """Generate a LinkedIn post image using Gemini Flash Image.

    Reads the existing post.md and generates a professional image
    following the branding and character profiles, using dataset media
    as style reference images.

    Args:
        working_dir: Path to the working directory with post.md.

    Returns:
        Dict with status, image path, and message.
    """

    return {
        "status": "not_implemented",
        "tool": "generate_image_tool",
        "working_dir": working_dir,
        "message": "Shell only — implementation lands in task #015.",
    }
