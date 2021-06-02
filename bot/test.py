from settings import lectures


class Test:
    def __init__(self, bot, chat_id, lecture_number, test_number):
        self.name = lectures[lecture_number]["tests"][test_number]["name"]
        self.questions = lectures[lecture_number]["tests"][test_number]["questions"]
        self.number_of_questions = len(self.questions)
        self.current_question = 1
        self.chat_id = chat_id
        self.bot = bot

    def start(self):
        self.bot.send_message(chat_id=self.chat_id, text=f"Начинаем тест по теме «{self.name}». Поехали!")
        message = self.bot.send_message(chat_id=self.chat_id,
                                        text=self.questions[str(self.current_question)]["question_text"])
        try:
            photo = open(self.questions[str(self.current_question)]["image_path"], 'rb')
            self.bot.send_photo(self.chat_id, photo)
        except FileNotFoundError as e:
            print(e)
        self.bot.register_next_step_handler(message, self.is_answer_right)

    def is_answer_right(self, message):
        if "завершить" in message.text.lower():
            self.bot.send_message(chat_id=self.chat_id, text="Тест закончен!")
            return
        elif message.text.lower() in self.questions[str(self.current_question)]["correct_answer"]:
            self.bot.send_message(chat_id=self.chat_id, text="Верно!")
            self.current_question += 1
            if self.current_question > self.number_of_questions:
                self.bot.send_message(chat_id=self.chat_id, text="Тест закончен!")
                return
            message = self.bot.send_message(chat_id=self.chat_id,
                                            text=self.questions[str(self.current_question)]["question_text"])
            try:
                photo = open(self.questions[str(self.current_question)]["image_path"], 'rb')
                self.bot.send_photo(self.chat_id, photo)
            except FileNotFoundError as e:
                print(e)
        else:
            message = self.bot.send_message(chat_id=self.chat_id, text="Неверно! Повторите попытку.")
        self.bot.register_next_step_handler(message, self.is_answer_right)
