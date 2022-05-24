from flask import Flask, render_template, request
import math

Flask_App = Flask(__name__)

@Flask_App.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])

def operation_result():

    error = None
    result = None

    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    operation = request.form['operation']

    input1 = float(first_input)
    input2 = float(second_input)

    if operation == "sqrt":
        result = math.sqrt(input1)

    elif operation == "pow":
        result = math.pow(input1, input2)

    elif operation == "log":
        math.log(input1) 

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()

