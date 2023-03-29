import os
import secrets              # Package that generates a random hex value
from PIL import Image       # Pillow package that helps to resize image
from flask import render_template, url_for, flash, redirect, request, abort
from dopeticks import app, db, bcrypt
from dopeticks.forms import RegistrationForm, LoginForm, UpdateAccountForm, TaskForm
from dopeticks.models import User, Task
from flask_login import login_user, current_user, logout_user, login_required



# tasks = [
#     {
#         'taskTitle' : 'Set up dopeticks structure',
#         'taskDescription' : 'Need to do this yo',
#         'taskStatus' : 'Ongoing',
#         'taskPriority' : 'Urgent',
#         'taskDue' : '21 Mar 2023'
#     }

# ]


@app.route("/")
@app.route("/home")
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        # Using Bcrypt to hash the password so that we don't store passwords in plain text
        hashedPW = bcrypt.generate_password_hash(form.userPassword.data).decode('utf-8')
        # Create an object user with the data collected from the form, passing in the hashed password (instead of cleartext) 
        user = User(userEmail=form.userEmail.data, userLastName=form.userLastName.data, userFirstName=form.userFirstName.data, userPassword=hashedPW)
        db.session.add(user)        # Adds user to db
        db.session.commit()         # Commits user to db
        flash('Your account has been created. Please log into your account', 'success')
        return redirect(url_for('login'))

    errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []
    return render_template('register.html', title='Sign up for your Dopeticks Account!', form=form, errors=errors)

@app.route("/login", methods=['GET','POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userEmail=form.userEmail.data).first()
        # Decrypt the password hash and check it against the users' password in the database
        # If they match, log the user in and remember their "remember me " choice
        if user and bcrypt.check_password_hash(user.userPassword, form.userPassword.data):
            login_user(user, remember=form.userRemember.data)
            # If the user has been trying to access a specific page before logging in, redirect them to that page. Otherwise redirect them to home
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    # errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []        
    return render_template('login.html', title='Log into your Dopeticks Account!', form=form)


@app.route("/logout")
def logout():
    # Uses flask-login's logout_user function
    logout_user()
    return redirect(url_for('home')) 


# This function saves/updates images in our database
def saveImage(formUploadedImage):
    # Renaming the image to a unique/random 8 byte hex so that there won't be any conflicting file names in the database
    randomHexImage = secrets.token_hex(8)
    # Splitting the file name from file extension so I can grab the extension and append it to my new hex value
    # I'm not using the file name variable, so I'm using '_' as a throwaway variable name
    _, fileExtension = os.path.splitext(formUploadedImage.filename)
    randomHexImage = randomHexImage + fileExtension
    # Concats the os path to the image
    imagePath = os.path.join(app.root_path, 'static/profilePics', randomHexImage)
    # Resizing image so that it's no more than 125px -- This allows us to save space and run more efficiently
    outputSize = (125, 125)
    imageThumb = Image.open(formUploadedImage)
    imageThumb.thumbnail(outputSize)
    # Saving the thumbnail image to the image path
    imageThumb.save(imagePath)
    # Returning the image for updating in the database
    return randomHexImage



@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.uploadImage.data:
            # Saving the picture and updating the database with the hex-ed filename
            hexedImage = saveImage(form.uploadImage.data)
            current_user.userImage = hexedImage

        current_user.userFirstName = form.userFirstName.data
        current_user.userLastName = form.userLastName.data
        current_user.userEmail = form.userEmail.data

        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.userFirstName.data = current_user.userFirstName
        form.userLastName.data = current_user.userLastName
        form.userEmail.data = current_user.userEmail

    userImage = url_for('static', filename='profilePics/' + current_user.userImage)
    return render_template('account.html', title='Your Dopeticks User Account', userImage=userImage, form=form)


@app.route("/dashboard")
@login_required             # Needed for routes that can only be accessed after login
def dashboard():
    return render_template('dashboard.html', title='Your Dopeticks Stats At A Glance')



# @app.route("/task/new", methods=['GET','POST'])
# @login_required             # Needed for routes that can only be accessed after login
# def newTask():
#     form = TaskForm()
#     if form.validate_on_submit():
#         flash('You have created a new task!', 'success')
#         return redirect(url_for('home'))

#     return render_template('createTask.html', title='New Task', form=form)


@app.route("/task/new", methods=['GET','POST'])
@login_required             # Needed for routes that can only be accessed after login
def newTask():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(taskTitle=form.taskTitle.data, taskDescription=form.taskDescription.data, userID=current_user.id, owner=current_user, 
            taskDue=form.taskDue.data, taskStatus=form.taskStatus.data )
        db.session.add(task)
        db.session.commit()
        flash('New Task Created!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('createTask.html', title='New Task', form=form, legend="New Task")


@app.route("/task/<int:taskID>/update", methods=['GET','POST'])
@login_required 
def task(taskID):
    task = Task.query.get_or_404(taskID)
    if task.owner != current_user:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        if form.taskStatus.data=="Done":
            # Maybe done is a separate button altogether..?
            task.taskTitle = form.taskTitle.data
            task.taskDescription = form.taskDescription.data
            task.taskDue = form.taskDue.data
            task.taskStatus = form.taskStatus.data
            db.session.commit()
            flash("OMG! You've completed a task!", 'success')
            # We should do some fancy confetti stuff here
            # Then move task to archived/done section
            return redirect(url_for('home'))
            
        else:
            task.taskTitle = form.taskTitle.data
            task.taskDescription = form.taskDescription.data
            task.taskDue = form.taskDue.data
            task.taskStatus = form.taskStatus.data
            db.session.commit()
            flash('Your task has been updated', 'success')
            return redirect(url_for('home'))



    elif request.method == 'GET':
        form.taskTitle.data = task.taskTitle
        form.taskDescription.data = task.taskDescription
        form.taskDue.data = task.taskDue
        form.taskStatus.data = task.taskStatus

    return render_template('createTask.html', title='Update Task', form=form, task=task, legend="Update Task")
