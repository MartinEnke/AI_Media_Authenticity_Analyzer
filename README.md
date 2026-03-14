
# AI Media Authenticity Analyzer

A modular AI engineering project that analyzes images for potential manipulation or AI generation using heuristic analysis, structured reasoning, and automated evaluation pipelines.

This project demonstrates how to design **AI systems infrastructure**, not just ML models.  
It focuses on **orchestration, reasoning pipelines, evaluation, and CI automation**.

---

# Project Goals

The goal of this project is to demonstrate the ability to design and implement:

- AI orchestration workflows
- modular AI tool architecture
- structured reasoning pipelines
- automated model evaluation
- CI/CD integration for AI systems

Accuracy is **not the primary goal** of this project.  
Instead, the focus is on **building robust AI system architecture**.

---

# System Architecture

The system processes an uploaded image and runs it through a modular analysis pipeline.

Pipeline overview:

User Claim  
↓  
Security Scan  
↓  
Image Analysis (heuristics)  
↓  
Reasoning Node (structured explanation)  
↓  
Risk Classification  
↓  
Evaluation & Reporting

The architecture is designed so additional analysis modules (GAN detectors, multimodal models, etc.) can be integrated later.

---

# Key Features

## Image Authenticity Heuristics

The analyzer extracts structural signals from images, including:

- aspect ratio anomalies
- edge density analysis
- alpha channel presence
- metadata inspection
- file signature validation

These signals are aggregated into an **authenticity score** and risk classification.

---

## Structured Reasoning Layer

Instead of returning raw model outputs, the system generates:

- human‑readable reasoning
- confidence explanations
- recommended action

This mirrors how production AI systems often provide **explainability layers**.

Example outputs include:

- authenticity score
- risk level
- reasoning explanation
- confidence explanation

---

## Modular Tool Architecture

The project separates logic into independent components:

- security tools
- image analysis tools
- reasoning nodes
- evaluation utilities

This design allows tools to be swapped or extended without changing the full pipeline.

---

## Evaluation Framework

A built‑in evaluation framework allows testing the pipeline on labeled datasets.

Evaluation tracks metrics such as:

- latency
- heuristic flags
- reasoning presence
- confidence explanation
- expected risk correctness

Results are automatically compiled into structured reports.

Example output:

- `results.json`
- `report.md`

---

## Azure DevOps CI Integration

The project includes a CI pipeline configuration using **Azure Pipelines**.

The pipeline automatically:

1. installs dependencies
2. runs evaluation cases
3. generates evaluation reports
4. publishes artifacts

Pipeline artifacts:

- evaluation results
- generated report

This demonstrates **CI automation for AI system evaluation**.

---

# Technologies Used

Python

- LangGraph
- Pydantic
- Pillow
- NumPy

Infrastructure

- Azure DevOps Pipelines
- GitHub integration

Architecture Concepts

- modular AI pipelines
- evaluation harnesses
- structured reasoning outputs
- CI for ML systems

---

# Example Output

Example analysis result:

Authenticity Score: 0.55  
Risk Level: Medium  

Detected Indicators:

- unusual aspect ratio
- very low edge density
- alpha channel presence

Recommended Action:

Manual review recommended due to multiple heuristic indicators.

---

# Repository Structure

AI_Media_Authenticity_Analyzer

```
ai-orchestrator/
    evaluation/
        evaluator.py
        report_generator.py
        cases/
        dataset/
    tools/
    reasoning/
    security/
azure-pipelines.yml
README.md
```

---

# What This Project Demonstrates

This project showcases skills relevant for **AI engineering and backend AI systems**, including:

- AI pipeline orchestration
- system modularity
- explainable AI outputs
- evaluation workflows
- CI/CD integration for AI systems

---

# Possible Future Extensions

Potential improvements include:

- GAN‑based synthetic image detection
- multimodal reasoning models
- vision‑language models
- larger evaluation datasets
- automated accuracy thresholds in CI

---

# Author

Martin Enke

AI Engineering student focused on:

- AI system design
- Python backend engineering
- applied AI infrastructure
- creative technology and music tools

---

# License

MIT License
