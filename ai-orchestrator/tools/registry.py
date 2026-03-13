from tools.security_tools import security_scan_tool
from tools.image_tools import (
    extract_metadata_tool,
    compute_edge_density_tool,
    detect_image_structure_flags_tool,
)

TOOL_REGISTRY = {
    "security_scan": security_scan_tool,
    "extract_metadata": extract_metadata_tool,
    "compute_edge_density": compute_edge_density_tool,
    "detect_image_structure_flags": detect_image_structure_flags_tool,
}