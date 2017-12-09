import telepot
from pyramid.view import view_config

from telebot.lib.logger import log


@view_config(route_name='get_message', renderer='json', request_method='POST')
def get_message(request):
    config = request.registry.settings['telebot']
    log.debug("Handler config: %s", config)

    message = request.json_body['message']
    user = message['from']
    log.debug("Message: %s", message)

    bot = telepot.Bot(config['telegram.token'])
    user_id = str(user['id'])
    if user_id in config['telegram.allowed_user_ids']:
        reply = "Hello, {}! \"{}\" back at ya!".format(user['first_name'],
                                                       message['text'])
        bot.sendMessage(user['id'], reply)
