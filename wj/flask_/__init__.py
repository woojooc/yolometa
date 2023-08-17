from flask import Flask
import config

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
