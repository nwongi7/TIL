from flask import Flask, render_template, send_file, request
from datetime import datetime as dt
import random

app = Flask(__name__)

hogu = []

@app.route("/") #주문 받는 방법(요청을 받는 방법)
def index():
    #return str(random.sample(range(1,46),6))
    #return send_file('home.html')
    lotto = random.sample(range(1,46),6)
    return render_template('index.html', lotto = lotto)

@app.route("/hello/<name>")
def hello(name):
    return "hello, {}".format(name)

@app.route("/cube/<num>")
def cube(num):
    return str((int(num))**3)

#@app.route("/power/<num>_<num2>")
#def power(num,num2):
#    return str(int(num) ** int(num2))

@app.route("/reverse/<word>")
def reverse(word):
    return word[::-1]

@app.route("/ispaln/<word>")
def ispaln(word):
    return str(word == word[::-1])
    # 삼항연산자
    # return "True" if word == word[::-1] else "False"

@app.route("/isitnewyear")
def isitnewyear():
    if dt.now().month == dt.now().day == 1:
        return "예"
    else:
        return "아니오"

@app.route("/goonghap")
def goonghap():
    me = request.args.get('me')
    you = request.args.get('you')

    hogu.append([me,you])
    rating = random.randint(60,99)
    return render_template('goonghap.html',me=me,you=you,rating=rating)

@app.route("/god")
def god():
    return str(hogu)