import controller as c
import logger


user_input = input('Calculation - 1, log_output - 2')
if user_input =='1':
    c.button_click()
else:
    logger.logger_out()

