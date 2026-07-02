"""Main MCP server implementation for the LinkedIn Writer."""

import logging

from fastmcp import FastMCP

from writing.config.settings import get_settings
from writing.routers.tools import register_mcp_tools
from writing.utils.logging import setup_logging

logger = logging.getLogger(__name__)


def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server instance.

    Returns:
        FastMCP: Configured MCP server instance.
    """

    settings = get_settings()

    mcp = FastMCP(
        name=settings.server_name,
        version=settings.version,
    )

    register_mcp_tools(mcp)

    return mcp


# Configure logging
setup_logging(level=get_settings().log_level)


# Create the server instance (used by `fastmcp run`)
mcp = create_mcp_server()

if __name__ == "__main__":
    mcp.run()
