import openai
import os
from dotenv import load_dotenv


load_dotenv() # Imports the API Key


openai.api_key = os.getenv("OPENAI_API_KEY")


client = openai

def check_facts(subtitles):
    prompt = f"""You are the AI fact-checker. I will provide you with some prompts, and your task is to determine whether they are true or false. 
    This is a political debate, so you must indicate who is telling the truth and who is not by starting with their statement, followed by whether it is true or false.
    For example: 'Trump or Harris' - their statement - It must be either true or false, not partially true or partially false, and include the number in front. 
    {subtitles}"""

    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI factchekcer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000)
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Error during GPT fact check: {e}")
        return "Error checking facts"
