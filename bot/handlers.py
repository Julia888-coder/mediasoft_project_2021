import markups
from settings import token, answers, lectures
from test import Test
from telebot import TeleBot

bot = TeleBot(token, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_hello(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["start"], reply_markup=markups.empty_markup())


@bot.message_handler(commands=["inf"])
def send_info(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["inf"], reply_markup=markups.inf_markup())


@bot.message_handler(commands=["help"])
def send_help(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["help"], reply_markup=markups.empty_markup())


@bot.message_handler(commands=["url"])
def send_url(message):
    bot.send_message(message.chat.id, answers["url"], reply_markup=markups.url_markup())


@bot.message_handler(commands=["tests"])
def send_lectures(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["tests"], reply_markup=markups.lectures_markup())


@bot.message_handler(commands=["homework"])
def send_homework_info(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["homework"], reply_markup=markups.homework_markup())


@bot.message_handler(regexp="Назад")
def go_back(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers["inf"], reply_markup=markups.inf_markup())


@bot.message_handler(content_types=["text"])
def handle_text_message(message):
    user_input = message.text.lower()
    if user_input == "статьи":
        bot.send_message(message.from_user.id, answers["Статьи"], reply_markup=markups.articles_markup())
    elif user_input == "лекция 1":
        bot.send_message(message.from_user.id, lectures["1"]["sources"], reply_markup=markups.articles_markup())
    elif user_input == "лекция 2":
        bot.send_message(message.from_user.id, lectures["2"]["sources"], reply_markup=markups.articles_markup())
    elif user_input == "лекция 3":
        bot.send_message(message.from_user.id, lectures["3"]["sources"], reply_markup=markups.articles_markup())
    elif user_input == "ресурсы":
        bot.send_message(message.from_user.id, answers["Ресурсы"])
    elif user_input == "видеолекции":
        bot.send_message(message.from_user.id, answers["Видеолекции"])
    elif user_input == "задания по лекциям":
        bot.send_message(message.from_user.id, answers["дз1"])
        bot.send_message(message.from_user.id, answers["дз2"])
        bot.send_message(message.from_user.id, answers["дз3"])
    elif user_input == "домашние задания":
        bot.send_message(message.from_user.id, answers["Домашние задания"])
    elif user_input == "назад":
        bot.send_message(message.from_user.id, answers["inf"], reply_markup=markups.inf_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    call_data = call.data
    if call_data == "Назад":
        bot.edit_message_text(text=answers["tests"],
                              chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              reply_markup=markups.lectures_markup())
    else:
        previous_text = call.message.json["text"]
        if "выберите тему теста" in previous_text.lower():
            lecture_number = previous_text[previous_text.index("«") + 1:previous_text.index(".")]
            test_number = call_data[0:call_data.index(".")]
            the_test = Test(bot=bot,
                            chat_id=call.message.chat.id,
                            lecture_number=lecture_number,
                            test_number=test_number)
            the_test.start()
        elif "выберите лекцию" in previous_text.lower():
            bot.edit_message_text(text=f"Вы выбрали лекцию «{call_data}». Выберите тему теста:",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  reply_markup=markups.tests_markup(call_data[0:call_data.index(".")]))
