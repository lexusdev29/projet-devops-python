from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main_bp
    app.register_blueprint(main_bp)   #préparation d'une structure propre avec blueprint

    return app
