from typing import TypedDict, Dict, Any, List


class GraphState(TypedDict, total=False):
    request_id: str
    file_path: str
    filename: str
    media_type: str
    mimetype: str
    claim: str

    security_result: Dict[str, Any]
    analysis_result: Dict[str, Any]

    flags: List[str]
    reasoning: str
    confidence_explanation: str
    authenticity_score: float
    risk_level: str
    recommended_action: str
    summary: str