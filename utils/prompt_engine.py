class PromptEngine:
    def get_system_prompt(self, mode):

        if mode == "summary":
            return "Summarize the text into clear bullet points."

        if mode == "outline":
            return "Convert this text into a clean structured outline."

        # default: full notes
        return (
            "You are an expert study notes generator. Convert the user text into "
            "clear, structured, student-friendly study notes with headings, bullets, "
            "explanations and examples."
        )
