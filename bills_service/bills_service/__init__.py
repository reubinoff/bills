from flask import Flask
from flask_restful import Api
from os import environ

DEFAULT_CONFIG_NAME = "APP_CONFIG_FILE"


app = Flask(__name__, instance_relative_config=True)
api = Api(app)

if environ.get(DEFAULT_CONFIG_NAME) is None:
    environ[DEFAULT_CONFIG_NAME] = "dev"

app.config.from_envvar(DEFAULT_CONFIG_NAME)
app.config.from_mapping(
    SECRET_KEY='dev'
)

print("Running in {} mode".format(app.config.get("MODE")))

# routes
from . import routes
########


@app.route('/')
def hello_world():
    return 'Yair Reubinoff'


if __name__ == '__main__':
    app.run()
