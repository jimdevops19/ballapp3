from flask import Flask
from flask_mail import Mail
import os


app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static/',
)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jokelie1919@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Additional flask plugins:
mail = Mail(app)

# Import your blueprints, register them:
from ballapp3.session.routes import session
from ballapp3.email.routes import email

app.register_blueprint(session)
app.register_blueprint(email)