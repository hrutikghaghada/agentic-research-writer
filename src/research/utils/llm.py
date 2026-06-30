"""Gemini client helpers for LLM interactions."""

import logging
from functools import lru_cache
from typing import Any

from google import genai
from google.genai import types
from pydantic import BaseModel

from research.config.settings import get_settings

logger = logging.getLogger(__name__)


# Singleton pattern: lru_cache ensures only one Gemini client is created
# across the entire application lifetime.
@lru_cache
def get_client() -> genai.Client:
    """Create and cache a Gemini client, with Opik tracking if configured."""

    settings = get_settings()
    # Initialize the Gemini client with the API key from settings.
    # get_secret_value() unwraps the Pydantic SecretStr to a plain string.
    client = genai.Client(api_key=settings.google_api_key.get_secret_value())

    # Wrap the client with Opik observability tracking (if configured),
    # so all LLM calls are automatically logged for monitoring/evals.
    return client


async def call_gemini(
    prompt: str,
    model: str | None = None,
    response_schema: type[BaseModel] | None = None,
    system_instruction: str | None = None,
) -> str:
    """Call Gemini with optional structured output.

    Args:
        prompt: The prompt to send to Gemini.
        model: Model name override. Defaults to settings.gemini_model.
        response_schema: If provided, Gemini returns JSON matching this Pydantic model.
        system_instruction: Optional system instruction for the model.

    Returns:
        The response text from Gemini.
    """

    settings = get_settings()
    client = get_client()
    # Use the provided model or fall back to the default from settings
    model_name = model or settings.gemini_model

    # Build config kwargs dynamically based on which options are provided
    config_kwargs: dict[str, Any] = {}
    if response_schema is not None:
        # When a Pydantic schema is given, tell Gemini to return structured JSON
        # that conforms to the schema (instead of free-form text)
        config_kwargs["response_mime_type"] = "application/json"
        config_kwargs["response_schema"] = response_schema
    if system_instruction is not None:
        config_kwargs["system_instruction"] = system_instruction

    # Only create a config object if we have options to set; otherwise pass None
    config = types.GenerateContentConfig(**config_kwargs) if config_kwargs else None

    # Make the async API call to Gemini via the google-genai SDK.
    # client.aio provides the async interface for non-blocking calls.
    response = await client.aio.models.generate_content(
        model=model_name,
        contents=prompt,
        config=config,
    )

    return response.text
