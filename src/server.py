from flask import Flask, current_app, Blueprint

v1_api = Blueprint("v1_api", __name__, url_prefix='/v1/')

def create_app():
    app = Flask(__name__)

    # TODO: Add config parameters to app object and set up database connection

    app.register_blueprint(v1_api)

    return app


@v1_api.route("/ping")
def hello():
    return "pong"