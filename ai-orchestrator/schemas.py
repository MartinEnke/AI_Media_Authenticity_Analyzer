from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    request_id: str
    file_path: str
    filename: str
    media_type: str
    mimetype: str
    claim: Optional[str] = None


class AnalysisResponse(BaseModel):
    request_id: str
    media_type: str
    risk_score: float
    risk_level: str
    flags: List[str]
    summary: str
    reasoning: str
    confidence_explanation: str
    recommended_action: str
    technical_details: Optional[Dict[str, Any]] = None