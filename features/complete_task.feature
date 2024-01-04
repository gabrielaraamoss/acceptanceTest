Feature: ToDo List Management

    Scenario: Marking a task as complete
        Given a list with one task
        And users enter index 1
        When the user marks it as complete
        Then the task's status is Completed

