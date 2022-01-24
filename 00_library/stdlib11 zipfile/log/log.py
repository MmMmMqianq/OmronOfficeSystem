import logging.config

logging.config.fileConfig("logging.conf")
applogger = logging.getLogger("applog")