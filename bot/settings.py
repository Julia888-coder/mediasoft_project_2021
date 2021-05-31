import json

token = '1801800815:AAEjupazugiswS0ne_hM0pZRLvsY5_SUUh0'

with open('./resources/json/lectures.json', 'r', encoding='UTF-8') as read_file:
    lectures = json.load(read_file)

with open('./resources/json/answers.json', 'r', encoding='UTF-8') as read_file:
    answers = json.load(read_file)