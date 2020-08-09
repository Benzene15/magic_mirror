from flask import Flask, render_template
import atexit
import API_2020

app = Flask(__name__)


@app.route('/')
def index():
    temp,days,quote=API_2020.main()
    return render_template('index.html',temp=temp, days=days,quote=quote)