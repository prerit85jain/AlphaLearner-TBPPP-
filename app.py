from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feature')
def features():
    return render_template('features.html')


@app.route('/practice')
def prac():
    return render_template('practice.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/traing_data')
def train_data():
    return render_template('train_data.html')

if __name__ == "__main__":
    app.run(debug = True)