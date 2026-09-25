import os
import telebot
from flask import Flask, request

TOKEN = os.getenv"TELEGRAM_BOT_TOKEN", "8886950289:AAG_71RKVArou92X3f94mioBk-AwOvEnGcI"
bot = telebot.TeleBot(8886950289:AAG_71RKVArou92X3f94mioBk-AwOvEnGcI)
server = Flask(__المصنع السعودي__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "مرحباً بك يا نايف في نظام مصنع شركة معين الخير! 🏭📐\n"
        "أنا مساعدك الفني الفوري للأبواب والحديد، وجاهز لتنفيذ الأوامر الفنية التالية:\n\n"
        "📐 **الحسابات الفنية:**\n"
        "• /calculate [الارتفاع] [العرض] - لحساب المساحة الإجمالية للأبواب.\n\n"
        "📝 **صياغة المعاملات والخطابات:**\n"
        "• /letter_increase - مسودة خطاب طلب زيادة موظف مع التزكية.\n"
        "• /meeting_minutes - نموذج جاهز لمحضر اجتماع المصنع.\n"
        "• /checklist - جدول استلام أبواب الرول الأربعة (أنفال)."
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['calculate'])
def calculate_door(message):
    try:
        args = message.text.split()
        height = float(args[1])
        width = float(args[2])
        area = height * width
        bot.reply_to(message, f"🏭 **مصنع شركة معين الخير**\n📐 المساحة الإجمالية للباب: `{area:.2f}` متر مربع.")
    except (IndexError, ValueError):
        bot.reply_to(message, "❌ يرجى إدخال المقاسات بشكل صحيح. مثال:\n`/calculate 2.5 1.2`")

@bot.message_handler(commands=['letter_increase'])
def letter_increase(message):
    letter = (
        "📝 **خطاب طلب زيادة راتب لموظف (مع التزكية والتوصية)**\n\n"
        "السادة إدارة شركة معين الخير المحترمين،\n"
        "نود تزكية وتوصية الموظف لزيادة راتبه نظير جهوده الاستثنائية داخل مصنع الأبواب والحديد.\n\n"
        "مقدمه لسيادتكم:\n"
        "مدير إدارة المصنع / نايف"
    )
    bot.reply_to(message, letter, parse_mode="Markdown")

@bot.message_handler(commands=['checklist'])
def checklist(message):
    check_list = (
        "📋 **جدول استلام أبواب رول (عدد 4 - أنفال):**\n\n"
        "🔲 فحص سلامة التشغيل والتوقف الذاتي في الأعلى والأسفل.\n"
        "🔲 فحص توقف الطوارئ المفاجئ (Emergency Stop).\n"
        "🔲 فحص ارتداد الباب تلقائياً عند اعتراض أي جسم أثناء الإغلاق.\n"
        "🔲 فحص وتشغيل النظام اليدوي بالسلسلة (Chain)."
    )
    bot.reply_to(message, check_list, parse_mode="Markdown")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    return "بوت مصنع معين الخير مستيقظ ويعمل!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
