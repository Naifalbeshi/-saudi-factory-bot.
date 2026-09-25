import os
from flask import Flask, request, jsonify
import telebot

# تهيئة التطبيق باسم app ليطابق البوت الشغال
app = Flask(__name__)

# 💡 حل ذكي: جعل الكلمتين تشيران لنفس التطبيق لحل خطأ Render فوراً
server = app 

# 🔑 ضع توكن بوت المصنع السعودي الكامل هنا بين علامتي التنصيص
TOKEN = "8886950289:AAG_71RKVArou92X3f94mioBk-AwOvEnGcI"  
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
            bot.reply_to(message, f"🏭 **مصنع شركة معين الخير**\n📐 المساحة الإجمالية للباب: `{area:.2f}` متر مربع.")
        else:
            bot.reply_to(message, "❌ يرجى إدخال المقاسات بعد الأمر. مثال:\n`/calculate 2.5 1.2`")
    except (IndexError, ValueError):
        bot.reply_to(message, "❌ حدث خطأ، يرجى التأكد من كتابة الأرقام بشكل صحيح بعد الأمر.")

@app.route('/', methods=['POST'])
def telegram_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Invalid request', 403

@app.route('/', methods=['GET'])
def index():
    return "بوت مصنع معين الخير يعمل بنجاح ومستيقظ تماماً!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
