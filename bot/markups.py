from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from settings import lectures


def empty_markup():
    return ReplyKeyboardRemove()


def inf_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    books_button = KeyboardButton('Книги')
    video_lectures_button = KeyboardButton('Видеолекции')
    articles_button = KeyboardButton('Статьи')
    resources_button = KeyboardButton('Ресурсы')
    markup.row(books_button, video_lectures_button)
    markup.row(articles_button, resources_button)
    return markup


def homework_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    homework1_button = KeyboardButton('Домашние задания')
    tasks_button = KeyboardButton('Задания по лекциям')
    markup.add(homework1_button)
    markup.add(tasks_button)
    return markup


def articles_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i in range(1, len(lectures) + 1):
        articles_button = KeyboardButton(f'Лекция {lectures[str(i)]["lecture_name"]}')
        markup.add(articles_button)
    back_button = KeyboardButton('Назад')
    markup.add(back_button)
    return markup


def url_markup():
    markup = InlineKeyboardMarkup()
    url_button = InlineKeyboardButton(text='Google-диск с материалами',
                                      url='https://drive.google.com/drive/folders/13GHAaf6VAbaPh8EF'
                                          '2v3FxDdZHxB2J6wj?usp=sharing')
    markup.add(url_button)
    return markup


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
    markup.add(InlineKeyboardButton("Назад", callback_data="Назад"))
    return markup
