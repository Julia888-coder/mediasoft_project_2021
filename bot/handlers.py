import markups
from settings import token, answers
from test import Test
from telebot import TeleBot

bot = TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_hello(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['start'], reply_markup=markups.empty_markup())


@bot.message_handler(commands=['inf'])
def send_info(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['inf'], reply_markup=markups.inf_markup())


@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['help'], reply_markup=markups.empty_markup())


@bot.message_handler(commands=['url'])
def send_url(message):
    bot.send_message(message.chat.id, answers['url'], reply_markup=markups.url_markup())


@bot.message_handler(commands=['tests'])
def send_lectures(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['tests'], reply_markup=markups.lectures_markup())

@bot.message_handler(commands=['homework'])
def send_homework(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['homework'], reply_markup=markups.homework_markup())

@bot.message_handler(regexp='Домашние задания')
def send_homework1(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Домашние задания'])

@bot.message_handler(regexp='Задания по лекциям')
def send_tasks(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['з1'])
    bot.send_message(user_id, answers['з2'])
    bot.send_message(user_id, answers['з3'])


@bot.message_handler(regexp='Видеолекции')
def send_video_lectures(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Видеолекции'])


@bot.message_handler(regexp='Ресурсы')
def send_resources(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Ресурсы'])


@bot.message_handler(regexp='Назад')
def go_back(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['inf'], reply_markup=markups.inf_markup())


@bot.message_handler(regexp='Статьи')
def send_articles(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Статьи'], reply_markup=markups.articles_markup())


@bot.message_handler(regexp='Лекция 1')
def send_first_article(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 1'], reply_markup=markups.articles_markup())


@bot.message_handler(regexp='Лекция 2')
def send_second_article(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 2'], reply_markup=markups.articles_markup())


@bot.message_handler(regexp='Лекция 3')
def send_third_article(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 3'], reply_markup=markups.articles_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    call_data = call.data
    if call_data == "Назад":
        bot.edit_message_text(text=answers['tests'],
                              chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              reply_markup=markups.lectures_markup())
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
                                  reply_markup=markups.tests_markup(call_data[0:call_data.index('.')]))
