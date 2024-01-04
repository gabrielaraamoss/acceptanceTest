Feature: ToDo List Management

  Scenario: Adding a task to an empty to-do list
    Given an empty to-do list
    When the user adds a task "Buy groceries"
    Then the to-do list has 1 task
