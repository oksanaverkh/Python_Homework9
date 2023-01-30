from calculation import calc
from user_interface import get_data as gd
from user_interface import set_data as sd
import logger as log 

def button_click():
    number1, number2, operator = gd()
    result = calc(number1, number2, operator)
    sd(result)
    # log.result_logger(result)
    log.logger(result)
    return result
