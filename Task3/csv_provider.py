from data_display import show_phonebook
import logger as log


def create_csv():
    log.log_input_data('Phonebook preview in csv-format reguested by user')
    with open('phonebook.csv', 'w') as file:
        for i in range(len(show_phonebook())):
            data = (show_phonebook())[i]
            file.write(data)
    log.log_input_data('File .csv unloaded')
