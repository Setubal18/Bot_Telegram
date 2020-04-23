import re

from telegram.ext.dispatcher import run_async
import requests

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']

	return url


def get_image_url():
	allowed_extension = ['jpg', 'jpeg', 'png']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = get_url()
		print(url)
		file_extension = re.search("([^.]*)$", url).group(1).lower()
	return url


@run_async
def dog(update, context):
	url = get_image_url()
	chat_id = update.message.chat_id

	context.bot.send_photo(chat_id=chat_id, photo=url)
