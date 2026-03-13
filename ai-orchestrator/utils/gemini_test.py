import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(".env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

for m in genai.list_models():
    name = getattr(m, "name", "")
    methods = getattr(m, "supported_generation_methods", [])
    if "generateContent" in methods:
        print(name, methods)