import os
import telebot
from flask import Flask, request

# 🔑 ضع هنا توكن بوت المصنع الجديد والكامل (الذي يبدأ بـ 8888) بين علامتي التنصيص
TOKEN = "8886950289:AAG_71RKVArou92X3f94mioBk-AwOvEnGcI"  
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

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
        # قراءة الأرقام من المصفوفة بدقة لمنع انهيار البوت
        height = float(args[1])
        width = float(args[2])
        area = height * width
        bot.reply_to(message, f"🏭 **مصنع شركة معين الخير**\n📐 المساحة الإجمالية للباب: `{area:.2f}` متر مربع.")
    except (IndexError, ValueError):
        bot.reply_to(message, "❌ يرجى إدخال المقاسات بشكل صحيح بعد الأمر.\nمثال:\n`/calculate 2.5 1.2`")

@server.route('/', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    return "بوت مصنع معين الخير يعمل بنجاح!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
