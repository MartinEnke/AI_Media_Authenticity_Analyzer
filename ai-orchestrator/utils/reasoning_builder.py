from typing import Dict, Any, List, Optional


FLAG_EXPLANATIONS = {
    "missing_metadata": "The image does not contain normal metadata, which can happen after export, stripping, or synthetic generation workflows.",
    "very_low_resolution": "The image has very limited resolution in at least one dimension, reducing traceability and making manipulation assessment harder.",
    "unusual_aspect_ratio": "The image uses an unusual aspect ratio, which can appear in banners, crops, composites, or generated assets.",
    "has_alpha_channel": "The image contains an alpha channel, which may indicate transparency, layering, or compositing workflows.",
    "very_small_file_size": "The file size is unusually small, which can indicate aggressive export compression or minimal image complexity.",
    "very_low_edge_density": "The image has very low edge density, suggesting unusually smooth or low-detail content.",
    "mimetype_mismatch": "The declared file type does not match the detected file signature, which is a security-relevant inconsistency.",
    "empty_file": "The uploaded file is empty and cannot be trusted for normal analysis.",
    "file_missing": "The uploaded file could not be found during processing.",
}


def build_reasoning(
    flags: List[str],
    analysis: Dict[str, Any],
    security: Dict[str, Any],
    claim: Optional[str] = None,
) -> Dict[str, str]:
    claim_text = claim.strip() if claim else ""

    if not flags:
        reasoning = (
            "The image did not trigger any major heuristic indicators in the current analysis pipeline. "
            "This does not prove authenticity, but it means no strong warning signals were detected by the current checks."
        )

        if claim_text:
            reasoning += f" In relation to the user's question ('{claim_text}'), the current evidence does not provide a strong warning signal."

        confidence = (
            "Confidence is limited because the current result is based on heuristic screening rather than a full forensic model."
        )

        summary = "No obvious suspicious indicators were detected in the uploaded image."
        return {
            "reasoning": reasoning,
            "confidence_explanation": confidence,
            "summary": summary,
        }

    unique_flags = list(dict.fromkeys(flags))
    evidence_lines = []

    for flag in unique_flags:
        if flag in FLAG_EXPLANATIONS:
            evidence_lines.append(FLAG_EXPLANATIONS[flag])

    aspect_ratio = analysis.get("aspect_ratio")
    edge_density = analysis.get("edge_density")
    mode = analysis.get("mode")
    detected_type = security.get("detected_type")
    mimetype_matches = security.get("mimetype_matches", True)

    extra_context = []

    if aspect_ratio is not None:
        extra_context.append(f"The measured aspect ratio is {aspect_ratio}.")
    if edge_density is not None:
        extra_context.append(f"The measured edge density is {edge_density}.")
    if mode:
        extra_context.append(f"The image mode is {mode}.")
    if detected_type:
        extra_context.append(f"The detected file signature is {detected_type}.")
    if mimetype_matches is False:
        extra_context.append("The declared mimetype and detected file signature do not match.")

    reasoning_parts = []

    if claim_text:
        reasoning_parts.append(
            f"In relation to the user's question ('{claim_text}'), the image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media."
        )
    else:
        reasoning_parts.append(
            "The image triggered multiple heuristic indicators that can be associated with synthetic, composited, or heavily processed media."
        )

    if evidence_lines:
        reasoning_parts.append(" ".join(evidence_lines))

    if extra_context:
        reasoning_parts.append(" ".join(extra_context))

    reasoning_parts.append(
        "These findings are suggestive rather than conclusive, so the result should be interpreted as a risk signal, not as proof of manipulation."
    )

    reasoning = " ".join(reasoning_parts)

    flag_count = len(unique_flags)
    security_flags = security.get("flags", [])

    if "mimetype_mismatch" in unique_flags or "empty_file" in unique_flags or "file_missing" in unique_flags:
        confidence = (
            "Confidence is elevated because the result includes a direct file integrity or type inconsistency, which is a stronger signal than visual heuristics alone."
        )
    elif flag_count >= 4:
        confidence = (
            "Confidence is moderate because several independent heuristic indicators point in the same direction, but none of them alone is definitive."
        )
    elif flag_count >= 2:
        confidence = (
            "Confidence is moderate-to-limited because the assessment depends on a small set of heuristic indicators rather than a decisive authenticity failure."
        )
    else:
        confidence = (
            "Confidence is limited because the result is driven by a single or weak indicator that could also occur in legitimate edited media."
        )

    if security_flags:
        summary = "The uploaded image contains technical and structural indicators that warrant manual review."
    else:
        summary = "The uploaded image contains several structural indicators that warrant manual review."

    if claim_text:
        summary = f"In relation to the user's question, the uploaded image contains indicators that warrant manual review."

    return {
        "reasoning": reasoning,
        "confidence_explanation": confidence,
        "summary": summary,
    }