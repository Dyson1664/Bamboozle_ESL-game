from flask import Flask, render_template, request, redirect, url_for, session
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, ElementClickInterceptedException

from dotenv import load_dotenv
import os
from selenium import webdriver
from time import sleep
load_dotenv()

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        session_data = {'title': request.form['title']}
        for i in range(1, 17):
            session_data.update(
                {f'vocab{i}': request.form[f'vocab{i}'] for i in range(1, 17) if request.form[f'vocab{i}'].strip()})
        session['data'] = session_data
        return redirect(url_for('create_game_route'))
    return render_template('index.html')

class Driver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(r'C:\Users\PC\Downloads\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def sign_in(self, url, email, password):
        self.driver.get(url)
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        sign_in_button.click()

    def create_game(self, title):
        title_box = self.driver.find_element(By.ID, 'one')
        title_box.send_keys(title)

        description_box = self.driver.find_element(By.ID, 'two')
        description_box.send_keys(title)

        make_game_button = self.driver.find_element(By.ID, 'five')
        make_game_button.click()
        sleep(5)

    def create_game_part_two(self, vocabs):
        print('1')

        # Wait for the button to be clickable using the XPath
        image_library_button_xpath = "//div[@id='question-form']//button[@type='button']"
        image_library_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, image_library_button_xpath))
        )

        # Click the button
        image_library_button.click()

        print('3')
        image_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "web-lib"))
        )
        image_button.click()
        print('4')
        sleep(6)


        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'close-gif'))
        )
        close_button.click()
        print('5')
        sleep(5)
        for val in vocabs:
            if val:
                questions_search_loop(self, val)
            print('7')

        close_game = "//a[@class='btn btn-defaulted']"

        # Use WebDriverWait to wait for the element to be clickable
        make_game = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, close_game))
        )
        make_game.click()






    def close(self):
        self.driver.quit()

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
    sleep(3)
#need to add something here to try again if time runs out
    try:
        fifth_image = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(5) img.giphy-gif-img.giphy-img-loaded"))
        )
        fifth_image.click()
    except:
        close_reopen(self)
        print('Had to close and reopen')




    save_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "tally"))
    )
    save_button.click()
    sleep(2)
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

        # Click the button
        image_library_button.click()
        sleep(5)

        fifth_image = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.giphy-gif:nth-of-type(5) img.giphy-gif-img.giphy-img-loaded"))
        )
        fifth_image.click()
    except WebDriverException as e:
        print("Exception occurred while closing the popup: ", e)


# driver = Driver()
@app.route('/create_game', methods=['GET'])
def create_game_route():
    data = session.get('data', {})
    if not data:
        # Redirect to home if there's no data in session
        return redirect(url_for('run'))

    # Initialize the driver within the function scope
    local_driver = Driver()

    title = data.get('title')
    vocabs = [data.get(f'vocab{i}', '') for i in range(1, 17)]


    # Sign in and create the game
    try:
        local_driver.sign_in(url, EMAIL, PASSWORD)
        local_driver.create_game(title)
        print('hi')
        local_driver.create_game_part_two(vocabs)
        return redirect(url_for('success_page'))
    except Exception as e:
        print(e)  # For debugging purposes, print the exception
        # Handle login failure, perhaps by redirecting to a login failure page
        return redirect(url_for('failure'))



@app.route('/success', methods=['GET'])
def success_page():
    return render_template('success.html')

@app.route('/login_failure', methods=['GET'])
def failure():
    return render_template('login_failure.html')

url = 'https://www.baamboozle.com/games/create'


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Try a different port like 5001

#got as far as for loop doesnt seem to work yet. Check why