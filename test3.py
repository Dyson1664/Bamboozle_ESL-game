from flask import Flask, render_template, request, redirect, url_for, session, send_file

from dotenv import load_dotenv
import os
from time import sleep
import db_1
import openai

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')
API_KEY = os.getenv('API_KEY')
from docx import Document


def generate_esl_quiz(vocab_words, api_key, max_tokens=550):
    """
    Function to generate an EASY ESL quiz for 10-year-olds.

    Parameters:
    - vocab_words: A list of vocabulary words to include in the quiz.
    - api_key: API key for OpenAI.
    - max_tokens: The maximum length of the generated quiz.
    """
    if not vocab_words:
        return "Vocabulary list is empty."

    formatted_vocab = ', '.join(vocab_words)
    prompt = f"Create an EASY ESL quiz for ten year olds about the following vocab words: {formatted_vocab}. " \
             f"Create TEN fill in the gap sentences with ten of the words. Make it easy. Also create a short comprehension with some of the words. " \
             f"It should be 1 page in total. ONLY gap fill and comprehension. Dont give the answers" \
             f"Above the fill in the blank questions should be ONLY BE THE TEN vocab words that the students can cross off after they answer each gap fill" \
             f"Here is an example" \
             '''VOCABULARY WORDS:

Farm, Mountain, Path, River, Village, Cable Car, Exercise, Tree, Country, Story

FILL IN THE GAP:

1. The apple ________ is next to the village.

2. I like to climb the _________ during summer vacation.

3. A narrow ________ leads to the ancient castle.

4. The ________ flows quietly under the wooden bridge.

5. Many people in the _________ know each other well.

6. I saw a spectacular view when I took the ________ to the top.

7. I ________ every morning to keep myself fit.

8. We enjoyed a picnic under the shade of a big ________.

9. I live in a small ________ in Europe.

10. Can you tell me a ________ before I go to bed?

COMPREHENSION:

Billy went to visit his Grandma who lives in a small village in the countryside. It was a tranquil place surrounded by mountains and a beautiful river that glistened under the sun. Every morning, Billy would exercise by running along a path that passed through a lush farm full of apple trees. One day, he decided to take an adventurous trip alone. Walking further along the path, he noticed a cable car station. Intrigued by this, Billy decided to take the cable car up the mountain, where he found a gorgeous waterfall. Overwhelmed by the extraordinary sight, Billy took back many stories to tell his friends in the city about his village adventure.

Questions:

1. Where does Billy's Grandma live?
   
2. What was Billy's daily exercise routine?

3. How did Billy go up the mountain?

4. What did Billy find at the top of the mountain?

5. Who did Billy want to share his adventure stories with?


Process finished with exit code 0'''


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
quiz_vocab = ['farm', 'field', 'forest', 'lake', 'mountain', 'path', 'river', 'town', 'village', 'waterfall', 'cable car', 'subway', 'exercise', 'tree', 'beach', 'country', 'week', 'please', 'story']
quiz = generate_esl_quiz(quiz_vocab, API_KEY)
print(quiz)


def create_a_word_document(text):
    doc = Document()
    doc.add_paragraph(text)
    filename = 'generated.docx'
    doc.save(filename)
    print(f"Document saved as {filename}")

create_a_word_document(quiz)