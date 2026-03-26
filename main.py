import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Gemini in your CLI")
    parser.add_argument("ai_prompt", 
                        type=str, 
                        help="Type a prompt for Google Gemini enclosed in quotes"
                        )
    parser.add_argument("--verbose", 
                        action="store_true", 
                        help="Enable verbose output"
                        )
    args = parser.parse_args()

    messages = [
        types.Content(role="user", 
                      parts=[types.Part(text=args.ai_prompt)]
                      )
        ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("api key not found!")
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0,
            )
    )
    if response.usage_metadata == None:
        raise RuntimeError("Failed to fetch usage metadata. " \
                           "API call most likely failed"
                           )

    if args.verbose:
        print(f"\nUser prompt: {args.ai_prompt}\n"
              f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
              f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
              )   

    if response.function_calls:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(response.text)

