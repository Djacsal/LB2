class BotHandler:
    def __init__(self, df, bot=None):
        self.df = df
        self.bot = bot

    def get_student_info(self, text_message):
        student_name = text_message.text.strip()
        student_data = self.df.loc[self.df['ФИО'] == student_name]

        if student_data.empty:
            self.bot.send_message(text_message.chat.id, "Не удалось найти информацию об ученике с ФИО: " + student_name)
        else:
            message = "Успеваемость ученика: " + student_name + ":\n"
            for subject in student_data.columns[1:]:
                message += subject + ": " + str(student_data[subject].values[0]) + "\n"

            self.bot.send_message(text_message.chat.id, message)
