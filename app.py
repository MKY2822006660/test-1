from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulate a database with a dictionary
users = {}

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return redirect(url_for('main_page_loader'))  # Redirect after successful sign-in
        else:
            return "Incorrect email or password. Try again."
    return render_template('index.html')  # Sign-in page

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if email in users:
            return "User already exists!"
        users[email] = password
        return redirect(url_for('main_page_loader'))  # Redirect after successful sign-up
    return render_template('sign-up.html')  # Sign-up page

@app.route('/main_page_loader')
def main_page_loader():
    return render_template('sign-up-and-log-in-loader-to-main-page.html')  # Redirects here after sign-in or sign-up

if __name__ == '__main__':
    app.run(debug=True, port=5001)
