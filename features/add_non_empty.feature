Feature: ToDo List Management

    Scenario: The list has more than {element} task
        Given a non-empty list
        When the user adds one task "New Task"
        Then the list has more than 1 task

