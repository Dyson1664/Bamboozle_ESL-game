from flask import Flask, render_template, request, redirect, url_for, session
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        session_data = {'title': request.form['title']}
        for i in range(1, 17):
            session_data[f'vocab{i}'] = request.form[f'vocab{i}']
        session['data'] = session_data
        return redirect(url_for('create_game_route'))
    return render_template('index.html')

@app.route('/create_game', methods=['GET', 'POST'])
def create_game_route():
    data = session.get('data', {})
    title = data.get('title')
    vocabs = [data.get(f'vocab{i}') for i in range(1, 17)]
    create_game(title, vocabs)
    return redirect(url_for('success_page'))  # You need to define a success_page route

def create_game(title, vocabs):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(r'C:\Users\PC\Downloads\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    sign_in(driver)
    # Assume you have a function to enter the title and vocab on the page after sign in
    # Example: enter_game_details(driver, title, vocabs)

def sign_in(driver):
    driver.get('https://www.example.com/login')  # Replace with the actual sign-in page
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("your_email@example.com")  # Replace with your actual email
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("your_password")  # Replace with your actual password
    sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    sign_in_button.click()

# Define other routes and functions as necessary

if __name__ == '__main__':
    app.run(debug=True)

