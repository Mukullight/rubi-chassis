from flask import Flask, request, render_template, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask app created on October 19, 2025.</p>'

if __name__ == '__main__':
    app.run(debug=True)