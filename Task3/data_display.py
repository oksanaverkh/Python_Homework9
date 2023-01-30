import logger as log


def find_contact_in_phonebook(last_name):
    with open('phonebook.txt', 'r') as data:
        data = data.read().split('\n')
        for i in range(len(data)):
            if f'Surname: {last_name}' in data[i]:
                print(str('\n'+data[i]+'\n'+data[i+1] +
                      '\n'+data[i+2]+'\n'+data[i+3]))
    log.log_input_data('Provided info about contact')


def show_phonebook():
    log.log_input_data('Phonebook preview requested by user')
    with open('phonebook.txt', 'r') as data:
        data = data.readlines()
    log.log_input_data('Phonebook unloaded')
    return data
