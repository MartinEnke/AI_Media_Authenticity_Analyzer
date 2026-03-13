import sys
import os

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from mcp.server.fastmcp import FastMCP

from tools.security_tools import security_scan_tool
from tools.image_tools import (
    extract_metadata_tool,
    compute_edge_density_tool,
    detect_image_structure_flags_tool,
)

mcp = FastMCP("media-auth-tools")


@mcp.tool()
def security_scan(file_path: str, declared_mimetype: str, media_type: str) -> dict:
    return security_scan_tool(
        file_path=file_path,
        declared_mimetype=declared_mimetype,
        media_type=media_type,
    )


@mcp.tool()
def extract_metadata(file_path: str) -> dict:
    return extract_metadata_tool(file_path)


@mcp.tool()
def compute_edge_density(file_path: str) -> dict:
    return compute_edge_density_tool(file_path)


@mcp.tool()
def detect_image_structure_flags(metadata: dict, edge_density: float) -> dict:
    return detect_image_structure_flags_tool(
        metadata=metadata,
        edge_density=edge_density,
    )


if __name__ == "__main__":
    mcp.run()