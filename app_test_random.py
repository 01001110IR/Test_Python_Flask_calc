from flask import Flask, render_template
import random
from tools.numbers.col import myzip
from tools.numbers.simp import add, add2
from tools.numbers.comp import  print_number_and_reverse, sum_of_digits

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def add_random():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = add(num1, num2)
    return f"Addition Result: {num1} + {num2} = {result}"

@app.route('/2')
def subtract_random():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = add2(num1, num2)
    return f"Subtraction Result: {num1} - {num2} = {result}"


@app.route('/3')
def check_random_palindrome():
    random_number = random.randint(1, 1000)  
    result = print_number_and_reverse(random_number)
    return result  

@app.route('/4')
def sum_random_digits():
    random_number = random.randint(1, 10000) 
    result = sum_of_digits(random_number)  
    return result


@app.route('/5')
def zip_example():
    iterable1 = [1, 2, 3]
    iterable2 = ['a', 'b', 'c']
    zipped = list(myzip(iterable1, iterable2))
    result = ', '.join(str(pair) for pair in zipped)

    return f"Zipped Result: {result}"

if __name__ == '__main__':
    app.run(debug=True,port=7000)





