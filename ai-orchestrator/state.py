from typing import Any, Dict, List, TypedDict


class GraphState(TypedDict, total=False):
    request_id: str
    file_path: str
    filename: str
    media_type: str
    mimetype: str
    claim: str

    prompt_version: str
    reasoning_mode: str

    security_result: Dict[str, Any]
    analysis_result: Dict[str, Any]

    flags: List[str]
    mcp_tool_trace: List[Dict[str, Any]]

    reasoning: str
    confidence_explanation: str
    summary: str

    risk_score: float
    risk_level: str
    recommended_action: str

    prompt_preview: Dict[str, Any]