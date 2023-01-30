# import logger as log    
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

result = 0
async def get_data(update: Update, context: CallbackContext):
    global result
    await update.message.reply_text('Enter number 1:')
    await update.message.reply_text('Enter an operator:')
    await update.message.reply_text('Enter number 2:')
    text = update.message.text.split()
    a = text[1]
    
    op = text[2]
    
    b = text[3]
    # await log.log(update, context)
    # await log.logger(a+op+b)

    if 'j' in a:
        a = complex(a)
    if 'j' in b:
        b = complex(b)
    else:
        a = int(a)
        b = int(b)

    result = 0
    # await log.logger(f'Calculation in progress {a} {op} {b}')
    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    await update.message.reply_text(f'Result = {result}')
    exit()
    # await result
    

# async def get_result(update: Update, context: CallbackContext):
#     await update.message.reply_text(f'Result = {result}')



    # await a, b, op

# async def set_data(update: Update, context: CallbackContext, data):
#     await update.message.reply_text(f'Result = {data}')
#     await log.log(update, context)
#     await log.logger(data)


