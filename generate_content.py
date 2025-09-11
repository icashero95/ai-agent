import os
from dotenv import load_dotenv
import sys
import functions.config
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types

def generate_content():
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction= functions.config.system_prompt,
            )
        )
    if (len(sys.argv) > 2) and (sys.argv[2] == '--verbose'):
        if response.text:
            print(f"User prompt: {user_prompt} \n {response.text}")
        else:
            print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} \n Response tokens: {response.usage_metadata.candidates_token_count}")
        for function_call_part in response.function_calls:
            function_result = call_function(function_call_part, verbose=True)
            if not (function_result.parts and (len(function_result.parts) > 0)):
                raise Exception("missing function_result.parts")
            elif not hasattr(function_result.parts[0], 'function_response'):
                raise Exception("missing function_response")
            elif not function_result.parts[0].function_response.response:
                raise Exception("missing function_response.response")
            else:
                print(f"-> {function_result.parts[0].function_response.response}")
    elif response.function_calls:
        for function_call_part in response.function_calls:
            function_result = call_function(function_call_part)
            if not (function_result.parts and (len(function_result.parts) > 0)):
                raise Exception("missing function_result.parts")
            elif not hasattr(function_result.parts[0], 'function_response'):
                raise Exception("missing function_response")
            elif not function_result.parts[0].function_response.response:
                raise Exception("missing function_response.response")
    else:
        print(response.text)