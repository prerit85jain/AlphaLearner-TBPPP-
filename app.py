from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feature')
def features():
    return render_template('features.html')


@app.route('/practice')
def prac():
    return render_template('practice.html')

users = {
    "ajay@alpha.com": {
        "name": "Ajay",
        "dob": "01-07-2006",
        "password": "Password123"
    },
    "akash@alpha.com": {
        "name": "Akash",
        "dob": "01-08-2005",
        "password": "Password456"
    }
}
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        dob = request.form['dob']
        password = request.form['password']
        if email in users:
            return "User already exists!"
        else:
            users[email] = {'name': name, 'dob': dob, 'password': password}
            return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            session['user'] = email
            return redirect(url_for('features'))
        return "Invalid credentials!"
    return render_template('signin.html')

@app.route('/traing_data')
def train_data():
    return render_template('train_data.html')

if __name__ == "__main__":
    app.run(debug = True)