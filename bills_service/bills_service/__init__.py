from flask import Flask
from flask_restful import Api




app = Flask(__name__)
api = Api(app)

app.config.from_mapping(
    SECRET_KEY='dev'
)



#routes
from . import routes
########

@app.route('/')
def hello_world():
    return 'Hello moshe reubinoff'


if __name__ == '__main__':
    app.run()
