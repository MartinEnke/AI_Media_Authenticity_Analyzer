import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_PATH = BASE_DIR / "evaluation" / "results.json"
REPORT_PATH = BASE_DIR / "evaluation" / "report.md"


def load_results():
    with open(RESULTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_by_mode(results):
    grouped = {}

    for item in results:
        if not item:
            continue
        mode = item.get("reasoning_mode", "unknown")
        grouped.setdefault(mode, []).append(item)

    summaries = {}

    for mode, items in grouped.items():
        valid_items = [x for x in items if "error" not in x]
        error_items = [x for x in items if "error" in x]

        if valid_items:
            avg_latency = round(sum(x["latency_ms"] for x in valid_items) / len(valid_items), 2)
            avg_score = round(sum(x["authenticity_score"] for x in valid_items) / len(valid_items), 2)
            summary_present_rate = round(sum(1 for x in valid_items if x["summary_present"]) / len(valid_items), 2)
            reasoning_present_rate = round(sum(1 for x in valid_items if x["reasoning_present"]) / len(valid_items), 2)
            confidence_present_rate = round(sum(1 for x in valid_items if x["confidence_present"]) / len(valid_items), 2)
            fallback_rate = round(sum(1 for x in valid_items if x.get("fallback_used")) / len(valid_items), 2)
            avg_reasoning_length = round(sum(x["reasoning_length"] for x in valid_items) / len(valid_items), 2)
            avg_confidence_length = round(sum(x["confidence_length"] for x in valid_items) / len(valid_items), 2)
            expected_flag_pass_rate = round(
                sum(1 for x in valid_items if x.get("expected_min_flags_passed")) / len(valid_items), 2
            )
            risk_accuracy = round(
                sum(1 for x in valid_items if x.get("risk_correct")) / len(valid_items), 2
            )
        else:
            avg_latency = None
            avg_score = None
            summary_present_rate = 0
            reasoning_present_rate = 0
            confidence_present_rate = 0
            fallback_rate = 0
            avg_reasoning_length = 0
            avg_confidence_length = 0
            expected_flag_pass_rate = 0
            risk_accuracy = 0

        summaries[mode] = {
            "total_cases": len(items),
            "successful_cases": len(valid_items),
            "failed_cases": len(error_items),
            "avg_latency_ms": avg_latency,
            "avg_authenticity_score": avg_score,
            "summary_present_rate": summary_present_rate,
            "reasoning_present_rate": reasoning_present_rate,
            "confidence_present_rate": confidence_present_rate,
            "fallback_rate": fallback_rate,
            "avg_reasoning_length": avg_reasoning_length,
            "avg_confidence_length": avg_confidence_length,
            "expected_flag_pass_rate": expected_flag_pass_rate,
            "risk_accuracy": risk_accuracy,
        }

    return summaries


def build_report(results, summaries):
    lines = []
    lines.append("# Evaluation Report\n")
    lines.append("## Overview\n")

    for mode, summary in summaries.items():
        lines.append(f"### Mode: {mode}\n")
        lines.append(f"- Total cases: {summary['total_cases']}")
        lines.append(f"- Successful cases: {summary['successful_cases']}")
        lines.append(f"- Failed cases: {summary['failed_cases']}")
        lines.append(f"- Average latency (ms): {summary['avg_latency_ms']}")
        lines.append(f"- Average authenticity score: {summary['avg_authenticity_score']}")
        lines.append(f"- Summary present rate: {summary['summary_present_rate']}")
        lines.append(f"- Reasoning present rate: {summary['reasoning_present_rate']}")
        lines.append(f"- Confidence present rate: {summary['confidence_present_rate']}")
        lines.append(f"- Fallback rate: {summary['fallback_rate']}")
        lines.append(f"- Average reasoning length: {summary['avg_reasoning_length']}")
        lines.append(f"- Average confidence length: {summary['avg_confidence_length']}")
        lines.append(f"- Expected flag pass rate: {summary['expected_flag_pass_rate']}\n")

    lines.append("## Per-case Results\n")

    for item in results:
        if not item:
            continue
        lines.append(f"### {item.get('case_id')} | mode={item.get('reasoning_mode')}\n")
        if "error" in item:
            lines.append(f"- Error: {item['error']}\n")
            continue

        lines.append(f"- Latency (ms): {item['latency_ms']}")
        lines.append(f"- Authenticity score: {item['authenticity_score']}")
        lines.append(f"- Risk level: {item['risk_level']}")
        lines.append(f"- Recommended action: {item['recommended_action']}")
        lines.append(f"- Flags: {', '.join(item['flags'])}")
        lines.append(f"- Fallback used: {item['fallback_used']}")
        lines.append(f"- Reasoning length: {item['reasoning_length']}")
        lines.append(f"- Confidence length: {item['confidence_length']}")
        lines.append(f"- Expected min flags passed: {item['expected_min_flags_passed']}")
        lines.append(f"- Summary: {item['summary']}")
        lines.append(f"- Reasoning: {item['reasoning']}")
        lines.append(f"- Confidence: {item['confidence_explanation']}\n")
        lines.append(f"- Label: {item['label']}")
        lines.append(f"- Expected risk: {item['expected_risk']}")
        lines.append(f"- Predicted risk: {item['predicted_risk']}")
        lines.append(f"- Risk correct: {item['risk_correct']}")

    return "\n".join(lines)


def main():
    results = load_results()
    summaries = summarize_by_mode(results)
    report = build_report(results, summaries)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Saved report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()