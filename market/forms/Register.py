from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo


class Register(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30)])
    email = StringField(label='Email Address', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=6)])
    password_confirmation = PasswordField(label='Confirm password', validators=[EqualTo(password)])
    submit = SubmitField(label='Create Account')
