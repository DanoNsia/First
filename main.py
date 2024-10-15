import telebot
import datetime
import time
import threading

from telebot.apihelper import send_message

bot = telebot.TeleBot("Введите токен")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, "Привет! Я буду напоминать тебе вовремя колоть <3")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

def send_reminders(chat_id):
    rem = "23:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == rem:
            bot.send_message(chat_id, "Пора бы уколоть <3")
            time.sleep(61)
        time.sleep(1)



bot.polling(none_stop=True)