# Contains all the routes specific to tasks - newTask, task
#****** To change task to createUpdateTask


from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from dopeticks import db
from dopeticks.tasks.forms import TaskForm
from dopeticks.models import User, Task
from flask_login import current_user, login_required


tasks = Blueprint('tasks', __name__)

@tasks.route("/task/new", methods=['GET','POST'])
@login_required             # Needed for routes that can only be accessed after login
def newTask():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(taskTitle=form.taskTitle.data, taskDescription=form.taskDescription.data, userID=current_user.id, owner=current_user, 
            taskDue=form.taskDue.data, taskStatus=form.taskStatus.data)
        db.session.add(task)
        db.session.commit()
        flash('New Task Created!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('createTask.html', title='New Task', form=form, legend="New Task")


@tasks.route("/task/<int:taskID>/update", methods=['GET','POST'])
@login_required 
def updateTask(taskID):
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
            return redirect(url_for('main.dashboard'))
            
        else:
            task.taskTitle = form.taskTitle.data
            task.taskDescription = form.taskDescription.data
            task.taskDue = form.taskDue.data
            task.taskStatus = form.taskStatus.data
            db.session.commit()
            flash('Your task has been updated', 'success')
            return redirect(url_for('main.dashboard'))

    elif request.method == 'GET':
        form.taskTitle.data = task.taskTitle
        form.taskDescription.data = task.taskDescription
        form.taskDue.data = task.taskDue
        form.taskStatus.data = task.taskStatus

    return render_template('createTask.html', title='Update Task', form=form, task=task, legend="Update Task")