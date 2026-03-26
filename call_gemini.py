import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def call_gemini(api_key, prompt, messages):

    if isinstance(prompt, list) == False:
        
        messages.extend([
            types.Content(role="user", 
                            parts=[types.Part(text=prompt.ai_prompt)]
                            )
            ]
        )

    verbose_text = ''

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
    if isinstance(prompt, list) == False:
        if prompt.verbose:
            verbose_text += f"\nUser prompt: {prompt.ai_prompt}\n" \
                            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n" \
                            f"Response tokens: {response.usage_metadata.candidates_token_count}\n"


    for i in response.candidates:
       messages.append(i.content)
    
 
    function_call_result_list = []
    if response.function_calls:
        for call in response.function_calls:
            function_call_result = call_function(call)

            if function_call_result.parts == None:
                raise Exception(f"Error: {call.name} .parts are empty")
            if function_call_result.parts[0].function_response == None:
                raise Exception(f"Error: {call.name}'s FunctionResponse returned empty")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception(f"Error: {call.name}'s actual call result returned empty")
            

            function_call_result_list.append(function_call_result.parts[0])
        
        messages.append(types.Content(role="user", parts=function_call_result_list))
        return verbose_text, messages, 0
    else:
        return verbose_text + response.text, messages, 1