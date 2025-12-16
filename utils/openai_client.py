import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class OpenAIClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY missing")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_text(self, text: str, mode: str):
        final_prompt = f"""
Mode: {mode}

Text:
{text}

Generate structured study notes.
"""
        response = self.model.generate_content(final_prompt)
        return response.text
