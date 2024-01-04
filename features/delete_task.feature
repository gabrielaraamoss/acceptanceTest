Feature: ToDo List Management

  Scenario: Deleting one task from a list
    Given a list contains tasks
    And index 2 entered by the user
    When the user deletes one of the tasks
    Then the title task is Shopping
