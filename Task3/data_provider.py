import logger as log


def import_contact_from_file(filename):
    with open('phonebook.txt', 'a') as file:
        with open(filename, 'r') as data:
            data = data.readlines()
            file.writelines(f'{data[0]}')
            file.writelines(data[1])
            file.writelines(data[2])
            file.writelines(f'{data[3]}\n')
    log.log_input_data('New contact imported from a file')


def add_contact_manually(contact_name):
    with open('phonebook.txt', 'a') as file:
        file.write(f'{contact_name}\n')
    log.log_input_data('New contact added')
