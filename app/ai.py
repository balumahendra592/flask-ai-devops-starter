import os
import anthropic

# Uses Claude (Anthropic) — swap with OpenAI if preferred
# Set ANTHROPIC_API_KEY in your .env or environment variables

def ask_ai(prompt: str) -> str:
    """Send a prompt to Claude and return the response text."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text
