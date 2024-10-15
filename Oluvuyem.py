import telebot
from telebot import types

API_TOKEN = '7769206506:AAEAp9fzpQLPOKWtA1sYhpGKD6CHTsV8PCE'
bot = telebot.TeleBot(API_TOKEN)

curses = []
user_count = set()
groups = set()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🧑‍💻 Hazırlayan", url="http://t.me/r4tkor")
    button2 = types.InlineKeyboardButton("🧩 Yeniliklər", url="http://t.me/ratk0r")
    button3 = types.InlineKeyboardButton("⚡Söhbət Qurupu⚡", url="http://t.me/SohbetQaraci")
    
    markup.add(button1, button2)
    markup.add(button3)

    bot.send_message(message.chat.id, "Salam 👋 Xoş gəldiniz! Botu qurupa əlavə edərək söyüşlərin qarşısını alın", reply_markup=markup)
    user_count.add(message.from_user.id)
    groups.add(message.chat.id)  # Qrup ID-sini əlavə edirik

@bot.message_handler(commands=['soyusyaz'])
def add_curse(message):
    curse = message.text.split(maxsplit=1)
    if len(curse) > 1:
        new_curses = curse[1].split(',')
        for word in new_curses:
            word = word.strip().lower()
            if word and word not in curses:
                curses.append(word)
                bot.send_message(message.chat.id, f"✅ Söyüş əlavə olundu: {word}")
    else:
        bot.send_message(message.chat.id, "❌ Söyüş əlavə etmək üçün düzgün formatda yazın: /soyusyaz söyüş1, söyüş2, ...")

@bot.message_handler(func=lambda message: True)
def check_curses(message):
    message_text = message.text.lower()
    for curse in curses:
        if curse in message_text:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, f"🚫 {message.from_user.first_name}, söyüş yazmağınız qadağandır!")
            break

@bot.message_handler(commands=['bstat'])
def statistics(message):
    stats = (
        f"📊 **Statistika**:\n"
        f"- **Qrupların sayı**: {len(groups)}\n"
        f"- **İstifadəçilərin sayı**: {len(user_count)}\n"
        f"- **Söyüşlərin sayı**: {len(curses)}\n"
        f"- **Son əlavə olunan söyüşlər**: {', '.join(curses) if curses else 'Heç biri yoxdur.'}"
    )
    bot.send_message(message.chat.id, stats)

bot.polling()
