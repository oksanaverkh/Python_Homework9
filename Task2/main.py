import logger as log
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import user_interface as ui

app = ApplicationBuilder().token("5812301493:AAGP6LQ1R9DZ5SA-FkzcXZENs9QiMtm2a_8").build()
print('server start')
user_input = input('''Choose an operation:
                        Calculation - 1, log_output - 2''')
if user_input =='1':
    app.add_handler(CommandHandler("get", ui.get_data))
    app.run_polling()
else:
    # log.logger_out()
     
    app.add_handler(CommandHandler("load", log.logger_journal))
    app.run_polling()






# app.add_handler(CommandHandler("res", ui.get_result))
# app.add_handler(CommandHandler("get", ui.get_data))




