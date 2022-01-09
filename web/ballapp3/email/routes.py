from flask import url_for, redirect, Blueprint, request
from flask_mail import Message
from ballapp3 import mail


email = Blueprint('email', __name__)


@email.route("/send_ready_email")
def email_route():
    msg = Message('Hello', sender='infoballapp@gmail.com', recipients=['jimshapedcoding@gmail.com'])
    msg.subject = "BallApp3 is ready to use ✔️"
    msg.body = f"""
    BallApp3 is ready to use!
    Access through: http://{request.environ.get('HTTP_X_REAL_IP', request.remote_addr)}
    """
    mail.send(msg)

    return ''
