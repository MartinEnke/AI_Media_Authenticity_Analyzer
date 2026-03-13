from typing import Dict, Any
from tools.registry import TOOL_REGISTRY


def analyze_image(file_path: str) -> Dict[str, Any]:
    metadata = TOOL_REGISTRY["extract_metadata"](file_path)
    edge_result = TOOL_REGISTRY["compute_edge_density"](file_path)
    structure_result = TOOL_REGISTRY["detect_image_structure_flags"](
        metadata=metadata,
        edge_density=edge_result["edge_density"],
    )

    return {
        **metadata,
        **edge_result,
        **structure_result,
    }