from llm_client import LLMClient

def main():
    client = LLMClient()

    # Single-turn response
    prompt = "What are the three most important things to consider when designing a chatbot?"
    response = client.generate_response(prompt)
    print(f"Response: {response}")

    # Multi-turn conversation
    user_message = "What's the capital of France?"
    response = client.chat(user_message)
    print(f"User: {user_message}")
    print(f"Model: {response}")

    user_message_2 = "And what's the capital of Germany?"
    response_2 = client.chat(user_message_2, history=[user_message])
    print(f"User: {user_message_2}")
    print(f"Model: {response_2}")

if __name__ == "__main__":
    main()