from datetime import datetime as dt

# def input_logger(num1, num2, op):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};number1;{}\n'
#                         .format(time, num1))
#         file.write('{};operator;{}\n'
#                         .format(time, op))
#         file.write('{};number2;{}\n'
#                         .format(time, num2))

# def result_logger(result):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};result = ;{}\n'
#                         .format(time, result))
def logger(text):
    with open('log.txt', 'a') as data:
        data.write(str(text)+'\n')

def logger_out():
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'r') as data:
        print(time, data.readlines())
