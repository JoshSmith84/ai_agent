import os
from dotenv import load_dotenv
from google import genai


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("api key not found!")
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    if response.usage_metadata != None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
              f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
    else:
        raise RuntimeError("Failed to fetch usage metadata. " \
                           "API call most likely failed")
    print(response.text)