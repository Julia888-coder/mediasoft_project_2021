import telebot
from settings import token, answers, lectures
from keyboards import get_start_keyboard, get_lectures_keyboard, get_tests_keyboard

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
            start_test(lecture_number, test_number, call.message.chat.id)
        elif "выберите лекцию" in previous_text.lower():
            bot.edit_message_text(text=f"Вы выбрали лекцию «{call_data}». Выберите тему теста:",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  reply_markup=get_tests_keyboard(call_data[0:call_data.index('.')]))


def start_test(lecture_number, test_number, chat_id):
    questions = lectures[lecture_number]["tests"][test_number]["questions"]
    right_answers = len(questions)
    current_right_answers = 0
    current_question_number = 1

    current_question = questions[str(current_question_number)]
    bot.send_message(chat_id=chat_id, text=current_question["question_text"])
    bot.register_next_step_handler(chat_id=chat_id, callback=is_answer_right)


@bot.message_handler(content_types=["text"])
def is_answer_right(message):
    if message.text.lower() == "1":
        return True
    return False
