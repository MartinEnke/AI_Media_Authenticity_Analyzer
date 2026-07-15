import json
import sys

from graph import build_graph
from schemas import AnalysisRequest, AnalysisResponse


def main() -> None:
    raw_input = sys.stdin.read()
    data = json.loads(raw_input)

    request = AnalysisRequest(**data)

    app = build_graph()

    result = app.invoke(
        {
            "request_id": request.request_id,
            "file_path": request.file_path,
            "filename": request.filename,
            "media_type": request.media_type,
            "mimetype": request.mimetype,
            "claim": request.claim,
            "flags": [],
            "mcp_tool_trace": [],
            "reasoning_mode": data.get("reasoning_mode", "llm"),
            "prompt_version": data.get("prompt_version", "v2"),
        }
    )

    technical_details = {
        "security": result.get("security_result", {}),
        "analysis": result.get("analysis_result", {}),
        "claim": result.get("claim"),
        "mcp_tool_trace": result.get("mcp_tool_trace", []),
        "prompt_preview": result.get("prompt_preview", {}),
    }

    response = AnalysisResponse(
        request_id=result["request_id"],
        media_type=result["media_type"],
        risk_score=result["risk_score"],
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