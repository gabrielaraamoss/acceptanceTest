Feature: ToDo List Management

  Scenario: Saving tasks to a file
    Given a list with tasks
    When the user saves the tasks to a file
    Then the tasks should be saved successfully
    And the saved tasks file should contain the tasks
