import telepot
# from telepot.loop import MessageLoop

def action(msg):
  chat_id = msg['chat']['id']
  command = msg['text']

  if command == '/start':
    test_archive_bot.sendMessage(chat_id,str("hola"))
    test_archive_bot.sendPhoto(chat_id, photo="https://static.wikia.nocookie.net/3e538daa-fe76-4d70-bec4-3e2a51d8695b")
  elif command == "/help":
    test_archive_bot.sendMessage(chat_id, str("COMMANDS \n /start=show introdction"))

test_archive_bot = telepot.Bot('2028651165:AAEWqdYXcKTUGLPlg9vC_ZXFwiAb3UmvM-c')
test_archive_bot.message_loop({'chat':action})

print (test_archive_bot.getMe())
