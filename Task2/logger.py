from datetime import datetime as dt
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def logger(text):
    with open('log.txt', 'a') as data:
        data.write(str(text)+'\n')

async def log(update: Update, context: CallbackContext):
    file = open('log.txt', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

def logger_out():
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'r') as data:
        print(time, data.readlines())

async def logger_journal(update: Update, context: CallbackContext):
    await Bot.send_document(chat_id=Update.effective_chat, document=open('Task2/log.txt', 'rb'))