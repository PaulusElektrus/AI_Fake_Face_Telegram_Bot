from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import logging, configparser

config = configparser.ConfigParser()
config.read_file(open("./token.config", mode="r"))
token = config.get("config", "token")


def main():

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    async def neu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        chat_id = update.message.chat_id
        await context.bot.send_photo(
            chat_id=chat_id, photo="https://thispersondoesnotexist.com/image"
        )

    async def start(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            "Hallo, ich erzeuge dir Bilder von künstlich erzeugten Menschen. Schreib mir einfach /neu."
        )

    async def help_command(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Schreib mir einfach /neu.")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("neu", neu))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hilfe", help_command))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()


if __name__ == "__main__":
    main()
