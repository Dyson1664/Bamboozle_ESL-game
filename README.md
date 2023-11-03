# ESL Game Creator Bot for Bamboozle

This bot automates the creation of ESL (English as a Second Language) games on the Bamboozle website through a Flask web server and Selenium WebDriver.

## Features

- User authentication on the Bamboozle website.
- Game creation with custom titles and vocabularies.
- Exception handling for robust automation.

## Prerequisites

- Python 3.6 or higher
- Flask
- Selenium WebDriver
- ChromeDriver compatible with the installed Chrome version

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Dyson1664/Bamboozle_ESL-game.git
   
2. pip install -r requirements.txt
   
3. Set environment variables for credentials:
   export EMAIL='your_email@example.com'
   export PASSWORD='your_password'

## Configuration
- Update the path to chromedriver.exe in the Driver class if necessary.
- Set a secure app.secret_key for session management in Flask.
