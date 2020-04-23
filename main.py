from telegram.ext import \
	Updater, \
	CommandHandler, \
	ConversationHandler

import logging

from dogs import dog
from settings import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
	update.message.reply_text('Quer um doguinho ?')


def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	conv_handler = ConversationHandler(
		entry_points=[
			CommandHandler('start', start),
			CommandHandler('dog', dog),
		],
		states={},
		fallbacks=[]

	)
	dp.add_handler(conv_handler)

	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
