from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from settings import lectures


def start_markup():
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)


def inf_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    books_button = KeyboardButton('Книги')
    lectures_button = KeyboardButton('Лекции')
    articles_button = KeyboardButton('Статьи')
    back_button = KeyboardButton('Назад')
    markup.row(books_button)
    markup.row(lectures_button)
    markup.row(articles_button)
    markup.row(back_button)
    return markup


def empty_markup():
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)


def lectures_markup():
    markup = InlineKeyboardMarkup()

    for i in range(1, len(lectures) + 1):
        markup.add(
            InlineKeyboardButton(lectures[str(i)]["lecture_name"], callback_data=lectures[str(i)]["lecture_name"]))

    return markup


def tests_markup(lecture_number: str):
    markup = InlineKeyboardMarkup()

    lecture_tests = lectures[lecture_number]["tests"]

    for i in range(1, len(lecture_tests) + 1):
        markup.add(InlineKeyboardButton(lecture_tests[str(i)]["name"],
                                        callback_data=lecture_tests[str(i)]["name"]))

    markup.add(
        InlineKeyboardButton("Назад", callback_data="Назад"))

    return markup
