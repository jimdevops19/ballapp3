from flask import Flask


def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        static_url_path='',
    )

    app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
    # Import your blueprints, register them:
    from ballapp3.session.routes import session

    app.register_blueprint(session)
    return app