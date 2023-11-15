from flask import Flask, render_template, request, redirect, url_for, session, send_file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from time import sleep
import db_1
import openai
from docx import Document
import threading

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')
API_KEY = os.getenv('API_KEY')
E_PASS = os.getenv('E_PASS')
E_NAME = os.getenv('E_NAME')
app = Flask(__name__)
app.secret_key = 'your_secret_key'

class Driver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def vocabs_to_enter(self, name, unit):
        title, vocabs = db_1.get_vocab(name, unit)
        return title, vocabs
    def enter_vocab(self, title, vocabs):
        self.driver.get('http://127.0.0.1:5001/vocab')
        try:
            title_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, 'title')))
            title_box.clear()
            title_box.send_keys(title)

            for num, box in enumerate(vocabs, start=1):
                input_box = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, f'vocab{num}')))
                input_box.clear()
                input_box.send_keys(box)

        except WebDriverException as e:
            print("Exception occurred while interacting with the element: ", e)



    def sign_in(self, url, email, password):
        self.driver.get(url)
        try:
            email_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_input.send_keys(email)
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password")))
            password_input.send_keys(password)
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            sign_in_button.click()
        except WebDriverException as e:
            print("Exception occurred while interacting with the element: ", e)

    #create game name and description
    def create_game(self, title='Vocab :)'):
        try:
            title_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'one')))
            title_box.send_keys(title)

            description_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'two')))
            description_box.send_keys(title)

            make_game_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'five')))
            make_game_button.click()

        except WebDriverException as e:
            print("Exception occurred while interacting with the element: ", e)

    #loop though adding vocab and clicking pictures
    def create_game_part_two(self, vocabs):
        try:
            image_library_button_xpath = "//div[@id='question-form']//button[@type='button']"
            image_library_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, image_library_button_xpath))
            )
            image_library_button.click()

            image_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "web-lib"))
            )
            image_button.click()
            sleep(6)

            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'close-gif'))
            )
            close_button.click()

            for vocab in vocabs:
                if vocab:
                    print(vocab)
                    self.questions_search_loop(vocab)

            close_game = "//a[@class='btn btn-defaulted']"

            # Use WebDriverWait to wait for the element to be clickable
            make_game = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, close_game))
            )
            make_game.click()

        except WebDriverException as e:
            print("Exception occurred while interacting with the element: ", e)

    def questions_search_loop(self, vocabs):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "problem"))
        )
        input_box.click()
        input_box.clear()
        input_box.send_keys('What is it?')

        vocab_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "solution1"))
        )
        vocab_box.click()
        vocab_box.clear()
        vocab_box.send_keys(vocabs)

        image_library_button_xpath = "//div[@id='question-form']//button[@type='button']"
        image_library_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, image_library_button_xpath))
        )

        # Click the button
        image_library_button.click()
        # is it needed?
        sleep(3)
        # need to add something here to try again if time runs out
        try:
            first_image = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(1) img.giphy-gif-img.giphy-img-loaded"))
            )
            first_image.click()
        except:
            try:
                fifth_image = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(5) img.giphy-gif-img.giphy-img-loaded"))
                )
                fifth_image.click()
            except:
                self.close_reopen()
            print('Couldnt click first pic. Had to close and reopen')

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tally"))
        )
        save_button.click()

    def close_reopen(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'close-gif'))
            )
            close_button.click()

            image_library_button_xpath = "//div[@id='question-form']//button[@type='button']"
            image_library_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, image_library_button_xpath))
            )

            image_library_button.click()

            try:

                first_image = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(1) img.giphy-gif-img.giphy-img-loaded"))
                )
                first_image.click()

            except:
                fifth_image = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(5) img.giphy-gif-img.giphy-img-loaded"))
                )
                fifth_image.click()
        except WebDriverException as e:
            print("Exception occurred while closing the popup: ", e)

    def create_bamboozle(self, url, EMAIL, PASSWORD, title, vocabs):
        self.sign_in(url, EMAIL, PASSWORD)
        self.create_game(title)
        self.create_game_part_two(vocabs)
        session.clear()

    def create_quiz(self, vocab_words, API_KEY, max_tokens=550):
        response = generate_esl_quiz(vocab_words, API_KEY, max_tokens=550)
        create_a_word_document(response)
        send_email_with_attachment()


    def close(self):
        self.driver.quit()


