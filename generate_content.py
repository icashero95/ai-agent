import os
from dotenv import load_dotenv
import sys
import functions.config
from call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types

def generate_content():
    user_prompt = sys.argv[1]
    
    verbose = (len(sys.argv) > 2) and (sys.argv[2] == '--verbose')

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[functions.config.available_functions],
            system_instruction= functions.config.system_prompt,
            )
        )
    if response.function_calls:
        for function_call_part in response.function_calls:
            function_result = call_function(function_call_part, verbose=verbose)
            if not (function_result.parts and (len(function_result.parts) > 0)):
                raise Exception("missing function_result.parts")
            part0 = function_result.parts[0]
            if not hasattr(part0, 'function_response') or not part0.function_response.response:
                raise Exception("missing function_response.response")
            if verbose:
                print(f"-> {function_result.parts[0].function_response.response}")
    else:
        if verbose:
            print(f"User prompt: {user_prompt}")
        if response.text:
            print(response.text)
    if verbose and hasattr(response, "usage_metadata"):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")