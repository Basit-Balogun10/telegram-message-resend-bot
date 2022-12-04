from decouple import config
import telegram

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

def telegram_bot(request):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        message = update.message
        
        message_id = message.id
        chat_id = message.chat.id
        original_message = message.reply_to_message
        caption = ""
        if original_message.caption:
            caption = original_message.caption
        
        if original_message.animation:
            bot.sendAnimation(chat_id=chat_id, animation=original_message.animation.file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.audio:
            bot.sendAudio(chat_id=chat_id, audio=original_message.audio.file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.document:
            bot.sendDocument(chat_id=chat_id, document=original_message.document.file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.photo:
            bot.sendPhoto(chat_id=chat_id, photo=original_message.photo[0].file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.sticker:
            bot.sendSticker(chat_id=chat_id, sticker=original_message.sticker.file_id, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.video:
            bot.sendVideo(chat_id=chat_id, video=original_message.video.file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.video_note:
            bot.sendVideoNote(chat_id=chat_id, video_note=original_message.video_note.file_id, reply_to_message_id=message_id, allow_sending_without_reply=True)
        elif original_message.voice:
            bot.sendVoice(chat_id=chat_id, voice=original_message.voice.file_id, caption=caption, reply_to_message_id=message_id, allow_sending_without_reply=True)
        else:
            bot.sendMessage(chat_id=chat_id, text=original_message.text, reply_to_message_id=message_id, allow_sending_without_reply=True)
        
        # Reply with the same message
        # bot.sendMessage(chat_id=chat_id, text=update.message.text, reply_to_message_id=message_id, allow_sending_without_reply=True)
    return "OK"