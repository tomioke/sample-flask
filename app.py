# Library
from flask import Flask, render_template

# Init
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('stats.html')