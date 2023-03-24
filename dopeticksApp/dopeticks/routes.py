from flask import render_template, url_for, flash, redirect, request
from dopeticks import app, db, bcrypt
from dopeticks.forms import RegistrationForm, LoginForm
from dopeticks.models import User, Task
from flask_login import login_user, current_user, logout_user, login_required



tasks = [
    {
        'taskTitle' : 'Set up dopeticks structure',
        'taskDescription' : 'Need to do this yo',
        'taskStatus' : 'Ongoing',
        'taskPriority' : 'Urgent',
        'taskDue' : '21 Mar 2023'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', tasks=tasks)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        # Using Bcrypt to hash the password so that we don't store passwords in plain text
        hashed_pw = bcrypt.generate_password_hash(form.userPassword.data).decode('utf-8')
        # Create an object user with the data collected from the form, passing in the hashed password (instead of cleartext) 
        user = User(userEmail=form.userEmail.data, userLastName=form.userLastName.data, userFirstName=form.userFirstName.data, userPassword=hashed_pw)
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


@app.route("/profile")
def profile():
    return render_template('profile.html', title='Profile')


@app.route("/dashboard")
@login_required             # Needed for routes that can only be accessed after login
def dashboard():
    return render_template('dashboard.html', title='Your Dopeticks Stats At A Glance')