import json
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from graph import build_graph

import argparse


DEFAULT_CASES_PATH = BASE_DIR / "evaluation" / "cases" / "image_cases.json"
RESULTS_PATH = BASE_DIR / "evaluation" / "results.json"


def load_cases(cases_path):
    with open(cases_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def resolve_case_path(path_str: str) -> str:
    return str((BASE_DIR / path_str).resolve())


def run_case(app, case, reasoning_mode):
    start = time.perf_counter()

    result = app.invoke({
    "request_id": case["id"],
    "file_path": resolve_case_path(case["file_path"]),
    "filename": case["filename"],
    "media_type": case["media_type"],
    "mimetype": case["mimetype"],
    "claim": case.get("claim"),
    "flags": [],
    "reasoning_mode": reasoning_mode,
    "prompt_version": case.get("prompt_version", "v1"),
})

    latency_ms = round((time.perf_counter() - start) * 1000, 2)

    confidence_text = result.get("confidence_explanation", "")
    reasoning_text = result.get("reasoning", "")
    flags = result.get("flags", [])

    fallback_used = "fallback" in confidence_text.lower()
    expected_min_flags = case.get("expected_min_flags", 0)

    expected_risk = case.get("expected_risk")
    predicted_risk = result.get("risk_level")
    risk_correct = expected_risk == predicted_risk

    output = {
        "case_id": case["id"],
        "reasoning_mode": reasoning_mode,
        "latency_ms": latency_ms,
        "flag_count": len(flags),
        "expected_min_flags": expected_min_flags,
        "expected_min_flags_passed": len(flags) >= expected_min_flags,
        "summary_present": bool(result.get("summary")),
        "reasoning_present": bool(reasoning_text),
        "confidence_present": bool(confidence_text),
        "fallback_used": fallback_used,
        "reasoning_length": len(reasoning_text),
        "confidence_length": len(confidence_text),
        "recommended_action": result.get("recommended_action"),
        "risk_level": result.get("risk_level"),
        "authenticity_score": result.get("authenticity_score"),
        "flags": flags,
        "summary": result.get("summary", ""),
        "reasoning": reasoning_text,
        "confidence_explanation": confidence_text,
        "label": case.get("label"),
        "expected_risk": expected_risk,
        "predicted_risk": predicted_risk,
        "risk_correct": risk_correct,
        "prompt_version": case.get("prompt_version", "v1"),
    }

    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases",
        default=str(DEFAULT_CASES_PATH),
        help="Path to the evaluation cases JSON file"
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    app = build_graph()

    all_results = []

    for case in cases:
        for mode in ["rule", "llm"]:
            try:
                result = run_case(app, case, mode)
                all_results.append(result)
                print(f"Finished {case['id']} with mode={mode}")
            except Exception as e:
                all_results.append({
                    "case_id": case["id"],
                    "reasoning_mode": mode,
                    "error": str(e),
                })
                print(f"Failed {case['id']} with mode={mode}: {e}")

    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nSaved results to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()