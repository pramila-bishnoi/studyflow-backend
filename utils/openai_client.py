import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY missing in .env")

        self.client = Client(api_key=api_key)

    def generate_text(self, prompt: str, mode: str):
        try:
            final_prompt = f"Mode: {mode}\n\nText:\n{prompt}\n\nGenerate structured study notes."

            # ✅ Correct Google GenAI function
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=final_prompt
            )

            return response.text

        except Exception as e:
            return f"Error: {str(e)}"
