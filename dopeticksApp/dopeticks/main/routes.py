# Contains all the routes specific to main routes - home(not logged in), dashboard(logged in)

from flask import render_template, url_for, flash, Blueprint
from dopeticks.models import Task
from flask_login import current_user, login_required
from datetime import datetime




main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@main.route("/dashboard")
@login_required             # Needed for routes that can only be accessed after login
def dashboard():
    dateToday = datetime.today()
    overdue = Task.query.filter(Task.userID == current_user.id, Task.taskDue < dateToday).count()
    overdueTasks = Task.query.filter(Task.userID == current_user.id, Task.taskDue < dateToday).order_by(Task.taskDue)
    tasks = Task.query.filter(Task.userID==current_user.id)
    todo = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="todo").count()
    doing = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="doing").count()
    done = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="done").count()
    todoTasks = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "todo").order_by(Task.taskDue)
    doingTasks = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "doing").order_by(Task.taskDue)
    doneTasks = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "done").order_by(Task.taskDue)
    return render_template('dashboard.html', title='Your Dopeticks Stats At A Glance', tasks=tasks, todo=todo, doing=doing, done=done,
        todoTasks=todoTasks, doingTasks=doingTasks, doneTasks=doneTasks, overdue=overdue, overdueTasks=overdueTasks)


@main.route("/test")
def test():
    return 'test'