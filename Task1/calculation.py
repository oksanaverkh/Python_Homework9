# from user_interface import get_data as gd
import logger as lg   

def calc(num1, num2, operator):
    result = 0
    lg.logger(f'Calculation in progress {num1} {operator} {num2}')
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    # lg.logger(result)
    return result


