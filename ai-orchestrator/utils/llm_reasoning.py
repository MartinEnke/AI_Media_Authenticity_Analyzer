import os
import json
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from google import genai
import sys

from utils.reasoning_builder import build_reasoning

# Load .env explicitly from ai-orchestrator root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def build_llm_reasoning_prompt(
    flags: List[str],
    analysis: Dict[str, Any],
    security: Dict[str, Any],
    claim: Optional[str] = None,
) -> str:
    return f"""
You are an AI media authenticity analysis assistant.

Your task is to interpret technical findings from an image authenticity pipeline.

Rules:
- Do NOT invent forensic evidence.
- Treat findings as heuristic indicators, not proof.
- Mention uncertainty clearly.
- If a user claim exists, address it.
- Return STRICT JSON only.

Required JSON format:
{{
  "summary": "...",
  "reasoning": "...",
  "confidence_explanation": "..."
}}

User claim:
{claim or "None"}

Flags:
{json.dumps(flags, indent=2)}

Security findings:
{json.dumps(security, indent=2)}

Analysis findings:
{json.dumps(analysis, indent=2)}
""".strip()


def get_llm_reasoning(
    flags: List[str],
    analysis: Dict[str, Any],
    security: Dict[str, Any],
    claim: Optional[str] = None,
) -> Dict[str, str]:
    if not api_key:
        fallback = build_reasoning(
            flags=flags,
            analysis=analysis,
            security=security,
            claim=claim,
        )
        fallback["confidence_explanation"] += " LLM fallback was used because GEMINI_API_KEY was not found."
        return fallback

    prompt = build_llm_reasoning_prompt(
        flags=flags,
        analysis=analysis,
        security=security,
        claim=claim,
    )

    try:
        response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
        text = response.text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "summary": "The uploaded image contains indicators that warrant manual review.",
                "reasoning": text,
                "confidence_explanation": "Confidence is limited because the Gemini response could not be parsed as structured JSON.",
            }

    except Exception as e:
        print(f"Gemini error: {e}", file=sys.stderr)
        fallback = build_reasoning(
            flags=flags,
            analysis=analysis,
            security=security,
            claim=claim,
    )
    fallback["confidence_explanation"] += " LLM fallback was used because the external reasoning model was temporarily unavailable."
    return fallback