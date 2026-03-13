# AI Media Authenticity Analyzer

An AI-powered system for analyzing image authenticity using a
combination of deterministic media analysis, tool-based architecture,
and LLM-assisted reasoning.
The project includes an evaluation harness that compares rule-based and LLM-assisted reasoning modes across latency, fallback behavior, output completeness, and expected signal detection.

The project demonstrates modern AI system design patterns including:

-   LangGraph orchestration pipelines
-   MCP (Model Context Protocol) tool architecture
-   modular media analysis tools
-   claim-aware AI reasoning
-   explainable authenticity scoring
-   resilient fallback behavior when LLMs are unavailable

------------------------------------------------------------------------

# Architecture

The system processes uploaded media through a multi-stage pipeline:

API Gateway (Fastify / Node.js) ↓ Python AI Orchestrator (LangGraph) ↓
MCP Tool Server ↓ Media Analysis Tools

Pipeline stages:

Intake → Security Scan → Image Feature Analysis → AI Reasoning →
Authenticity Scoring → Output

------------------------------------------------------------------------

# Key Features

## Media Security Validation

The system verifies file integrity before analysis.

Examples:

-   file signature validation
-   mimetype mismatch detection
-   empty file detection
-   basic tampering signals

------------------------------------------------------------------------

## Image Structure Analysis

The analyzer extracts structural indicators including:

-   resolution
-   aspect ratio
-   alpha channel presence
-   EXIF metadata
-   edge density
-   file size characteristics

These signals are used to detect potential:

-   synthetic media
-   heavy compositing
-   generated assets
-   suspicious export patterns

------------------------------------------------------------------------

## Explainable AI Reasoning

The system generates a human-readable explanation that interprets
detected indicators and relates them to the user's question.

Example claim-aware analysis:

"Is this image AI-generated?"

The system responds with:

-   summary
-   reasoning
-   confidence explanation
-   recommended action

------------------------------------------------------------------------

## MCP Tool Architecture

Analysis functions are exposed as MCP tools:

security_scan\
extract_metadata\
compute_edge_density\
detect_image_structure_flags

This enables:

-   modular AI tool orchestration
-   future remote tool execution
-   compatibility with agent-style architectures

------------------------------------------------------------------------

## LangGraph Orchestration

The analysis pipeline is implemented using LangGraph, enabling:

-   modular workflow nodes
-   deterministic + AI reasoning combination
-   future agent tool-calling support

------------------------------------------------------------------------

# Example Response

``` json
{
  "authenticity_score": 0.55,
  "risk_level": "medium",
  "flags": [
    "very_low_resolution",
    "unusual_aspect_ratio",
    "has_alpha_channel",
    "very_low_edge_density"
  ],
  "summary": "The uploaded image contains indicators that warrant manual review.",
  "reasoning": "...",
  "confidence_explanation": "...",
  "recommended_action": "manual_check"
}
```

------------------------------------------------------------------------

# Technology Stack

Backend:

-   Python
-   LangGraph
-   MCP (Model Context Protocol)
-   Pillow
-   NumPy

API Layer:

-   Node.js
-   Fastify

AI:

-   Gemini LLM (optional reasoning layer)
-   rule-based fallback reasoning

------------------------------------------------------------------------

# Design Goals

This project explores how AI systems can combine:

-   deterministic media analysis
-   modular tool architectures
-   LLM reasoning
-   explainable outputs

to support **media authenticity assessment**.

The architecture emphasizes:

-   explainability
-   modularity
-   orchestration
-   reliability

------------------------------------------------------------------------

# Project Status

Current version:

v0.1

Implemented:

-   LangGraph orchestration
-   MCP tool server
-   image authenticity heuristics
-   claim-aware reasoning
-   Fastify upload API

Upcoming:

-   evaluation framework
-   model comparison
-   audio analysis module
-   GAN artifact detection
