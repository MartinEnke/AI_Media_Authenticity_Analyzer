from pydantic import BaseModel
from typing import List, Optional, Dict, Any


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
    authenticity_score: float
    risk_level: str
    flags: List[str]
    summary: str
    reasoning: str
    confidence_explanation: str
    recommended_action: str
    technical_details: Optional[Dict[str, Any]] = None