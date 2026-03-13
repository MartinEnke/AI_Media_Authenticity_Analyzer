import sys
import json
from schemas import AnalysisRequest, AnalysisResponse
from graph import build_graph


def main():
    raw_input = sys.stdin.read()
    data = json.loads(raw_input)

    request = AnalysisRequest(**data)

    app = build_graph()
    result = app.invoke({
        "request_id": request.request_id,
        "file_path": request.file_path,
        "filename": request.filename,
        "media_type": request.media_type,
        "mimetype": request.mimetype,
        "claim": request.claim,
        "flags": [],
        "reasoning_mode": data.get("reasoning_mode", "llm"),
    })

    technical_details = {
        "security": result.get("security_result", {}),
        "analysis": result.get("analysis_result", {}),
        "claim": result.get("claim"),
    }

    response = AnalysisResponse(
        request_id=result["request_id"],
        media_type=result["media_type"],
        authenticity_score=result["authenticity_score"],
        risk_level=result["risk_level"],
        flags=result.get("flags", []),
        summary=result["summary"],
        reasoning=result.get("reasoning", ""),
        confidence_explanation=result.get("confidence_explanation", ""),
        recommended_action=result["recommended_action"],
        technical_details=technical_details,
    )

    print(response.model_dump_json())


if __name__ == "__main__":
    main()