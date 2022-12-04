from decouple import config
import telegram

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

def telegram_bot(request):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "okay"