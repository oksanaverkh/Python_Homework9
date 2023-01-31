import logger as log    
from telegram import Update
from telegram.ext import CallbackContext

async def find_contact(update: Update, context: CallbackContext):
    await log.logger('Info about contact requested by user')
    await update.message.reply_text('Enter a surname: ')   
    text = update.message.text.split()
    surname = text[1]
    with open('Task3\phonebook.txt', 'r') as data:
        data = data.read().split('\n')
        for i in range(len(data)):
            if f'Surname: {surname}' in data[i]:
                await update.message.reply_text(f"{data[i]}'\n'{data[i+1]}'\n'{data[i+2]}'\n'{data[i+3]}")
    await log.logger('Provided info about contact')
    await log.log(update, context)

async def export_phonebook(update: Update, context: CallbackContext):
    await log.logger('User chose export of the phonebook')
    await update.message.reply_text(f'''Choose a format: 
        export in .txt format - enter /txt,
        export in .csv format - enter /csv,
        in message - enter /here''')
    user_input = update.message.text
    await log.logger('User chose an export format')
    await log.log(update, context)

async def export_phonebook_txt(update: Update, context: CallbackContext):
    await log.logger('Export of the phonebook in .txt format requested by user')
    await log.log(update, context)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('Task3/phonebook.txt', 'rb'))
    await log.logger('Phonebook.txt unloaded')

async def export_phonebook_csv(update: Update, context: CallbackContext):
    await log.logger('Export of the phonebook in .csv format requested by user')
    await log.log(update, context)
    with open('Task3/phonebook.csv', 'w') as file:
        with open('Task3/phonebook.txt', 'r') as data:
            data = data.readlines()
            file.writelines(data)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('Task3/phonebook.csv', 'rb'))
    await log.logger('Phonebook.csv unloaded')

async def export_phonebook_message(update: Update, context: CallbackContext):
    await log.logger('Phonebook preview requested by user')
    await log.log(update, context)
    with open('Task3\phonebook.txt', 'r') as data:
        text = '\n'.join(data.readlines())
        await update.message.reply_text(text)
   
