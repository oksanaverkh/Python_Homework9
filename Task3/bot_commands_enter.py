import logger as log    
from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext):
    await log.logger('User starts the program')
    await update.message.reply_text(f'''Choose an operation: 
        finding a contact - enter /find,
        addition of a new contact - enter /add,
        export of a phonebook - enter /export,
        logger journal unload - enter /load''')
    user_input = update.message.text
    await log.logger('User chose an operation')
    await log.log(update, context)
    

async def add_contact(update: Update, context: CallbackContext):
    await log.logger('Contact addition requested by user')
    await update.message.reply_text('Enter a surname: ')
    await update.message.reply_text('Enter a name: ')
    await update.message.reply_text('Enter a phone number: ')
    await update.message.reply_text('Enter description: ')
    text = update.message.text.split()
    surname = text[1]
    name = text[2]
    telephone = text[3]
    description = text[4]
    contact = 'Surname: '+surname+'\n'+'Name: '+name + '\n' + \
        'Telephone: '+telephone+'\n'+'Comment: '+description+'\n'
    with open('Task3\phonebook.txt', 'a') as file:
        file.write(f'{contact}\n')
    await update.message.reply_text(f'Contact {contact} added to the phonebook')
    await log.logger('New contact added')
    await log.log(update, context)
   





