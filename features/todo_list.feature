Feature: To-Do List Manager
  The system should allow users to manage their tasks easily through a command-line interface.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      | Buy groceries|
      | Pay bills    |

  Scenario: Mark a task as completed
    Given the to-do list contains a task "Buy groceries" that is pending
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario Clear the entire to-do list:
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Delete a task by name
    Given the to-do list contains a task "Buy groceries"
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"

  Scenario: Edit a task name
    Given the to-do list contains a task "Do homework"
    When the user edits task "Do homework" to "Do math homework"
    Then the to-do list should contain "Do math homework"
