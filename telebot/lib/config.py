import os
from configparser import ConfigParser

from telebot.lib.exceptions import InvalidConfigException
from telebot.lib.logger import log


ENV_VARS = {
    'telegram__allowed_user_ids': True,
    'telegram__token': True,
}

config = {}


def init_config(path):
    path = path if os.path.isfile(path) else None
    config.update(read_config(path))
    return config


def read_config(files=None):
    log.info("Loading settings from: %s", files)
    settings = {}
    files = files or []
    config = ConfigParser()
    config.read(files)
    settings = config_parser_to_flat(config)
    log.debug("Settings from file: %s", settings)
    return settings


def config_parser_to_flat(config):
    return dict(
        ('{}.{}'.format(sec, item), value)
        for sec in config.sections()
        for item, value in config.items(sec))


def get_settings_from_env(env_vars=None):
    log.info("Loading settings from ENV variables")
    settings = {}
    env_vars = ENV_VARS if env_vars is None else env_vars
    for name, value in env_vars.items():
        value = os.getenv(name)
        if not value:
            raise InvalidConfigException(name)
        log.debug("ENV Variable: %s = %s", name, value)
        settings[name.replace('__', '.')] = value
    log.debug("Settings from ENV: %s", settings)
    return settings
