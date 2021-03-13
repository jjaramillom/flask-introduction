from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, ValidationError
from market.models.User import User


class Register(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30)])
    email = StringField(label='Email Address', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=6)])
    password_confirmation = PasswordField(label='Confirm password', validators=[EqualTo('password')])
    submit = SubmitField(label='Create Account')

    # FlaskForm is taking all functions that start with validate_
    # to automatically validate the variable following the "_", in this case username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already used')
