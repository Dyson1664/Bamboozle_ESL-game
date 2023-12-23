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
import db_5
import openai
from docx import Document
from word_search_generator import WordSearch
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
print(API_KEY)
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
        title, vocabs = db_5.get_vocab(name, unit)
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

    def create_quiz(self, API_KEY, vocab_words, max_tokens=550):
        response = generate_esl_quiz(API_KEY, vocab_words, max_tokens=550)
        create_a_word_document(response)
        send_email_with_attachment(r'C:\Users\PC\Desktop\work_webpage\Bamboozle_ESL-game\word_doc.docx')

    def create_word_search2(self, vocab):
        puzzle = create_word_search(vocab)
        send_email_with_attachment(puzzle)

    def close(self):
        self.driver.quit()

# main webpage
@app.route('/', methods=['GET', 'POST'])
def book_unit():
    book_to_units = db_5.some_function()
    books = db_5.get_all_books()
    books.sort()
    kg_vocab = db_5.make_kg_dict()
    selected_book = session.get('selected_book', '')
    selected_unit = session.get('selected_unit', '')
    combined_vocab = ''

    if request.method == 'POST':
        selected_book = request.form.get('bookName')
        selected_unit = request.form.get('unitNumber')
        session['selected_book'] = selected_book
        session['selected_unit'] = selected_unit

        if request.form['action'] == 'bamboozle':
            vocab_words = request.form.get('vocab')
            vocabs = vocab_words.split(', ') if vocab_words else []

            title = session.get('title', '')
            if not vocabs:
                return render_template('book_unit.html', error="Vocabulary is required.", books=books, book_to_units=book_to_units, selected_book=selected_book, selected_unit=selected_unit)

            local_driver = Driver()
            print(vocabs)
            thread = threading.Thread(target=local_driver.create_bamboozle,
                                      args=(url, EMAIL, PASSWORD, title, vocabs))
            thread.start()
            return render_template('book_unit.html', vocab=vocab_words, books=books, book_to_units=book_to_units, kg_vocab=kg_vocab, selected_book=selected_book, selected_unit=selected_unit)

        elif request.form['action'] == 'reviewQuiz':
            vocabs = request.form.get('vocab')
            if not vocabs:
                return render_template('book_unit.html', error="Vocabulary is required.", books=books, kg_vocab=kg_vocab, book_to_units=book_to_units, selected_book=selected_book, selected_unit=selected_unit)

            local_driver = Driver()
            quiz_thread = threading.Thread(target=local_driver.create_quiz, args=(API_KEY, vocabs, 550))
            quiz_thread.start()

            return render_template('book_unit.html', vocab=vocabs, books=books, book_to_units=book_to_units, kg_vocab=kg_vocab, selected_book=selected_book, selected_unit=selected_unit)

        elif request.form['action'] == 'ShowVocab':

            book = request.form.get('bookName')
            unit = request.form.get('unitNumber')
            kg_category = request.form.get('kgTitle')
            existing_vocab = request.form.get('vocab', '')
            new_combined_vocab = []

            # Fetch vocab for selected book and unit
            if book != 'None':
                _, new_vocab = db_5.get_vocab(book, unit)

                new_combined_vocab.extend(new_vocab)

            # Fetch vocab for selected kindergarten category

            if kg_category != 'NONE':
                kg_vocab_list = kg_vocab.get(kg_category, [])

                new_combined_vocab.extend(kg_vocab_list)

            # Append new vocab to existing vocab

            if existing_vocab:

                combined_vocab = ', '.join(filter(None, [existing_vocab, ', '.join(new_combined_vocab)]))

            else:

                combined_vocab = ', '.join(new_combined_vocab)


            return render_template('book_unit.html', vocab=combined_vocab, books=books, book_to_units=book_to_units, kg_vocab=kg_vocab, selected_book=selected_book, selected_unit=selected_unit)


        elif request.form['action'] == "wordSearch":
            vocabs = request.form.get('vocab')

            local_driver = Driver()
            word_search_thread = threading.Thread(target=local_driver.create_word_search2, args=(vocabs,))
            word_search_thread.start()

            return render_template('book_unit.html', vocab=vocabs, books=books, kg_vocab=kg_vocab, book_to_units=book_to_units,
                                   selected_book=selected_book, selected_unit=selected_unit)

    return render_template('book_unit.html', vocab=combined_vocab, books=books, book_to_units=book_to_units, kg_vocab=kg_vocab, selected_book=selected_book, selected_unit=selected_unit)

@app.route('/success', methods=['GET'])
def success_page():
    return render_template('success.html')

@app.route('/login_failure', methods=['GET'])
def failure():
    return render_template('login_failure.html')

url = 'https://www.baamboozle.com/games/create'


def create_prompt(vocabs):
    return f"""Hello, I need your assistance to create an EASY and I really mean Easy ESL quiz for ten-year-old students using the following vocabulary words: {vocabs}. The quiz should be straightforward, engaging, and designed for beginners. Here's the format I'd like you to follow:

1. **Fill in the Blanks:** 
   - Develop TEN sentences with a blank space for a word from the vocabulary list. 
   - Each sentence should use a different vocabulary word in a context that helps infer its meaning.
   - Ensure the sentences are simple, age-appropriate, and provide enough context clues to guess the missing word.
   - List the vocabulary words at the top of this section for easy reference.

2. **Reading Comprehension:**
   - Write a short, engaging story appropriate for the age group, incorporating some of the vocabulary words.
   - After the story, include FIVE comprehension questions that test the students' understanding of the text and how the vocabulary words are used within it.
   - The story and questions should be simple enough for students at this level to understand without external help.

Please do not include the answers in the quiz. Aim to keep the total length of the quiz to about one page. For clarity, here's a structure outline for your reference:

**Vocabulary Words:** 
{vocabs}

**Fill in the Blanks:**
1. Sentence with a blank using vocab1.
2. Sentence with a blank using vocab2.
... and so on.

**Reading Comprehension:**
[Short story incorporating some of the vocabulary words]

**Comprehension Questions:**
1. Question about the story.
2. Another question about the story.
... and so on."""





def generate_esl_quiz(API_KEY, vocab_words, max_tokens=550):
    # if not vocab_words:
    #     return "Vocabulary list is empty."

    prompt = create_prompt(vocab_words)

    openai.api_key = API_KEY

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


def create_word_search(vocab):
    puzzle = WordSearch(vocab)
    location = puzzle.save(path=r'C:\Users\PC\Desktop\pythonProject\Bamboozle_ESL-game\word_search.pdf')

    return location


def create_a_word_document(text):
    doc = Document()
    doc.add_paragraph(text)
    filename = 'word_doc.docx'
    doc.save(filename)
    print(f"Document saved as {filename}")

def send_email_with_attachment(file_path):
    send_from = E_NAME
    password = E_PASS
    send_to = E_NAME
    subject = f'Quiz'
    body = ':)'
    # file_path = 'C:\\Users\\PC\\Desktop\\pythonProject\\Bamboozle_ESL-game\\word_doc.docx'
    file_path = file_path
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
#need to pull then edit changes
#needs to be deleted tomorrow

