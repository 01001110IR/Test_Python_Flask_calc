from flask import Flask, render_template, request
import random
from tools.numbers.col import myzip
from tools.numbers.simp import add, add2
from tools.numbers.comp import  print_number_and_reverse, sum_of_digits
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return str(result)

@app.route('/2', methods=['GET'])
def subtract_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 - num2
    return str(result)

@app.route('/3', methods=['GET'])
def check_palindrome():
    user_input = request.args.get('input_string', '')
    result = print_number_and_reverse(user_input)
    return str(result)


@app.route('/4', methods=['GET'])
def sum_digits():
    user_input = int(request.args.get('input_number', 0))
    result = sum_of_digits(user_input)
    return str(result)

@app.route('/5', methods=['GET'])
def zip_example():
    iterable1 = request.args.getlist('iterable1')
    iterable2 = request.args.getlist('iterable2')
    
    if len(iterable1) != len(iterable2):
        return "Error: The two lists must have the same length."

    zipped = list(zip(iterable1, iterable2))
    result = ', '.join(str(pair) for pair in zipped)
    return result

if __name__ == '__main__':
    app.run(debug=True, port=7000)
