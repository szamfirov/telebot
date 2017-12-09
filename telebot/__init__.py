import argparse

from pyramid.config import Configurator

from telebot.lib.config import get_settings_from_env, init_config
from telebot.lib.logger import log, setup_logger
from telebot.routes import setup_routes


def main(global_config, **settings):
    setup_logger("DEBUG")

    try:
        global_config_file = global_config['__file__']
    except KeyError:
        global_config_file = 'settings.ini'

    settings['telebot'] = init_config(global_config_file)

    config = Configurator(settings=settings)
    setup_routes(config)
    config.scan('telebot.handlers')
    return config.make_wsgi_app()


def generate_wsgi_app(app, environ):
    setup_logger()

    settings = {}
    settings['telebot'] = get_settings_from_env()
    config = Configurator(settings=settings)
    setup_routes(config)
    config.scan('telebot.handlers')
    return config.make_wsgi_app()(app, environ)


if __name__ == "__main__":
    main({})
