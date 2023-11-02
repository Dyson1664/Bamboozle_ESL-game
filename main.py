from flask import Flask, render_template, request, redirect, url_for, session
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        # Capture form data and store in session
        session_data = {'title': request.form['title']}
        for i in range(1, 17):
            session_data[f'vocab{i}'] = request.form[f'vocab{i}']
        session['data'] = session_data
        # Now you can use the data with any function you want
        vocab = split_data(session_data)
        print_vocab(vocab)
        # Redirect or render a template as needed
        return redirect(url_for('display'))
    return render_template('index.html')

#returns a list the title as a list and a list of all animal names or vocab names
def split_data(session_data):
    title = session_data.get('title')
    vocabs = [session_data.get(f'vocab{i}') for i in range(1, 17)]
    return [title], vocabs


def print_vocab(vocab):
    for v in vocab:
        print(v)

@app.route('/p')
def display():
    # Retrieve data from session to pass to the template
    data = session.get('data', {})
    return render_template('display.html', data=data)



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(r'C:\Users\PC\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

def sign_in(driver):
    # Navigate to the webpage
    driver.get('https://www.baamboozle.com/games/create') # Replace with your actual URL

    # Locate email input box and enter email
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("teacher1@cec.com.vn")  # Replace with the email you want to enter

    # Locate password input box and enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("cec.com.vn")  # Replace with the password you want to enter

    # Locate the submit button and click it
    sign_in_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-block.btn-primaryed[type='submit']")
    sign_in_button.click()

def create_game(driver, title):
    enter_title = driver.find_element(By.ID, 'one')
    enter_title.send_keys(str(title))


# title, vocabs = split_data()
# create_game(driver, title)

if __name__ == '__main__':
    app.run(debug=True)
