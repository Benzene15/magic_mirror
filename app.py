from flask import Flask, render_template
import API_2020

app = Flask(__name__)


@app.route('/')
def index():
    temp,days,quote=API_2020.main()
    return render_template('index.html',days=days,quote=quote)