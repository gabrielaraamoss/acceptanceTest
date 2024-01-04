Feature: ToDo List Management

    Scenario: Deleting all tasks from a list
        Given a list with tasks
        When the user deletes all the tasks
        Then the list is empty
