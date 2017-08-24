import os
from telegram.ext import Updater


TOKEN = os.environ['TOKEN_TELEGRAM']
PORT = int(os.environ['PORT'])
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://webh00k.herokuapp.com/" + TOKEN)
print("url set")
updater.idle()
