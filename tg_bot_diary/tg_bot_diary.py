import telebot

TOKEN = '7182143701:AAHGwa4SNdBbF5PtOvFwCzmXBBOCFbzmp1U'
bot = telebot.TeleBot(TOKEN)

students = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать в электронный журнал! Чтобы начать, отправьте свое имя.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in students:
        students[chat_id] = {'name': text, 'grades': []}
        bot.send_message(chat_id, f"Привет, {text}! Вы успешно зарегистрированы в системе.")

    else:

        bot.send_message(chat_id, "Я пока не умею обрабатывать это. Чтобы узнать доступные команды, напишите /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Доступные команды:\n/add_grade - добавить оценку\n/view_grades - посмотреть оценки"
    bot.send_message(message.chat.id, help_text)

bot.polling()
