import telebot

TOKEN = '7182143701:AAHGwa4SNdBbF5PtOvFwCzmXBBOCFbzmp1U'
bot = telebot.TeleBot(TOKEN)

students = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "����� ���������� � ����������� ������! ����� ������, ��������� ���� ���.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in students:
        students[chat_id] = {'name': text, 'grades': []}
        bot.send_message(chat_id, f"������, {text}! �� ������� ���������������� � �������.")

    else:

        bot.send_message(chat_id, "� ���� �� ���� ������������ ���. ����� ������ ��������� �������, �������� /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "��������� �������:\n/add_grade - �������� ������\n/view_grades - ���������� ������"
    bot.send_message(message.chat.id, help_text)

bot.polling()
