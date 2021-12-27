from flask_wtf import FlaskForm
from wtforms import SubmitField


class ContinueSessionCreationForm(FlaskForm):
    submit = SubmitField(label='Continue ...')