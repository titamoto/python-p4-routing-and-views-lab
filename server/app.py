#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    list = [i for i in range(integer)]
    string = ''
    for el in list:
       string += f'{el}\n'
    return f'{string}'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = int(num1) + int(num2)
        return f'{result}'
    if operation == '-':
        result = int(num1) - int(num2)
        return f'{result}'
    if operation == '*':
        result = int(num1) * int(num2)
        return f'{result}'
    if operation == '%':
        result = int(num1) % int(num2)
        return f'{result}'
    if operation == 'div':
        result = int(num1) / int(num2)
        return f'{result}'

