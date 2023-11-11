from flask import Flask, render_template, request, redirect, url_for, session
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

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')

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
    def create_game(self, title):
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

    def close(self):
        self.driver.quit()


@app.route('/', methods=['GET', 'POST'])
def book_unit():
    if request.method == 'POST':
        # Check for vocabulary list submission
        if 'vocabList' in request.form:
            vocab_list = request.form['vocabList']
            print(vocab_list)
            # Process the vocabulary list
            # ... (your code to handle vocab list)

            # Store the processed vocab list in the session temporarily
            session['processed_vocabs'] = vocab_list

            # Re-render the same page without redirecting
            return render_template('book_unit.html',
                                   message="Vocabulary list processed. Please submit the book form to continue.")

        # Check for book form submission
        if 'bookName' in request.form and 'unitNumber' in request.form:
            try:
                book_name = request.form['bookName']
                unit_number = request.form['unitNumber']
                # query db
                title, vocabs = db_1.get_vocab(book_name, unit_number)

                # Here, use the processed vocabs from the session if available
                processed_vocabs = session.get('processed_vocabs', vocabs)

                # Store retrieved data in session.
                session['title'] = title
                session['vocabs'] = processed_vocabs

                # Clear the processed vocabs from the session
                session.pop('processed_vocabs', None)

                # Redirect to the page to show the populated vocabulary form.
                return redirect(url_for('show_vocab'))
            except KeyError:
                # Render the book_unit page with an error if the form fields are not found.
                return render_template('book_unit.html', error="Please fill in all the fields.")

    # Render the page for a GET request or if no form data is submitted
    return render_template('book_unit.html')


@app.route('/', methods=['GET', 'POST'])
def book_unit():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        # Check for vocabulary list submission
        if form_type == 'vocab_form':
            vocab_list = request.form.get('vocabList')
            print(vocab_list)
            # Process the vocabulary list
            # ... (your code to handle vocab list)

            # Store the processed vocab list in the session temporarily
            session['processed_vocabs'] = vocab_list

            # Re-render the same page without redirecting
            return render_template('book_unit.html',
                                   message="Vocabulary list processed. Please submit the book form to continue.")

        # Check for book form submission
        elif form_type == 'book_form':
            try:
                book_name = request.form['bookName']
                unit_number = request.form['unitNumber']
                # query db
                title, vocabs = db_1.get_vocab(book_name, unit_number)

                # Here, use the processed vocabs from the session if available
                processed_vocabs = session.get('processed_vocabs', vocabs)

                # Store retrieved data in session.
                session['title'] = title
                session['vocabs'] = processed_vocabs

                # Clear the processed vocabs from the session
                session.pop('processed_vocabs', None)

                # Redirect to the page to show the populated vocabulary form.
                return redirect(url_for('show_vocab'))
            except KeyError:
                # Render the book_unit page with an error if the form fields are not found.
                return render_template('book_unit.html', error="Please fill in all the fields.")

    # Render the page for a GET request or if no form data is submitted
    return render_template('book_unit.html')


@app.route('/go')
def go():
    if 'title' in session and 'vocabs' in session:
        title = session['new_title']
        vocabs = session['new_vocabs']
        # load bot
        local_driver = Driver()
        try:
            local_driver.sign_in(url, EMAIL, PASSWORD)
            local_driver.create_game(title)
            local_driver.create_game_part_two(vocabs)
            return redirect(url_for('success_page'))
        except Exception as e:
            print(e)
            # Handle login failure
        return render_template('success.html')
    else:
        return redirect(url_for('book_unit'))

@app.route('/success', methods=['GET'])
def success_page():
    return render_template('success.html')

@app.route('/login_failure', methods=['GET'])
def failure():
    return render_template('login_failure.html')

url = 'https://www.baamboozle.com/games/create'



if __name__ == '__main__':
    app.run(debug=True, port=5001)






import openai

def generate_esl_quiz(prompt, api_key):
    """
    Function to generate an ESL quiz using OpenAI's GPT-4 API.

    Parameters:
    prompt (str): The prompt describing the quiz requirements.
    api_key (str): Your OpenAI API key.

    Returns:
    str: The generated quiz text.
    """
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Replace with the model you are using, if different.
            prompt=prompt,
            max_tokens=150  # Adjust as needed for the length of quiz desired.
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
# quiz_prompt = "Create a beginner ESL quiz about daily routines."
# my_api_key = "your-api-key-here"
# quiz = generate_esl_quiz(quiz_prompt, my_api_key)
# print(quiz)