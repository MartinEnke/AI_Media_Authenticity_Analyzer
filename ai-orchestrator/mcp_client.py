import asyncio
import json
import os
import sys
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Tuple

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MCP_SERVER_PATH = os.path.join(BASE_DIR, "mcp_server", "server.py")

SERVER_PARAMS = StdioServerParameters(
    command=sys.executable,
    args=[MCP_SERVER_PATH],
)


@asynccontextmanager
async def get_mcp_session():
    """
    Start the local MCP server through stdio and provide an initialized
    MCP client session.
    """
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session


def _extract_json_from_tool_result(result: Any) -> Dict[str, Any]:
    """
    Normalize an MCP tool response into a plain Python dictionary.
    """
    if isinstance(result, dict):
        return result

    structured_content = getattr(result, "structuredContent", None)
    if isinstance(structured_content, dict):
        return structured_content

    structured_content = getattr(result, "structured_content", None)
    if isinstance(structured_content, dict):
        return structured_content

    content = getattr(result, "content", None)

    if content:
        for block in content:
            text = getattr(block, "text", None)

            if not text:
                continue

            try:
                parsed = json.loads(text)
            except json.JSONDecodeError:
                continue

            if isinstance(parsed, dict):
                return parsed

    raise ValueError(
        f"Unsupported MCP tool-result format: {type(result).__name__}"
    )


async def _call_tool(
    session: ClientSession,
    tool_name: str,
    arguments: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Call a registered MCP tool and normalize its response.
    """
    result = await session.call_tool(tool_name, arguments)

    is_error = getattr(result, "isError", False) or getattr(
        result,
        "is_error",
        False,
    )

    if is_error:
        raise RuntimeError(f"MCP tool '{tool_name}' returned an error.")

    return _extract_json_from_tool_result(result)


async def security_scan_via_mcp_async(
    file_path: str,
    declared_mimetype: str,
    media_type: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Execute the security scan through the MCP server.
    """
    async with get_mcp_session() as session:
        result = await _call_tool(
            session=session,
            tool_name="security_scan",
            arguments={
                "file_path": file_path,
                "declared_mimetype": declared_mimetype,
                "media_type": media_type,
            },
        )

    trace = [
        {
            "tool": "security_scan",
            "transport": "mcp_stdio",
            "status": "completed",
        }
    ]

    return result, trace


async def analyze_image_via_mcp_async(
    file_path: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Compose the image-analysis pipeline from individual MCP tools.

    The orchestrator controls the sequence, while the MCP server owns
    access to the analysis capabilities.
    """
    trace: List[Dict[str, Any]] = []

    async with get_mcp_session() as session:
        metadata = await _call_tool(
            session=session,
            tool_name="extract_metadata",
            arguments={"file_path": file_path},
        )

        trace.append(
            {
                "tool": "extract_metadata",
                "transport": "mcp_stdio",
                "status": "completed",
            }
        )

        edge_result = await _call_tool(
            session=session,
            tool_name="compute_edge_density",
            arguments={"file_path": file_path},
        )

        trace.append(
            {
                "tool": "compute_edge_density",
                "transport": "mcp_stdio",
                "status": "completed",
            }
        )

        edge_density = float(edge_result.get("edge_density", 0.0))

        noise_result = await _call_tool(
            session=session,
            tool_name="detect_noise_consistency",
            arguments={"file_path": file_path},
        )

        trace.append(
            {
                "tool": "detect_noise_consistency",
                "transport": "mcp_stdio",
                "status": "completed",
            }
        )

        structure_result = await _call_tool(
            session=session,
            tool_name="detect_image_structure_flags",
            arguments={
                "metadata": metadata,
                "edge_density": edge_density,
                "noise_analysis": noise_result,
            },
        )

        trace.append(
            {
                "tool": "detect_image_structure_flags",
                "transport": "mcp_stdio",
                "status": "completed",
            }
        )

    analysis_result = {
        **metadata,
        **structure_result,
        "edge_density": edge_density,
        "noise_analysis": noise_result,
    }

    return analysis_result, trace


def security_scan_via_mcp(
    file_path: str,
    declared_mimetype: str,
    media_type: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Synchronous entry point for the current synchronous LangGraph nodes.
    """
    return asyncio.run(
        security_scan_via_mcp_async(
            file_path=file_path,
            declared_mimetype=declared_mimetype,
            media_type=media_type,
        )
    )


def analyze_image_via_mcp(
    file_path: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Synchronous entry point for image analysis.
    """
    return asyncio.run(analyze_image_via_mcp_async(file_path))

