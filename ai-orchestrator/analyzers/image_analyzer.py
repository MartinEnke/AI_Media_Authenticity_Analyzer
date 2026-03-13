from mcp_client import call_tool_sync


def analyze_image(file_path: str) -> dict:
    metadata = call_tool_sync("extract_metadata", {"file_path": file_path})
    edge_result = call_tool_sync("compute_edge_density", {"file_path": file_path})
    structure_result = call_tool_sync(
        "detect_image_structure_flags",
        {
            "metadata": metadata,
            "edge_density": edge_result["edge_density"],
        },
    )

    return {
        **metadata,
        **edge_result,
        **structure_result,
    }