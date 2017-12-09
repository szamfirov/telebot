import logging


log = logging.getLogger(__name__)


def setup_logger(log_level="INFO"):
    logging.basicConfig(level=getattr(logging, log_level.upper()),
                        format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s '
                        '(%(filename)s:%(lineno)d)',
                        datefmt='%Y-%m-%d %H:%M:%S %z')
