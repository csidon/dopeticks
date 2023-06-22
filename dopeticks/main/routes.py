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
    context = dict()
    dateToday = datetime.today()
    # Getting all tasks that are "todo" and "not archived"
    alltasksdone = Task.query.filter(Task.userID==current_user.id,Task.taskStatus!="archived", Task.taskStatus=="done")
    alltasksnotdone = Task.query.filter(Task.userID==current_user.id,Task.taskStatus!="archived", Task.taskStatus!="done")
    todo = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="todo")
    doing = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="doing")
    done = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="done")
    archived = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="archived")
    overdue = Task.query.filter(Task.userID == current_user.id, Task.taskDue < dateToday, Task.taskStatus != "archived")
    print("alltasksnotdone = " + str(alltasksnotdone.count()))
    print("todo = " + str(todo.count()))
    print("doing = " + str(doing.count()))
    print("done = " + str(done.count()))
    print("archived = " + str(archived.count()))
    print("overdue = " + str(overdue.count()))




    context['defaults'] = alltasksdone.count() + alltasksnotdone.count()
    notdone = alltasksnotdone.order_by(Task.taskDue)
    alldone = alltasksdone.order_by(Task.taskDue)
    context['defaultTasks'] = notdone.union_all(alldone)
    context['todo'] = todo.count()
    context['todoTasks'] = todo.order_by(Task.taskDue)
    context['doing'] = doing.count()
    context['doingTasks'] = doing.order_by(Task.taskDue)
    context['done'] = done.count()
    context['doneTasks'] = done.order_by(Task.taskDue)
    context['archived'] = archived.count()
    context['archivedTasks'] = archived.order_by(Task.taskDue)
    context['overdue'] = overdue.count()
    context['overdueTasks'] = overdue.order_by(Task.taskDue)



    # context['overdue'] = Task.query.filter(Task.userID == current_user.id, Task.taskDue < dateToday, Task.taskStatus != "archived").count()
    # context['overdueTasks'] = Task.query.filter(Task.userID == current_user.id, Task.taskDue < dateToday, Task.taskStatus != "archived").order_by(Task.taskDue)
    # context['tasks'] = Task.query.filter(Task.userID==current_user.id, Task.taskStatus != "archived")
    # context['todo'] = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="todo", Task.taskStatus != "archived").count()
    # context['doing'] = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="doing", Task.taskStatus != "archived").count()
    # context['done'] = Task.query.filter(Task.userID==current_user.id,Task.taskStatus=="done", Task.taskStatus != "archived").count()
    # context['todoTasks'] = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "todo", Task.taskStatus != "archived").order_by(Task.taskDue)
    # context['doingTasks'] = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "doing", Task.taskStatus != "archived").order_by(Task.taskDue)
    # context['doneTasks'] = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "done", Task.taskStatus != "archived").order_by(Task.taskDue)
    # context['archivedTasks'] = Task.query.filter(Task.userID == current_user.id, Task.taskStatus == "archived").order_by(Task.taskDue)
    return render_template('dashboard.html', title='Your Dopeticks Stats At A Glance', context=context)

@main.route("/test")
def test():
    return 'test'