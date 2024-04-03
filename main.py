import telebot
from yandex_api import add_track, is_yandex_music_track_link
from config import TG_TOKEN


playListId = 1004
bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'video_note', 'contact', 'location', 'venue', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message', 'invoice', 'successful_payment', 'connected_website', 'passport_data', 'poll', 'dice'])
def handle_message(message):
    if message.content_type == 'text':
        text = message.text
        if is_yandex_music_track_link(text):
            if add_track(playListId, text):
                bot.reply_to(message, 'Трек добавлен')
            else:
                bot.reply_to(message, 'Трек уже есть в плейлисте')
        else:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                print("error")
    else:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            print("error")

bot.infinity_polling()