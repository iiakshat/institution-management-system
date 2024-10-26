from flask import Flask
from flask_login import LoginManager
from config import Config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app