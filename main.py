from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext.dispatcher import run_async

import requests
import re
import logging

from settings import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
	update.message.reply_text('Quer um doguinho ?')


def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']

	return url


def get_image_url():
	allowed_extension = ['jpg', 'jpeg', 'png']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = get_url()
		file_extension = re.search("([^.]*)$", url).group(1).lower()
	return url


@run_async
def dog(update, context):
	url = get_image_url()
	chat_id = update.message.chat_id

	context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler('dog', dog))

	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
