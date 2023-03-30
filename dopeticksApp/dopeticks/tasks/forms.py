# Creating HTML forms with classes from flask_wtf

from flask_wtf import FlaskForm				# Provides form validation functionality				
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField, DateField
from wtforms.validators import DataRequired




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

