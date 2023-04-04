Feature: User login and task management

  Scenario: User logs in and creates a task
    Given the user is on the login page
    When the user enters valid login credentials and clicks login
    Then the user is redirected to the task creation page
    When the user enters task details and clicks submit
    Then the task is created and displayed on the task list page

  Scenario: User logs in and views their tasks
    Given the user is on the login page
    When the user enters valid login credentials and clicks login
    Then the user is redirected to the task list page
    When the user clicks on a task
    Then the task details are displayed

  Scenario: User logs in and edits a task
    Given the user is on the login page
    When the user enters valid login credentials and clicks login
    Then the user is redirected to the task list page
    When the user clicks on a task
    Then the task details are displayed
    When the user clicks the edit button and enters new task details
    Then the task details are updated

  Scenario: User logs in and deletes a task
    Given the user is on the login page
    When the user enters valid login credentials and clicks login
    Then the user is redirected to the task list page
    When the user clicks on a task
    Then the task details are displayed
    When the user clicks the delete button
    Then the task is deleted

  Scenario: User logs in and logs out
    Given the user is on the login page
    When the user enters valid login credentials and clicks login
    Then the user is redirected to the task list page
    When the user clicks the logout button
    Then the user is redirected to the login page

