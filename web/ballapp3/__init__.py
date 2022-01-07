from flask import Flask
import os

def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        static_url_path='',
    )

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    # Import your blueprints, register them:
    from ballapp3.session.routes import session

    app.register_blueprint(session)
    return app