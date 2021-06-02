import json
import os

# Ключ доступа к сообществу
ACCESS_KEY = os.getenv('TOKEN')

with open('../resources/json/lectures.json', 'r', encoding='UTF-8') as read_file:
    lectures = json.load(read_file)

with open('../resources/json/answers.json', 'r', encoding='UTF-8') as read_file:
    answers = json.load(read_file)
