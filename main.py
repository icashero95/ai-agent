import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types


def main():
    print("Hello from ai-agent!")
    if len(sys.argv) < 2:
        print("No prompt arguments provided.")
        sys.exit(1)
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    if (len(sys.argv) > 2) and (sys.argv[2] == '--verbose'):
        print(f"User prompt: {user_prompt} \n {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} \n Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()




