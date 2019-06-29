import logging
import logging.config
from .logger import logging_config

from flask import Flask
from flask_restful import Api
from os import environ
from flask_sqlalchemy import SQLAlchemy
from bills_service import logger

DEFAULT_CONFIG_NAME = "APP_CONFIG_FILE"


app = Flask(__name__, instance_relative_config=True)
api = Api(app)
logging.config.dictConfig(logging_config)
logging.getLogger().setLevel(
    getattr(logging, str(app.config.get("LOG_LEVEL")), "DEBUG"))

if environ.get(DEFAULT_CONFIG_NAME) is None:
    environ[DEFAULT_CONFIG_NAME] = "dev"

app.config.from_envvar(DEFAULT_CONFIG_NAME)

logging.info("Running in {} mode".format(app.config.get("MODE")))

######################### DB #####################
db = SQLAlchemy(app)
###############################################################

######################### ROUTES #####################
from bills_service import routes
###############################################################


if __name__ == '__main__':
    app.run()
