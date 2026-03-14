
# AI Media Authenticity Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Node.js](https://img.shields.io/badge/Node.js-Fastify-green)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)
![Gemini](https://img.shields.io/badge/Gemini-LLM-orange)

An AI engineering portfolio project that analyzes images for potential manipulation or AI generation using a modular analysis pipeline, structured reasoning, evaluation tooling, and CI‑ready infrastructure.

The goal of this project is **not to build a perfect AI detector**, but to demonstrate how to design and implement a **production‑style AI system architecture** including orchestration, explainability, evaluation, and deployment infrastructure.

The system combines:

• tool‑based analysis pipelines  
• LLM‑assisted reasoning  
• structured prompt engineering  
• evaluation tooling  
• CI/CD configuration  
• a modern web interface  

---

# Project Overview

This system analyzes media (currently images) and produces a structured authenticity assessment including:

• authenticity score  
• risk level classification  
• detected heuristic flags  
• reasoning explanation  
• confidence explanation  
• recommended action  

The architecture reflects how **real‑world AI systems aggregate multiple signals** rather than relying on a single model.

---

# Architecture

The system uses a modular pipeline orchestrated with **LangGraph**.

User Upload / Claim  
→ Next.js Frontend  
→ Fastify API Gateway  
→ Python AI Orchestrator  
→ LangGraph Pipeline  

Pipeline tools:

• Security Scan Tool  
• Image Analysis Tool  
• LLM Reasoning Engine  

Output:

• Authenticity Score  
• Risk Classification  
• Recommended Action  

Evaluation system:

• Results JSON  
• Markdown Reports  
• CI Pipeline Integration

---

# Pipeline Flow

Intake  
→ Security Scan  
→ Image Analysis  
→ Prompt Builder  
→ Reasoning Node  
→ Scoring Engine  
→ Output  

Each stage contributes structured signals interpreted by the reasoning layer.

This architecture mirrors **production AI workflows where models are only one component of a larger system**.

---

# Core Features

## Image Authenticity Heuristics

The analyzer extracts structural indicators such as:

• aspect ratio anomalies  
• edge density analysis  
• alpha channel detection  
• EXIF metadata inspection  
• file signature validation  
• image dimension checks  

These indicators feed a heuristic authenticity scoring system.

---

## Structured Reasoning Layer

Instead of returning raw technical signals, the system generates explainable outputs:

• summary  
• reasoning explanation  
• confidence explanation  

This simulates **explainable reasoning layers used in real‑world AI systems**.

---

## Hybrid Reasoning System

Two reasoning strategies are supported:

Rule‑based reasoning  
Deterministic explanation generated from heuristic findings.

LLM reasoning  
Google **Gemini** interprets the analysis signals and produces structured reasoning.

The system can switch between reasoning modes for evaluation purposes.

---

## Prompt Engineering + Versioning

The project includes a structured prompt experimentation system:

• prompt templates  
• prompt builder utilities  
• prompt preview in outputs  
• multiple prompt versions (v1 / v2)

This allows controlled experimentation with LLM reasoning behavior.

---

## Tool‑Based Architecture

The pipeline is intentionally modular.

Tools currently include:

• security scan tool  
• metadata extraction  
• edge density analysis  
• image structure flag detection  

New tools can be added without rewriting orchestration logic.

---

# Evaluation Framework

The repository includes a built‑in evaluation system for benchmarking reasoning strategies.

Metrics include:

• latency  
• fallback usage  
• expected flag thresholds  
• reasoning length  
• confidence explanation length  
• risk classification correctness  

Evaluation artifacts:

evaluation/results.json  
evaluation/report.md  

---

# Azure DevOps CI Integration

The repository contains an **Azure DevOps pipeline configuration**.

The pipeline is designed to:

• install dependencies  
• run evaluation scripts  
• generate evaluation reports  
• publish artifacts  

Hosted pipeline execution currently requires Azure hosted parallelism approval for new/free accounts, but the CI configuration demonstrates how AI workflows integrate into CI/CD pipelines.

---

# Web Interface

The project includes a lightweight web UI built with **Next.js**.

Users can:

• upload images  
• submit authenticity questions  
• view reasoning explanations  
• inspect analysis signals  

This demonstrates how an AI analysis backend can be exposed through a modern web interface.

---

# Technology Stack

AI Orchestration  
Python  
LangGraph  
Pydantic  

Image Processing  
Pillow  
NumPy  

LLM Integration  
Google Gemini API  

Backend API  
Node.js  
Fastify  

Frontend  
Next.js  

Infrastructure  
Azure DevOps Pipelines  
GitHub  

---

# Example Output

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
  "recommended_action": "manual_check"
}

---

# Repository Structure

AI_Media_Authenticity_Analyzer

frontend  
Next.js web interface

api-gateway  
Fastify API server

ai-orchestrator  
analysis tools  
LangGraph pipeline  
evaluation framework

azure-pipelines.yml  
CI pipeline configuration

---

# Running the Project

Clone the repository

git clone https://github.com/<your-username>/AI_Media_Authenticity_Analyzer.git

Create environment

cd ai-orchestrator
python -m venv .venv
source .venv/bin/activate

Install dependencies

pip install -r requirements-devops.txt

Run analyzer

python main.py

---

# Quick Demo

python main.py <<'EOF'
{
  "request_id":"demo-001",
  "file_path":"/path/to/image.png",
  "filename":"image.png",
  "media_type":"image",
  "mimetype":"image/png",
  "claim":"Is this image AI-generated?",
  "reasoning_mode":"llm",
  "prompt_version":"v2"
}
EOF

---

# Why This Project Is Valuable

This repository demonstrates the ability to build:

• orchestrated AI pipelines  
• tool‑based AI architectures  
• structured reasoning systems  
• prompt experimentation infrastructure  
• evaluation frameworks  
• CI‑integrated AI workflows  

The focus is on **AI engineering and system design**, not just model usage.

---

# Future Extensions

Planned improvements:

• audio deepfake detection  
• additional image forensic signals  
• larger benchmark datasets  
• model comparison (Gemini / GPT / open models)  
• containerized deployment  
• hosted inference API  
• evaluation dashboards

---

# Author

Martin Enke

AI engineering student focused on:

• AI systems architecture  
• Python backend engineering  
• applied AI infrastructure  
• creative technology and audio tools  

---

# License

MIT License
