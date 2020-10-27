# First Party Packages
from telegram import Update
from telegram.ext import Updater, CommandHandler

# Python Packages
import requests
import re
import logging


def get_url():
    contents = requests.get("https://fakeface.rest/face/json").json()
    url = contents["image_url"]
    return url


def get_image_url():
    allowed_extension = ["jpg", "jpeg", "png"]
    file_extension = ""
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


def neu(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def start(update, context):
    update.message.reply_text(
        "Hallo, ich erzeuge dir Bilder von künstlich erzeugten Menschen. Schreib mir einfach /neu."
    )


def help_command(update, context):
    update.message.reply_text("Schreib mir einfach /neu.")


def main():

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    )

    updater = Updater("1379740291:AAH_uoawZS5TUgcGyBJ1OO3f4Qy-wAny2o4")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("neu", neu))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("hilfe", help_command))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
