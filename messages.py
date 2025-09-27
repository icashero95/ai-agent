from google.genai import types

def init_messages(user_prompt: str):
    return [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt)]
            )
        ]