@app.route('/', methods=['GET', 'POST'])
def book_unit():
    books, units = db_1.some_function()
    if request.method == 'POST':
        if request.form['action'] == 'bamboozle':
            vocab_words = request.form.get('vocab')
            vocabs = vocab_words.split(', ')

            title = session['title']
            if not vocab_words:
                return render_template('book_unit.html', error="Vocabulary is required.", books=books, units=units)
            else:
                local_driver = Driver()
                print(vocabs)
                thread = threading.Thread(target=local_driver.create_bamboozle,
                                          args=(url, EMAIL, PASSWORD, title, vocabs))
                # thread.start()
                return render_template('book_unit.html', vocab=vocab_words, books=books, units=units)

        elif request.form['action'] == 'reviewQuiz':
            vocabs = request.form.get('vocab')
            if not vocabs:
                return render_template('book_unit.html', error="Vocabulary is required.", books=books, units=units)

            print(vocabs)
            local_driver = Driver()
            quiz_thread = threading.Thread(target=local_driver.create_quiz, args=(vocabs, API_KEY, 550))
            # quiz_thread.start()

            return render_template('book_unit.html', vocab=vocabs, books=books, units=units)





        elif request.form['action'] == 'ShowVocab':
            try:
                book = request.form['bookName']
                unit = request.form['unitNumber']
                title = book + ' Unit ' + unit
                session['title'] = title
                book_name, new_vocab = db_1.get_vocab(book, unit)

                # Append new vocab to the temporary vocab list
                existing_vocab = request.form.get('vocab', '')

                # Combine existing and new vocab
                combined_vocab = existing_vocab + ', ' + ', '.join(new_vocab) if existing_vocab else ', '.join(new_vocab)

                return render_template('book_unit.html', vocab=combined_vocab, books=books, units=units)

            except KeyError:
                return render_template('book_unit.html')

        # Render the page for a GET request or if no form data is submitted
        return render_template('book_unit.html')

    # Render the page for a GET request or if no form data is submitted
    return render_template('book_unit.html', book_to_units=book_to_units)


@app.route('/success', methods=['GET'])
def success_page():
    return render_template('success.html')

@app.route('/login_failure', methods=['GET'])
def failure():
    return render_template('login_failure.html')

url = 'https://www.baamboozle.com/games/create'


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
             f"It should be 1 page in total. ONLY gap fill and an easy comprehension. Dont give the answers" \
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

Billy went to visit his Grandma who lives in a small village in the countryside. It has mountains and a beautiful river. Every morning, Billy would exercise by running along a path that passed through apple trees. One day, he decided to take an adventurous trip alone. Walking along the path, he saw a cable car station. Billy took the cable car up the mountain, where he found a waterfall. Billy took back many stories to tell his friends in the city about his village adventure.

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


def create_a_word_document(text):
    doc = Document()
    doc.add_paragraph(text)
    filename = 'word_doc.docx'
    doc.save(filename)
    print(f"Document saved as {filename}")

def send_email_with_attachment():
    send_from = E_NAME
    password = E_PASS
    send_to = E_NAME
    subject = f'Quiz'
    body = ':)'
    file_path = 'C:\\Users\\PC\\Desktop\\pythonProject\\Bamboozle_ESL-game\\word_doc.docx'
    server = None
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(send_from, password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Open the file to be sent
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(file_path))
            msg.attach(part)

        # Send the email
        server.send_message(msg)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if server:
            server.quit()

        # Attempt to delete the file
        try:
            print("Deleting the document...")
            os.remove(file_path)
            print(f"Document {file_path} deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")


if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)



#should work. Errors for making game and quiz included. Need to make errors for searching DB
