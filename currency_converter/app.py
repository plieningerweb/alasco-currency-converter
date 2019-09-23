from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object("currency_converter.settings")

    from .views import currency_converter
    app.register_blueprint(currency_converter)
    Bootstrap(app)

    return app
