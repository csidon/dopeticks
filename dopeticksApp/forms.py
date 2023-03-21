from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, email_validator



# Creates HTML forms with classes from flask_wtf
class RegistrationForm(FlaskForm):
	userEmail = StringField('Email', validators=[DataRequired(), Email()])
	userPassword = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Get Your Account!')


class LoginForm(FlaskForm):
	userEmail = StringField('Email', validators=[DataRequired(), Email()])
	userPassword = PasswordField('Password', validators=[DataRequired()])

	# Remembers user's information so that they do not need to re-login if they close their browser
	# using a secure cookie
	userRemember = BooleanField('Remember Me')

	submit = SubmitField('Login')
