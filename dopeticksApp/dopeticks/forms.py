from datetime import datetime       # Manages datetime issues, also imported in models.py
from flask_wtf import FlaskForm				# Provides form validation functionality
from flask_wtf.file import FileField, FileAllowed	# Provides ability for the form to manage files/images
from flask_login import current_user				
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, DateField
from wtforms.validators import DataRequired, Length, Email, email_validator, EqualTo, ValidationError
from dopeticks.models import User



# Creates HTML forms with classes from flask_wtf
class RegistrationForm(FlaskForm):
	userFirstName = StringField('First Name', validators=[DataRequired()])
	userLastName = StringField('Last Name', validators=[DataRequired()])
	userEmail = StringField('Email (This will also be your username)', validators=[DataRequired(), Email()])
	userPassword = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	confirmPassword = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('userPassword', message='Password must match')])
	submit = SubmitField('Create account')

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

class UpdateAccountForm(FlaskForm):
	userFirstName = StringField('First Name', validators=[DataRequired()])
	userLastName = StringField('Last Name', validators=[DataRequired()])
	userEmail = StringField('Email (This will also be your username)', validators=[DataRequired(), Email()])
	uploadImage = FileField('Update your profile picture', validators=[FileAllowed(['jpg', 'png'])])

	submit = SubmitField('Update')

	def validate_userEmail(self, userEmail):
		if userEmail.data != current_user.userEmail:
			user = User.query.filter_by(userEmail=userEmail.data).first()
			# If the user query is none, nothing happens. Otherwise if the query returns data, throw validation error message
			if user:
				raise ValidationError("That email already exists. Please register with another email address")


# class TaskForm(FlaskForm):
# 	taskTitle = StringField('Title', validators=[DataRequired()])
# 	taskDescription = TextAreaField('Description', validators=[DataRequired()])

# 	# Will do this later
# 	taskStatus = SelectField('Task Status', validators=[DataRequired()], choices=[ ("To do", "todo"), ("Doing", "doing"), ("Done!", "done")] )
# 	# taskPriority = RadioField('Priority', validators=[DataRequired()], choices=["Normal", "High", "Urgent"], coerce=unicode )
# 	# Note to team: Let's do a task icon selection later once we get this working. We'll start with a default icon form now. 
# 	# taskIcon = FileField('Update your profile picture', validators=[FileAllowed(['jpg', 'png'])])
# 	# Due dates aren't a compulsory field
# 	# taskDue = DateField('Due Date', format='%d-%m-%Y')

# 	submit = SubmitField('Create New Task')

class TaskForm(FlaskForm):
	taskTitle = StringField('Title', validators=[DataRequired()])
	taskDescription = TextAreaField('Description', validators=[DataRequired()])
	taskDue = DateField('Task Due', format="%Y-%m-%d")
	# choices = [ ("To do", "todo"), ("Doing", "doing"), ("Done!", "done")]
	choices = {"To do", "Doing", "Done"}
	taskStatus = SelectField('Task Status', validators=[DataRequired()], choices=choices )
	# taskStatus = SelectField('Task Status', validators=[DataRequired()], choices=[ "To do", "Doing", "Done!"] )

	# taskStatus = SelectField('Task Status', validators=[DataRequired()], choices=[ ("To do", "todo"), ("Doing", "doing"), ("Done!", "done")] )

	submit = SubmitField('Create New Task')

