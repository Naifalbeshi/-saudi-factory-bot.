import os
from flask import Flask, request
import telebot

app = Flask(__name__)
server = app

TOKEN = os.getenv("8526301637:AAExxSCgqy_3bqYRuXtAoeZdSL5ek1236j0") # ناخذه من Render مو من الكود
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "مرحباً بك يا نايف في نظام مصنع شركة معين الخير! 🏭📐\n"
        "أنا مساعدك الفني الفوري للأبواب والحديد.\n\n"
        "📐 **الأوامر المتاحة حالياً:**\n"
        "• /calculate [الارتفاع] [العرض] - لحساب المساحة الإجمالية للأبواب."
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['calculate'])
def calculate_door(message):
    try:
        args = message.text.split()
        if len(args) >= 3:
            height = float(args[1])
            width = float(args[2])
            area = height * width
            bot.reply_to(message, f"🏭 **مصنع شركة معين الخير**\n📐 المساحة: `{area:.2f}` متر مربع.", parse_mode="Markdown")
        else:
            bot.reply_to(message, "❌ مثال:\n`/calculate 2.5 1.2`", parse_mode="Markdown")
    except:
        bot.reply_to(message, "❌ تأكد من الأرقام")

@app.route('/', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    return "بوت معين الخير شغال ✅", 200
