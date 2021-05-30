import telebot
from settings import token, answers, lectures
from keyboards import get_start_keyboard, get_lectures_keyboard, get_tests_keyboard
from test import Test

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['start'], reply_markup=get_start_keyboard())


@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['help'])


@bot.message_handler(commands=['tests'])
def send_lectures(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['tests'], reply_markup=get_lectures_keyboard())


@bot.message_handler(regexp='Книги')
def send_books(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Книги'])


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    call_data = call.data
    if call_data == "Назад":
        bot.edit_message_text(text=answers['tests'],
                              chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              reply_markup=get_lectures_keyboard())
    else:
        previous_text = call.message.json['text']
        if "выберите тему теста" in previous_text.lower():
            lecture_number = previous_text[previous_text.index("«") + 1:previous_text.index(".")]
            test_number = call_data[0:call_data.index('.')]
            the_test = Test(bot=bot,
                            chat_id=call.message.chat.id,
                            lecture_number=lecture_number,
                            test_number=test_number)
            the_test.start()
        elif "выберите лекцию" in previous_text.lower():
            bot.edit_message_text(text=f"Вы выбрали лекцию «{call_data}». Выберите тему теста:",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  reply_markup=get_tests_keyboard(call_data[0:call_data.index('.')]))
