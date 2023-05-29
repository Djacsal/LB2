import telebot
import pandas as pd

from bot_handler import BotHandler

class TBot:
    def __init__(self, token, excel_file):
        self.token = token
        self.df = pd.read_excel(excel_file)
        self.bot = telebot.TeleBot(token)
        self.bot_handler = BotHandler(self.df, self.bot)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            student_list = '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(self.df['ФИО'])])
            self.bot.send_message(message.chat.id,'Привет! Я бот родителей в классе. Чтобы получить информацию об успеваемости ребенка, введите его ФИО.\nСписок учеников:\n' + student_list)

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            self.bot_handler.get_student_info(message)

        self.bot.polling()