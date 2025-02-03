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

if __name__ == "__main__":
    app.run(debug = True)