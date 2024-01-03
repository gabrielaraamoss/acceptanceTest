Feature: To-Do List Manager

Scenario: Add multiple tasks to the to-do list
  Given the to-do list is empty
  When the user adds a task "Buy groceries"
  And the user adds a task "Finish work"
  Then the to-do list should contain "Buy groceries"
  And the to-do list should contain "Finish work"

Scenario: Mark multiple tasks as completed
  Given the to-do list contains tasks:
    | Task           | Status  |
    | Buy groceries  | Pending |
    | Finish work    | Pending |
  When the user marks task "Buy groceries" as completed
  And the user marks task "Finish work" as completed
  Then the to-do list should show task "Buy groceries" as completed
  And the to-do list should show task "Finish work" as completed

