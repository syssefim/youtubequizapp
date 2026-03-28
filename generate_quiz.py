from google import genai
import os
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

# 3. Initialize the new Client
client = genai.Client(api_key=api_key)







def generate_quiz(transcript):
    # 4. Define your prompt
    prompt = "Based off of this text, create a multiple choice quiz with 7 questions. Then return the questions and answers as a json object: " + transcript

    # 5. Generate content
    # Note the changes: client.models.generate_content, and the arguments are 'model' and 'contents'
    response = client.models.generate_content(
        model='gemini-2.5-flash', # Updated to the current standard model
        contents=prompt
    )

    #print(response.text)
    return response