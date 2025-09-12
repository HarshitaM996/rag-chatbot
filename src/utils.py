def validate_prompt(prompt: str) -> bool:
    """Validate the user prompt to ensure it is not empty."""
    return bool(prompt.strip())

def format_response(response: str) -> str:
    """Format the response from the LLM for better readability."""
    return response.strip() if response else "No response received."