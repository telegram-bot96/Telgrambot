import os
import telebot
from telebot import types

API_TOKEN = os.getenv("BOT_TOKEN")  # token will come from Glitch/Heroku
bot = telebot.TeleBot(API_TOKEN)

# Start command with buttons
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Videos Set 1 🎥")
    btn2 = types.KeyboardButton("Videos Set 2 🎥")
    btn3 = types.KeyboardButton("Videos Set 3 🎥")
    btn4 = types.KeyboardButton("Videos Set 4 🎥")
    btn5 = types.KeyboardButton("Videos Set 5 🎥")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.reply_to(message, "Welcome! Choose a set of videos:", reply_markup=markup)

# Send videos when button pressed
@bot.message_handler(func=lambda message: True)
def send_videos(message):
    if message.text == "Videos Set 1 🎥":
        videos = ["FILE_ID1", "FILE_ID2", "FILE_ID3"]  # replace with your file_ids
    elif message.text == "Videos Set 2 🎥":
        videos = ["FILE_ID21", "FILE_ID22"]
    elif message.text == "Videos Set 3 🎥":
        videos = ["FILE_ID31", "FILE_ID32"]
    elif message.text == "Videos Set 4 🎥":
        videos = ["FILE_ID41", "FILE_ID42"]
    elif message.text == "Videos Set 5 🎥":
        videos = ["FILE_ID51", "FILE_ID52"]
    else:
        return

    for vid in videos:
        bot.send_video(message.chat.id, vid)

bot.polling()
