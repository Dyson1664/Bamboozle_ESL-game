from dotenv import load_dotenv
import os
from time import sleep
import db_1
import openai

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')
API_KEY = os.getenv('API_KEY')

def generate_esl_quiz(vocab_words, api_key, max_tokens=550):
    """
    Function to generate an ESL quiz for 10-year-olds using the OpenAI GPT-4 Chat model.

    Parameters:
    - vocab_words: A list of vocabulary words to include in the quiz.
    - api_key: API key for OpenAI.
    - max_tokens: The maximum length of the generated quiz.
    """
    if not vocab_words:
        return "Vocabulary list is empty."

    formatted_vocab = ', '.join(vocab_words)
    prompt = f"Create a easy ESL quiz about the following vocab words: {formatted_vocab}. " \
             f"Create a gap fill with the words. Also create a short comprehension with some of the words. " \
             f"It should be 1 page in total. ONLY gap fill and comprehension. Dont give the answers"

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the GPT-4 model
            messages=[
                {"role": "system", "content": "You are a skilled ESL teacher."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
quiz_vocab = ['egg', 'ball', 'hat', 'apple', 'big', 'small']
quiz = generate_esl_quiz(quiz_vocab, API_KEY)
print(quiz)