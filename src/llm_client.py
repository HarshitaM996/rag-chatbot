import google.generativeai as genai
import os
from dotenv import load_dotenv

class LLMClient:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Configure the API key
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY is not set. Please check your environment variables or .env file.")
        genai.configure(api_key=self.api_key)

        # Choose a model
        # gemini-1.5-flash: A fast, efficient, and versatile model.
        # gemini-1.5-pro: A more powerful model with a larger context window, ideal for complex tasks.
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        # Make a simple text generation call
        response = self.model.generate_content(prompt)
        return response.text

    def chat(self, user_message, history=None):
        # Handle multi-turn conversations (chat history)
        if history is None:
            history = []
        chat = self.model.start_chat(history=history)
        response = chat.send_message(user_message)
        return response.text