import os
import json
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from google import genai

from utils.reasoning_builder import build_reasoning
from utils.prompt_builder import build_reasoning_prompt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None


def get_llm_reasoning(
    flags: List[str],
    analysis: Dict[str, Any],
    security: Dict[str, Any],
    claim: Optional[str] = None,
    prompt_version: str = "v1",
) -> Dict[str, str]:
    if not api_key or client is None:
        fallback = build_reasoning(
            flags=flags,
            analysis=analysis,
            security=security,
            claim=claim,
        )
        fallback["confidence_explanation"] += " LLM fallback was used because the external reasoning model was temporarily unavailable."
        return fallback

    prompt_parts = build_reasoning_prompt(
    claim=claim,
    security=security,
    analysis=analysis,
    flags=flags,
    prompt_version=prompt_version,
)

    combined_prompt = (
        f"{prompt_parts['system_prompt']}\n\n"
        f"{prompt_parts['user_prompt']}\n\n"
        "Return valid JSON only with keys: summary, reasoning, confidence_explanation."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=combined_prompt
        )

        text = response.text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "summary": "The uploaded image contains indicators that warrant manual review.",
                "reasoning": text,
                "confidence_explanation": "Confidence is limited because the model response was not valid JSON.",
            }

    except Exception:
        fallback = build_reasoning(
            flags=flags,
            analysis=analysis,
            security=security,
            claim=claim,
        )
        fallback["confidence_explanation"] += " LLM fallback was used because the external reasoning model was temporarily unavailable."
        return fallback