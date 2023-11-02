# from flask import Flask, render_template, request, redirect, url_for, session
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
#
#
#
#
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# service = Service(r'C:\Users\PC\Downloads\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# driver.get('https://www.google.com/')

fruit_dictionary = {
    'vocab1': 'apple',
    'vocab2': 'banana',
    'vocab3': 'cherry',
    'vocab4': 'date',
    'vocab5': 'elderberry',
    'vocab6': 'fig',
    'vocab7': 'grape',
    'vocab8': 'honeydew',
    'vocab9': 'ivy',
    'vocab10': 'jackfruit',
    'vocab11': 'kiwi',
    'vocab12': 'lemon',
    'vocab13': 'mango',
    'vocab14': 'nectarine',
    'vocab15': 'orange',
    'vocab16': 'papaya'
}

for num, val in enumerate(fruit_dictionary.values(), start=1):
    print(num, val)


list4 = ['apple', 'dog', 'cat', '', '']
for val in list4:
    if val:
        print(val)
        print('i')
