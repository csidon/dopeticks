from datetime import datetime       # Manages datetime issues
from dopeticks import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def loadUser(userID):
    return User.query.get(int(userID))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    userFirstName = db.Column(db.String(100), nullable=False)
    userLastName = db.Column(db.String(100), nullable=False)
    userEmail = db.Column(db.String(120), unique=True, nullable=False)
    # A hash will be generated for userImage to be 20 Char, and userPass as 60 Char
    userImage = db.Column(db.String(20), nullable=False, default='default.jpg')
    userPassword = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.userEmail}', '{self.userPassword}', '{self.userImage}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskTitle = db.Column(db.String(180), nullable=False)
    taskDescription = db.Column(db.Text, nullable=False)
    taskStatus = db.Column(db.String, nullable=True, default='todo')
    taskPriority = db.Column(db.String, nullable=True, default='normal')
    taskDue = db.Column(db.DateTime, nullable=True, default=datetime.now)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        # return f"Task('{self.taskTitle}', '{self.taskStatus}', '{self.taskPriority}', '{self.taskDue}')"
        return f"Task('{self.taskTitle}', '{self.taskDescription}', '{self.taskStatus}','{self.taskDue}','{self.taskPriority}')"


