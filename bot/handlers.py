import telebot
from settings import token, answers
from markups import inf_markup, lectures_markup, tests_markup, empty_markup, articles_markup
from test import Test
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_hello(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['start'], reply_markup=empty_markup())


@bot.message_handler(commands=['inf'])
def send_info(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['inf'], reply_markup=inf_markup())


@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['help'], reply_markup=empty_markup())

@bot.message_handler(commands = ['url'])
def url(message):
    markup = InlineKeyboardMarkup()
    btn_my_site= InlineKeyboardButton(text='Гугл диск', url='https://drive.google.com/drive/folders/13GHAaf6VAbaPh8EF'
                                                            '2v3FxDdZHxB2J6wj?usp=sharing')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "По ссылке можно найти оформленные презентации, документы и задания. ", reply_markup = markup)

@bot.message_handler(commands=['tests'])
def send_lectures(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['tests'], reply_markup=lectures_markup())


@bot.message_handler(regexp='Книги')
def send_books(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Книги'])

@bot.message_handler(regexp='Видеолекции')
def send_videolec(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Видеолекции'])

@bot.message_handler(regexp='Ресурсы')
def send_resourses(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Ресурсы'])

@bot.message_handler(regexp='Назад')
def send_back(message):
    user_id = message.chat.id
    bot.send_message(user_id, "повторный выбор", reply_markup=inf_markup())

@bot.message_handler(regexp='Статьи')
def send_articles(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Статьи'], reply_markup=articles_markup())

@bot.message_handler(regexp='Лекция 1')
def send_article1(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 1'], reply_markup=articles_markup())

@bot.message_handler(regexp='Лекция 2')
def send_article2(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 2'], reply_markup=articles_markup())

@bot.message_handler(regexp='Лекция 3')
def send_article3(message):
    user_id = message.chat.id
    bot.send_message(user_id, answers['Лекция 3'], reply_markup=articles_markup())



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    call_data = call.data
    if call_data == "Назад":
        bot.edit_message_text(text=answers['tests'],
                              chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              reply_markup=lectures_markup())
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
                                  reply_markup=tests_markup(call_data[0:call_data.index('.')]))
