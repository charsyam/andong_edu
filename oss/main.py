from flask import Flask

from andong_edu import AndongEdu
from edu_exceptions import *

app = Flask(__name__)
edu = AndongEdu()

@app.route('/hello/<name>')
def hello_world(name):
    return edu.hello(name)

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    raise NotImplementedError("Not Implemented")

@app.route('/minus/<num1>/<num2>')
def minus(num1, num2):
    raise NotImplementedError("Not Implemented")

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    raise NotImplementedError("Not Implemented")

@app.route('/divide/<num1>/<num2>')
def divide(num1, num2):
    raise NotImplementedError("Not Implemented")

@app.route('/factorial/<num1>')
def factorial(num):
    raise NotImplementedError("Not Implemented")
