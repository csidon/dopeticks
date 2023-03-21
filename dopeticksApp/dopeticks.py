from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

# Set a secret key to prevent against modifying cookies and XSS requests on forms
app.config['SECRET_KEY'] = '16de15a4bf6314e0badd358db742206261ccee1b5222fb8e'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log into your Dopeticks Account!', form=form)

@app.route("/profile")
def profile():
    return render_template('about.html', title='Profile')



if __name__ == '__main__':
    app.run(debug=True)