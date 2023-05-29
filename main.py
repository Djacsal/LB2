from telegram_bot import TBot

if __name__ == "__main__":
    token = '6023751288:AAEZZlv0ks27J3_Rk27A8y4ZMm8aflUVHAw'
    exel_file = 'students.xlsx'

    bot_app = TBot(token, exel_file)
    bot_app.run()

