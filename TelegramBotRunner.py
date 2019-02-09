import telegram

my_token = '746952122:AAHbdl3fPpNJTnAWnX-QYCOSD3czGG4sSzI'

bot = telegram.Bot(token= my_token)
updates = bot.getUpdates()

chat_id = bot.getUpdates()[-1].message.chat.id #

bot.sendMessage(chat_id = chat_id, text="I am conan, It's a detective.")
