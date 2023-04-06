from behave import *
from datetime import datetime, timedelta
from dopeticks import db, bcrypt
from dopeticks.models import User, Task
from flask_login import current_user

use_step_matcher("parse")

@given("the user is not logged in")
def step_impl(context):
    context.client.get('/logout')

@given("the user is logged in")
def step_impl(context):
    with context.application.test_client() as client:
        client.post('/login', data=dict(email='testuser1@example.com', password='testpassword'), follow_redirects=True)

@when("the user navigates to the homepage")
def step_impl(context):
    response = context.client.get('/')
    assert response.status_code == 200

@when('the user navigates to the "{page}" page')
def step_impl(context, page):
    response = context.client.get('/' + page.lower())
    assert response.status_code == 200

@when('the user creates a new task with the title "{title}", description "{description}", priority "{priority}", and due date "{due_date}"')
def step_impl(context, title, description, priority, due_date):
    with context.application.test_client() as client:
        due_date = datetime.strptime(due_date, "%m/%d/%Y %I:%M %p")
        response = client.post('/tasks/create', data=dict(
            title=title, description=description, priority=priority, due_date=due_date
        ), follow_redirects=True)
        assert response.status_code == 200
        assert b'Task created!' in response.data

@when('the user completes the task with the title "{title}"')
def step_impl(context, title):
    task = Task.query.filter_by(taskTitle=title).first()
    task.taskStatus = 'done'
    db.session.commit()

@when('the user updates the task with the title "{title}" to have a priority of "{priority}"')
def step_impl(context, title, priority):
    task = Task.query.filter_by(taskTitle=title).first()
    task.taskPriority = priority
    db.session.commit()

@when('the user deletes the task with the title "{title}"')
def step_impl(context, title):
    task = Task.query.filter_by(taskTitle=title).first()
    db.session.delete(task)
    db.session.commit()

@then('the user should see the task with the title "{title}" displayed on the "{page}" page')
def step_impl(context, title, page):
    response = context.client.get('/' + page.lower())
    assert response.status_code == 200
    assert bytes(title, 'utf-8') in response.data

@then('the user should not see the task with the title "{title}" displayed on the "{page}" page')
def step_impl(context, title, page):
    response = context.client.get('/' + page.lower())
    assert response.status_code == 200
    assert bytes(title, 'utf-8') not in response.data

@then('the user should see the updated priority of the task with the title "{title}" on the "{page}" page')
def step_impl(context, title, page):
    response = context.client.get('/' + page.lower())
    assert response.status_code == 200
    task = Task.query.filter_by(taskTitle=title).first()
    assert bytes(task.taskPriority, 'utf-8') in response.data

@then('the user should see a message indicating that the task with the title "{title}" has been completed')
def step_impl(context, title):
    response = context.client.get('/tasks')
    assert response.status_code == 200
