
def check_input_1():
    number = input()
    while not number in '1234':
        print('Wrong value, try again')
        number = input()
    return number


def check_input_2():
    number = input()
    while not number in '12':
        print('Wrong value, try again')
        number = input()
    return number


def check_input_3():
    number = input()
    while not number in '123':
        print('Wrong value, try again')
        number = input()
    return number


def check_filepath():
    path = input()
    while not '.' in path:
        print('Wrong value, try again')
        path = input()
    return path


def check_text():
    text = input()
    while not text.isalpha():
        print('Wrong input, try again')
        text = input()
    return text
