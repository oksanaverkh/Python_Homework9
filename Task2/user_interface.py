import logger as log    
from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def start(update: Update, context: CallbackContext):
    await log.logger('User starts the program')
    await update.message.reply_text(f'Choose an operation: Calculation - enter /get, display logging journal - enter /load')
    await log.logger('User chose an operation')
    user_input = update.message.text


async def get_data(update: Update, context: CallbackContext):
    await update.message.reply_text('Enter number 1:')
    await update.message.reply_text('Enter an operator:')
    await update.message.reply_text('Enter number 2:')
    text = update.message.text.split()
    a = text[1]
    op = text[2]
    b = text[3]
    await log.logger(f'User entered numbers and operator')
    await log.log(update, context)

    if 'j' in a:
        a = complex(a)
    if 'j' in b:
        b = complex(b)
    else:
        a = int(a)
        b = int(b)

    result = 0
    await log.logger(f'Calculation in progress {a} {op} {b}')
    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    await update.message.reply_text(f'Result = {result}')
    await log.logger(f'Result displayed to user {result}')




