from google import genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")



# 3. Define the schema for a SINGLE question
class QuizQuestion(BaseModel):
    id: int
    question: str
    options: list[str]
    correct_answer: str

# 4. Define the schema for the FULL quiz (a list of questions)
class Quiz(BaseModel):
    questions: list[QuizQuestion]


# 5. Initialize the new Client
client = genai.Client(api_key=api_key)







def generate_quiz(transcript):
    # 6. Define your prompt
    prompt = 'You are a teacher and you just had your students watch a youtube video in class. ' \
    'Now you want to test your students knowledge by giving them a quiz on the youtube video.' \
    'Given the transcript of the youtube video, generate a list of ten appropriate questions ' \
    'and answers to test your students knowledge. Also put a letter followed by a parenthesy before every' \
    'multiple choice: ' + transcript

    # 7. Generate content
    # Note the changes: client.models.generate_content, and the arguments are 'model' and 'contents'
    response = client.models.generate_content(
        model='gemini-2.5-flash', # Updated to the current standard model
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': Quiz.model_json_schema(),
        },
    )

    quiz_data = Quiz.model_validate_json(response.text)

    

    return quiz_data.model_dump_json()