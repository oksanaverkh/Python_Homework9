import logger as log    

def get_data():
    a = input('Enter a number: ')
    op = input('Enter an operator: ')
    b = input('Enter a number: ')
    log.logger(a+op+b)

    if 'j' in a:
        a = complex(a)
    if 'j' in b:
        b = complex(b)
    else:
        a = int(a)
        b = int(b)
    # log.input_logger(a, b, op)

    return a, b, op

def set_data(data):
    print(f'Result = {data}')
    log.logger(data)


