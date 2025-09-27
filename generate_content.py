import os
from dotenv import load_dotenv
import functions.config
from call_function import call_function
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))



def generate_content(messages, verbose=False):
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[functions.config.available_functions],
            system_instruction= functions.config.system_prompt,
            )
        )
    #appending candidates
    if getattr(response, "candidates", None):
        for cand in response.candidates:
            if getattr(cand, "content", None):
                messages.append(cand.content)
    if response.function_calls:
        for fc in response.function_calls:
            print(f"- Calling function: {fc.name}")
            function_result = call_function(fc, verbose=verbose)
            if verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            #converting function_result into user message
            tool_msg = types.Content(
                role="user",
                parts=function_result.parts, # parts already includes function_response
            )
            messages.append(tool_msg)
            if verbose:
                print("Appended tool response")

    return response