from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        return render_template('success.html')
    else:
        return render_template('index.html')


@app.route('/sign_in')
def login():
    pass


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('login_failure.html')

@app.route('/run')
def run():
    # your code here
    return render_template('login_failure.html')

@app.route('/login')
def profile(username):
    pass

with app.test_request_context():
    print(url_for('page'))  # Output: '/'
    print(url_for('failure'))  # Output: '/login'
    print(url_for('profile', username='john_doe'))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
