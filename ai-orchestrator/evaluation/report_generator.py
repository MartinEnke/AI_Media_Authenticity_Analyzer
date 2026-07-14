import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_PATH = BASE_DIR / "evaluation" / "results.json"
REPORT_PATH = BASE_DIR / "evaluation" / "report.md"


def load_results():
    with open(RESULTS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def summarize_by_mode(results):
    grouped = {}

    for item in results:
        if not item:
            continue

        mode = item.get("reasoning_mode", "unknown")
        grouped.setdefault(mode, []).append(item)

    summaries = {}

    for mode, items in grouped.items():
        valid_items = [item for item in items if "error" not in item]
        error_items = [item for item in items if "error" in item]

        if valid_items:
            avg_latency = round(
                sum(item["latency_ms"] for item in valid_items)
                / len(valid_items),
                2,
            )
            avg_score = round(
                sum(item["risk_score"] for item in valid_items)
                / len(valid_items),
                2,
            )
            summary_present_rate = round(
                sum(1 for item in valid_items if item["summary_present"])
                / len(valid_items),
                2,
            )
            reasoning_present_rate = round(
                sum(1 for item in valid_items if item["reasoning_present"])
                / len(valid_items),
                2,
            )
            confidence_present_rate = round(
                sum(1 for item in valid_items if item["confidence_present"])
                / len(valid_items),
                2,
            )
            fallback_rate = round(
                sum(1 for item in valid_items if item.get("fallback_used"))
                / len(valid_items),
                2,
            )
            avg_reasoning_length = round(
                sum(item["reasoning_length"] for item in valid_items)
                / len(valid_items),
                2,
            )
            avg_confidence_length = round(
                sum(item["confidence_length"] for item in valid_items)
                / len(valid_items),
                2,
            )
            expected_flag_pass_rate = round(
                sum(
                    1
                    for item in valid_items
                    if item.get("expected_min_flags_passed")
                )
                / len(valid_items),
                2,
            )
            risk_accuracy = round(
                sum(1 for item in valid_items if item.get("risk_correct"))
                / len(valid_items),
                2,
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
            "avg_risk_score": avg_score,
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
    lines = [
        "# Evaluation Report\n",
        "## Overview\n",
    ]

    for mode, summary in summaries.items():
        lines.append(f"### Mode: {mode}\n")
        lines.append(f"- Total cases: {summary['total_cases']}")
        lines.append(f"- Successful cases: {summary['successful_cases']}")
        lines.append(f"- Failed cases: {summary['failed_cases']}")
        lines.append(f"- Average latency (ms): {summary['avg_latency_ms']}")
        lines.append(f"- Average risk score: {summary['avg_risk_score']}")
        lines.append(
            f"- Summary present rate: {summary['summary_present_rate']}"
        )
        lines.append(
            f"- Reasoning present rate: "
            f"{summary['reasoning_present_rate']}"
        )
        lines.append(
            f"- Confidence present rate: "
            f"{summary['confidence_present_rate']}"
        )
        lines.append(f"- Fallback rate: {summary['fallback_rate']}")
        lines.append(
            f"- Average reasoning length: "
            f"{summary['avg_reasoning_length']}"
        )
        lines.append(
            f"- Average confidence length: "
            f"{summary['avg_confidence_length']}"
        )
        lines.append(
            f"- Expected flag pass rate: "
            f"{summary['expected_flag_pass_rate']}"
        )
        lines.append(f"- Risk accuracy: {summary['risk_accuracy']}\n")

    lines.append("## Per-case Results\n")

    for item in results:
        if not item:
            continue

        lines.append(
            f"### {item.get('case_id')} | "
            f"mode={item.get('reasoning_mode')} | "
            f"prompt={item.get('prompt_version', 'v1')}\n"
        )

        if "error" in item:
            lines.append(f"- Error: {item['error']}\n")
            continue

        lines.append(f"- Latency (ms): {item['latency_ms']}")
        lines.append(f"- Risk score: {item['risk_score']}")
        lines.append(f"- Risk level: {item['risk_level']}")
        lines.append(
            f"- Recommended action: {item['recommended_action']}"
        )
        lines.append(f"- Flags: {', '.join(item['flags'])}")
        lines.append(f"- Fallback used: {item['fallback_used']}")
        lines.append(f"- Reasoning length: {item['reasoning_length']}")
        lines.append(
            f"- Confidence length: {item['confidence_length']}"
        )
        lines.append(
            f"- Expected min flags passed: "
            f"{item['expected_min_flags_passed']}"
        )
        lines.append(f"- Summary: {item['summary']}")
        lines.append(f"- Reasoning: {item['reasoning']}")
        lines.append(
            f"- Confidence: {item['confidence_explanation']}\n"
        )
        lines.append(f"- Label: {item['label']}")
        lines.append(f"- Expected risk: {item['expected_risk']}")
        lines.append(f"- Predicted risk: {item['predicted_risk']}")
        lines.append(f"- Risk correct: {item['risk_correct']}")
        lines.append(
            f"- Prompt version: "
            f"{item.get('prompt_version', 'v1')}"
        )

    return "\n".join(lines)


def main():
    results = load_results()
    summaries = summarize_by_mode(results)
    report = build_report(results, summaries)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"Saved report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()