"""Constants used throughout the MCP server."""

# File names
RESEARCH_MD_FILE = "research.md"
RESEARCH_RESULTS_FILE = "research_results.json"
EXPLORATION_STATE_FILE = "exploration_state.json"

# Folder names
MEMORY_FOLDER = ".memory"
TRANSCRIPTS_FOLDER = "transcripts"

# Exploration budget — caps how many `deep_research` / `analyze_youtube_video`
# calls the agent can make in one research session before it must call
# `compile_research`. 6 calls roughly matches "3 rounds × 2 queries"
# enough room for breadth-first exploration without runaway, and
# small enough that the agent has to plan up front.
MAX_EXPLORATION_CALLS = 6
