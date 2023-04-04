Feature: Automated Task Creation

  Scenario: Create a new task automatically
    Given the user is logged in
    When the system automatically creates a new task with the title "Automated Task", description "This task was created automatically", priority "High", and due date "04/30/2023 12:00 PM"
    Then the user should see the task with the title "Automated Task" displayed on the "tasks" page
