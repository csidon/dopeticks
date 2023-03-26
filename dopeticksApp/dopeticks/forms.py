from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, email_validator, EqualTo, ValidationError
from dopeticks.models import User



# Creates HTML forms with classes from flask_wtf
class RegistrationForm(FlaskForm):
	userFirstName = StringField('First Name', validators=[DataRequired()])
	userLastName = StringField('Last Name', validators=[DataRequired()])
	userEmail = StringField('Email (This will also be your username)', validators=[DataRequired(), Email()])
	userPassword = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	confirmPassword = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('userPassword', message='Password must match')])
	submit = SubmitField('Get Your Account!')

	def validate_userEmail(self, userEmail):
		user = User.query.filter_by(userEmail=userEmail.data).first()
		# If the user query is none, nothing happens. Otherwise if the query returns data, throw validation error message
		if user:
			raise ValidationError("That email already exists. Please register with another email address")




class LoginForm(FlaskForm):
	userEmail = StringField('Email address', validators=[DataRequired(), Email()])
	userPassword = PasswordField('Password', validators=[DataRequired()])

	# Remembers user's information so that they do not need to re-login if they close their browser
	# using a secure cookie
	userRemember = BooleanField('Remember Me')

	submit = SubmitField('Login')
