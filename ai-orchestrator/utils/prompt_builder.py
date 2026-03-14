import json
from utils.prompt_templates import PROMPT_TEMPLATES


def build_reasoning_prompt(claim, security, analysis, flags, prompt_version="v1"):
    template = PROMPT_TEMPLATES.get(prompt_version, PROMPT_TEMPLATES["v1"])
    claim_text = claim if claim else "No explicit user claim provided."

    user_prompt = template["user"].format(
        claim=claim_text,
        security_findings=json.dumps(security, indent=2),
        image_findings=json.dumps(analysis, indent=2),
        flags=json.dumps(flags, indent=2),
    )

    return {
        "prompt_version": prompt_version,
        "system_prompt": template["system"].strip(),
        "user_prompt": user_prompt.strip(),
    }