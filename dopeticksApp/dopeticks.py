from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

# Set a secret key to prevent against modifying cookies and XSS requests on forms
app.config['SECRET_KEY'] = '16de15a4bf6314e0badd358db742206261ccee1b5222fb8e'
# format for the URI is postgresql://{user}:{password}@{RDS endpoint}/{db name, default is postgres}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresmaster:1NewPass!@dopeticks-db-v02.chcal2ivuvcc.us-west-2.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



app.app_context().push()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userEmail = db.Column(db.String(120), unique=True, nullable=False)
    # A hash will be generated for userImage to be 20 Char, and userPass as 60 Char
    userImage = db.Column(db.String(20), nullable=False, default='default.jpg')
    userPassword = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.userEmail}', '{self.userPassword}', '{self.userImage}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskTitle = db.Column(db.String(180), nullable=False)
    taskDescription = db.Column(db.Text, nullable=False)
    taskStatus = db.Column(db.Integer, nullable=False, default='0')
    taskPriority = db.Column(db.Integer, nullable=False, default='3')
    taskDue = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Task('{self.taskTitle}', '{self.taskStatus}', '{self.taskPriority}', '{self.taskDue}')"


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
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.userFirstName.data}!', 'success')
        return redirect(url_for('home'))

    errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []
    return render_template('register.html', title='Sign up for your Dopeticks Account!', form=form, errors=errors)

@app.route("/login", methods=['GET','POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.userEmail.data == "test@test.com" and form.userPassword.data == 'password':
            flash("You're logged in!", 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    # errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []        
    return render_template('login.html', title='Log into your Dopeticks Account!', form=form)

@app.route("/profile")
def profile():
    return render_template('about.html', title='Profile')



if __name__ == '__main__':
    app.run(debug=True)