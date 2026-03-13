import asyncio
import json
import os
from contextlib import asynccontextmanager
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


BASE_DIR = os.path.dirname(__file__)

SERVER_PARAMS = StdioServerParameters(
    command=os.path.join(BASE_DIR, ".venv", "bin", "python"),
    args=[os.path.join(BASE_DIR, "mcp_server", "server.py")],
)


@asynccontextmanager
async def get_mcp_session():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session


def _extract_json_from_tool_result(result: Any) -> dict:
    """
    Normalize MCP tool results into a plain Python dict.

    Depending on SDK version, tool responses may come back wrapped in
    content blocks. We try a few safe patterns and fall back clearly.
    """
    # Case 1: already a plain dict
    if isinstance(result, dict):
        return result

    # Case 2: SDK result object with content blocks
    content = getattr(result, "content", None)
    if content:
        first = content[0]

        # Text content block
        text = getattr(first, "text", None)
        if text:
            return json.loads(text)

    raise ValueError(f"Unsupported MCP tool result format: {type(result)}")


async def call_tool(tool_name: str, arguments: dict) -> dict:
    async with get_mcp_session() as session:
        result = await session.call_tool(tool_name, arguments)
        return _extract_json_from_tool_result(result)


def call_tool_sync(tool_name: str, arguments: dict) -> dict:
    """
    Synchronous wrapper so the current LangGraph nodes can use MCP tools
    without becoming async yet.
    """
    return asyncio.run(call_tool(tool_name, arguments))