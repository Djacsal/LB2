import telebot
import pandas as pd

# Токен вашего бота, который вы получите от BotFather в Telegram
TOKEN = '6023751288:AAEZZlv0ks27J3_Rk27A8y4ZMm8aflUVHAw'

# Загружаем файл Excel с данными об учениках и их успеваемости
df = pd.read_excel('students.xlsx')

# Создаем объект для работы с ботом
bot = telebot.TeleBot(TOKEN)

# Функция, которая будет вызываться при отправке команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот родителей в классе. Чтобы получить информацию об успеваемости ребенка, введите его ФИО.')

# Функция, которая будет вызываться при отправке сообщения с ФИО ученика
@bot.message_handler(content_types=['text'])
def get_student_info(text_message):
    student_name = text_message.text.strip()

    # Ищем данные об ученике по ФИО
    student_data = df.loc[df['ФИО'] == student_name]

    # Если не удалось найти данные об ученике, отправляем сообщение об ошибке
    if student_data.empty:
        bot.send_message(text_message.chat.id, "Не удалось найти информацию об ученике с ФИО: " + student_name)
    else:
        # Формируем сообщение с данными об успеваемости ученика
        message = "Успеваемость ученика: " + student_name + ":\n"
        for subject in student_data.columns[1:]:
            message += subject + ": " + str(student_data[subject].values[0]) + "\n"

        # Отправляем сообщение с данными об успеваемости ученика
        bot.send_message(text_message.chat.id, message)

# Запускаем бота
bot.polling()
