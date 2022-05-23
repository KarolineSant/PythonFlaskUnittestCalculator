from flask import Flask, render_template, request
import math
import unittest

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

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        if operation == "+":
            result = math.sqrt(input1)

        elif operation == "-":
            result = input1 ** input2

        elif operation == "*":
            math.log(input1) 

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Você não pode dividir por zero."
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Você não pode realizar um calculo numérico com esses dados"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()