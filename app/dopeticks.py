# Contains the actual python code that will import the app and start the development server.

from flask import Flask



@app.route("/")
# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

@app.route("/testpage")
def testpage():
    return "<h1> Gods this is hard</h1>"


# runs the app and allows us to see changes without having to restart the server
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()