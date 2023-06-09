# Contains all the routes specific to users - register, login, logout, account

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from dopeticks import db, bcrypt
from dopeticks.models import User
from dopeticks.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from dopeticks.users.utils import saveImage



users = Blueprint('users', __name__)

@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()

    if form.validate_on_submit():
        # Using Bcrypt to hash the password so that we don't store passwords in plain text
        hashedPW = bcrypt.generate_password_hash(form.userPassword.data).decode('utf-8')
        # Create an object user with the data collected from the form, passing in the hashed password (instead of cleartext) 
        user = User(userEmail=form.userEmail.data, userLastName=form.userLastName.data, userFirstName=form.userFirstName.data, userPassword=hashedPW)
        db.session.add(user)        # Adds user to db
        db.session.commit()         # Commits user to db
        flash('Your account has been created. Please log into your account', 'success')
        return redirect(url_for('users.login'))

    errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []
    return render_template('register.html', title='Sign up for your Dopeticks Account!', form=form, errors=errors)

@users.route("/login", methods=['GET','POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userEmail=form.userEmail.data).first()
        # Decrypt the password hash and check it against the users' password in the database
        # If they match, log the user in and remember their "remember me " choice
        if user and bcrypt.check_password_hash(user.userPassword, form.userPassword.data):
            login_user(user, remember=form.userRemember.data)
            # If the user has been trying to access a specific page before logging in, redirect them to that page. Otherwise redirect them to home
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
            return render_template('login.html', title='Log into your Dopeticks Account!', form=form)
    # errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []        
    return render_template('login.html', title='Log into your Dopeticks Account!', form=form)


@users.route("/logout")
def logout():
    # Uses flask-login's logout_user function
    logout_user()
    return redirect(url_for('main.home')) 

@users.route("/account", methods=['GET','POST'])
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
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.userFirstName.data = current_user.userFirstName
        form.userLastName.data = current_user.userLastName
        form.userEmail.data = current_user.userEmail

    userImage = url_for('static', filename='profilePics/' + current_user.userImage)
    return render_template('account.html', title='Your Dopeticks User Account', userImage=userImage, form=form)