ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example. Run: "cp .env.example .env" and fill in the missing values.)
endif

include .env
export

export UV_PROJECT_ENVIRONMENT=.venv
export PYTHONPATH = ./src/

# --- Default Values ---

QA_FOLDERS := src/ scripts/
TEST_SLUG := im-currently-designing-a-second-brain-ai-agent
DATASET_DIR := datasets/linkedin_paul_iusztin

# --- QA ---

format-fix: # Auto-format Python code using ruff formatter.
	uv run ruff format $(QA_FOLDERS)

lint-fix: # Auto-fix linting issues using ruff linter.
	uv run ruff check --fix $(QA_FOLDERS)

format-check: # Check code formatting without making changes using ruff formatter.
	uv run ruff format --check $(QA_FOLDERS) 

lint-check: # Check code for linting issues without fixing them using ruff linter.
	uv run ruff check $(QA_FOLDERS)

# --- Run ---

run-research-server: # Run the Deep Research MCP server (stdio transport).
	uv run fastmcp run src/research/server.py

run-writing-server: # Run the LinkedIn Writer MCP server (stdio transport).
	uv run fastmcp run src/writing/server.py

test-research-workflow: # Test the research workflow using the dataset seed.
	@mkdir -p test_logic
	@cp $(DATASET_DIR)/$(TEST_SLUG)_seed.md test_logic/seed.md
	uv run python scripts/test_research_workflow.py --working-dir test_logic --iterations 2