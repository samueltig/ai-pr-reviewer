from openai import OpenAI

class AIReviewer:
    """Handles code review generation using an AI Language Model."""

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_review(self, code_diff: str) -> str:
        """Sends the code diff to the AI model and returns a professional review."""
        
        prompt = (
            "You are a Senior Software Engineer reviewing a Pull Request. "
            "Analyze the following code changes. Point out bugs, suggest security and performance improvements, "
            "and highlight good practices. Format your response in clean Markdown.\n\n"
            f"Code Diff:\n{code_diff}"
        )

        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful and expert AI code reviewer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.2 # Low temperature keeps the AI focused and logical
        )
        
        return response.choices[0].message.content