#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    nums = []
    for i in range(parameter):
        nums.append(f'{i}\n')
    return ''.join(nums)

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == "div":
        divide = int(num1) / int(num2)
        return f"{divide}"
    elif operation == "*":
        multiply = int(num1) * int(num2)
        return f"{multiply}"
    elif operation == "-":
        subtract = int(num1) - int(num2)
        return f"{subtract}"
    elif operation == "+":
        sum = int(num1) + int(num2)
        return f"{sum}"
    elif operation == "%":
        remainder = int(num1) % int(num2)
        return f"{remainder}"