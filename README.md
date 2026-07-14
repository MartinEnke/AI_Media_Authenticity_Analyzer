# AI Media Authenticity Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)
![MCP](https://img.shields.io/badge/MCP-Tool%20Protocol-blueviolet)
![Gemini](https://img.shields.io/badge/Gemini-Reasoning-orange)

## Explainable Media Authenticity Analysis with LangGraph & MCP

An AI engineering portfolio project demonstrating how modular forensic
analysis, LangGraph orchestration, MCP-based tools and LLM reasoning can
be combined into an explainable media authenticity assessment pipeline.

Rather than attempting to build a perfect **AI image detector**, this
project explores how multiple independent forensic signals can be
orchestrated into a transparent and extensible analysis workflow. The
emphasis is on **AI engineering, explainability, evaluation and system
architecture** rather than claiming perfect detection accuracy.

------------------------------------------------------------------------

# Why this project?

Modern generative models can closely imitate real photographs, making
deterministic AI detection increasingly unreliable.

Instead of relying on a single prediction model, this project aggregates
multiple independent forensic signals into an explainable assessment.
Every stage contributes structured evidence that is interpreted by the
reasoning layer and presented transparently to the user.

The project demonstrates production-oriented AI engineering concepts
including:

-   LangGraph workflow orchestration
-   Model Context Protocol (MCP)
-   modular analysis tools
-   structured reasoning
-   prompt engineering
-   evaluation pipelines
-   modern frontend architecture

------------------------------------------------------------------------

# Architecture

``` text
Image Upload
      │
      ▼
Security Validation (MCP)
      │
      ▼
Metadata Extraction (MCP)
      │
      ▼
Structural Image Analysis (MCP)
      │
      ▼
LangGraph Orchestration
      │
      ▼
Rule-based + Gemini Reasoning
      │
      ▼
Authenticity Assessment
      │
      ▼
Explainable Next.js Frontend
```

Each component has a single responsibility, making the pipeline easy to
extend with additional forensic modules.

------------------------------------------------------------------------

# Pipeline

1.  User uploads an image.
2.  Independent MCP tools analyse different characteristics.
3.  LangGraph orchestrates execution and aggregates structured results.
4.  Rule-based scoring combines forensic evidence.
5.  Gemini generates an explainable analyst summary.
6.  Results are visualised with confidence levels, evidence cards and
    pipeline trace.

------------------------------------------------------------------------

# MCP Tool Architecture

Every forensic capability is implemented as an independent MCP tool.

Current tools include:

-   Security Scan
-   Metadata Extraction
-   Edge Density Analysis
-   Image Structure Analysis

This architecture allows new forensic detectors to be added without
changing the orchestration workflow.

------------------------------------------------------------------------

# Explainable Analysis

Instead of returning only a classification, the application explains
*why* a conclusion was reached.

The interface presents:

-   Authenticity Risk Score
-   Media Profile
-   Confidence
-   Analyst Summary
-   Individual forensic evidence
-   Score contribution of each signal
-   Pipeline execution trace

This makes the decision process transparent and easier to evaluate.

------------------------------------------------------------------------

# Evaluation Framework

The repository includes an evaluation framework for comparing reasoning
strategies and prompt versions.

Collected metrics include:

-   latency
-   prompt version
-   reasoning mode
-   detected signals
-   confidence
-   risk score
-   evaluation reports

The focus is on measuring pipeline behaviour rather than model accuracy
alone.

------------------------------------------------------------------------

# Technology Stack

### AI

-   Python
-   LangGraph
-   Gemini
-   Pydantic

### MCP Tools

-   Security validation
-   Metadata extraction
-   Image heuristics

### Frontend

-   Next.js
-   React

### Backend

-   FastAPI
-   Node.js API Gateway

### Infrastructure

-   Azure DevOps Pipelines
-   GitHub

------------------------------------------------------------------------

# Project Structure

``` text
frontend/
api-gateway/
ai-orchestrator/
    analysis/
    mcp/
    langgraph/
    evaluation/
```

------------------------------------------------------------------------

# Future Improvements

Planned extensions include:

-   additional forensic MCP tools (noise/frequency analysis)
-   expanded benchmark datasets
-   model comparison
-   containerised deployment
-   hosted inference API
-   evaluation dashboards

------------------------------------------------------------------------

# Key Takeaways

This project demonstrates:

-   AI workflow orchestration
-   MCP integration
-   explainable AI
-   modular system design
-   structured reasoning
-   evaluation-driven development
-   production-oriented AI engineering

The objective is not to claim perfect AI detection, but to build a
realistic, transparent and extensible media authenticity analysis
platform.

------------------------------------------------------------------------

# Author

**Martin Enke**

Software Engineer focused on AI systems, backend engineering, LLM
applications and creative technology.