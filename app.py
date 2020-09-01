from flask import Flask, render_template
import atexit
import time
import API_2020

app = Flask(__name__)


@app.route('/')
def index():
    temp=API_2020.weather()
    days=API_2020.calc_days()
    quote=API_2020.random_quote()
    date_time=API_2020.date_time()
    w_label="http://openweathermap.org/img/wn/"+str(temp['weather'][0]['icon'])+"@2x.png"
    sunset=API_2020.calc_suntime(temp['sys']['sunset'])
    sunrise=API_2020.calc_suntime(temp['sys']['sunrise'])
    return render_template('index.html',temp=temp, days=days,quote=quote,date_time=date_time,w_label=w_label, sunset=sunset, sunrise=sunrise)