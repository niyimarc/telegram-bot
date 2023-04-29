from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, Bot
import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


API_KEY = 'TOKEN_HERE'
bot = Bot(token=API_KEY)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = Update.de_json(request.body, bot)
        application.process_update(update)
        return HttpResponse("ok")
    else:
        return HttpResponse("it is get, not post!")
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(API_KEY).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()