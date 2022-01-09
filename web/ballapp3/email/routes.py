import os
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
    Access through: http://{os.environ.get('PUBLIC_IP')}
    
    """
    mail.send(msg)

    return ''
