from wtforms.validators import DataRequired, Length, Email
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

# 确保 username 字段只包含字母、数字、下划线和点号.
class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    Email()])
    username = StringField('Username', validators=[
     DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    'Usernames must have only letters, '
    'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    mysubmit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    mysubmit = SubmitField('Log In')