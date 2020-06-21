from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def base_context():
    return {
        'now': datetime.utcnow()
    }

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
