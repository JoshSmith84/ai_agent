import os
import sys
import argparse
from dotenv import load_dotenv
from call_gemini import call_gemini



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

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    max_iterations = int(os.environ.get("MAX_ITER"))
    if api_key == None:
        raise RuntimeError("api key not found!")
    
    messages = []
    i = 0
    for i in range(max_iterations):
        i += 1
        response_text, messages_out, done = call_gemini(api_key,args,messages)
        messages.extend(messages_out)
        args = messages

        if i >= max_iterations:
            sys.exit(f"""Error: Maximum iterations ({max_iterations} reached
                     with no resolution. Exiting...)""")
        if done == 0:
            continue
        else:
            break

    print(response_text)
    print(f"iterations taken: {i}")
    sys.exit()
 

