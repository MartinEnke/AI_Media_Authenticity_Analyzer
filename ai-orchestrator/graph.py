from langgraph.graph import StateGraph, END
from state import GraphState
from analyzers.image_analyzer import analyze_image
from analyzers.audio_analyzer import analyze_audio
from tools.security_tools import security_scan_tool
from utils.llm_reasoning import get_llm_reasoning
from utils.reasoning_builder import build_reasoning
from utils.llm_reasoning import get_llm_reasoning


def intake_node(state: GraphState) -> GraphState:
    return state


def security_node(state: GraphState) -> GraphState:
    security_result = security_scan_tool(
    file_path=state["file_path"],
    declared_mimetype=state["mimetype"],
    media_type=state["media_type"],
)

    state["security_result"] = security_result

    existing_flags = state.get("flags", [])
    security_flags = security_result.get("flags", [])
    state["flags"] = existing_flags + security_flags

    return state


def image_analysis_node(state: GraphState) -> GraphState:
    result = analyze_image(state["file_path"])
    state["analysis_result"] = result

    existing_flags = state.get("flags", [])
    analysis_flags = result.get("flags", [])
    state["flags"] = existing_flags + analysis_flags

    return state


def audio_analysis_node(state: GraphState) -> GraphState:
    result = analyze_audio(state["file_path"])
    state["analysis_result"] = result

    existing_flags = state.get("flags", [])
    analysis_flags = result.get("flags", [])
    state["flags"] = existing_flags + analysis_flags

    return state


def reasoning_node(state: GraphState) -> GraphState:
    reasoning_mode = state.get("reasoning_mode", "llm")

    if reasoning_mode == "rule":
        reasoning_result = build_reasoning(
            flags=state.get("flags", []),
            analysis=state.get("analysis_result", {}),
            security=state.get("security_result", {}),
            claim=state.get("claim"),
        )
    else:
        reasoning_result = get_llm_reasoning(
            flags=state.get("flags", []),
            analysis=state.get("analysis_result", {}),
            security=state.get("security_result", {}),
            claim=state.get("claim"),
        )

    state["reasoning"] = reasoning_result.get("reasoning", "")
    state["confidence_explanation"] = reasoning_result.get("confidence_explanation", "")
    state["summary"] = reasoning_result.get(
        "summary",
        "The uploaded image contains indicators that warrant manual review."
    )

    return state


def scoring_node(state: GraphState) -> GraphState:
    base_score = state.get("analysis_result", {}).get("base_score", 0.2)

    security_flags = state.get("security_result", {}).get("flags", [])
    if security_flags:
        base_score += 0.2

    unique_flags = list(dict.fromkeys(state.get("flags", [])))
    state["flags"] = unique_flags

    base_score = min(base_score, 0.95)

    if base_score >= 0.7:
        risk_level = "high"
        action = "human_review"
    elif base_score >= 0.4:
        risk_level = "medium"
        action = "manual_check"
    else:
        risk_level = "low"
        action = "allow_with_logging"

    state["authenticity_score"] = round(base_score, 2)
    state["risk_level"] = risk_level
    state["recommended_action"] = action

    return state


def router(state: GraphState) -> str:
    return state["media_type"]


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("intake", intake_node)
    graph.add_node("security", security_node)
    graph.add_node("image_analysis", image_analysis_node)
    graph.add_node("audio_analysis", audio_analysis_node)
    graph.add_node("reasoning", reasoning_node)
    graph.add_node("scoring", scoring_node)

    graph.set_entry_point("intake")
    graph.add_edge("intake", "security")

    graph.add_conditional_edges(
        "security",
        router,
        {
            "image": "image_analysis",
            "audio": "audio_analysis",
        }
    )

    graph.add_edge("image_analysis", "reasoning")
    graph.add_edge("audio_analysis", "reasoning")
    graph.add_edge("reasoning", "scoring")
    graph.add_edge("scoring", END)

    return graph.compile()