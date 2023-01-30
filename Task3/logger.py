from datetime import datetime as dt


def log_input_data(text):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}:{}\n'
                   .format(time, str(text)))


def log_output_data_term():
    log_input_data('Logging journal preview requested by user')
    with open('log.txt', 'r') as data:
        print(*data.readlines())
    log_input_data('Logging journal printed in terminal')


def log_output_data_csv():
    log_input_data('Logging journal unload in .csv file requested by user')
    with open('log.csv', 'w') as file:
        with open('log.txt', 'r') as data:
            data = data.readlines()
            file.writelines(data)
    log_input_data('Logging journal unload in .csv file')
