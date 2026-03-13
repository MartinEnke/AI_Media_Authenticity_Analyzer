from typing import Dict, Any
from utils.security_checks import validate_basic_file_properties


def security_scan_tool(file_path: str, declared_mimetype: str, media_type: str) -> Dict[str, Any]:
    """
    MCP-style security tool wrapper.
    """
    return validate_basic_file_properties(
        file_path=file_path,
        declared_mimetype=declared_mimetype,
        media_type=media_type,
    )