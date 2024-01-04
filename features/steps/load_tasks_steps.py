from behave import *
from todo_list import ToDoListManager
import json
import os

@given("a list with multiples tasks")
def step_given_list_with_tasks(context):
    context.todo_manager = ToDoListManager()
    context.todo_manager.add_task("Task 1", "Task 2", "Task 3")

@when("the user saves the tasks to a file")
def step_when_user_saves_tasks_to_file(context):
    context.filename = "saved_tasks.json"
    try:
        context.todo_manager.save_tasks(context.filename)
    except Exception as e:
        context.save_error = str(e)

@then("the tasks should be saved successfully")
def step_then_tasks_saved_successfully(context):
    assert os.path.exists(context.filename), "Saved tasks file does not exist."
    
    with open(context.filename, 'r') as file:
        saved_tasks = json.load(file)

    assert len(saved_tasks) == len(context.todo_manager.tasks), "Mismatch in the number of tasks."
    
    for saved_task, original_task in zip(saved_tasks, context.todo_manager.tasks):
        assert saved_task["description"] == original_task["description"], "Task description mismatch."
        assert saved_task["completed"] == original_task["completed"], "Task completion status mismatch."

@then("the saved tasks file should contain the tasks")
def step_then_saved_tasks_file_contains_tasks(context):
    assert os.path.exists(context.filename), "Saved tasks file does not exist."

    with open(context.filename, 'r') as file:
        saved_tasks = json.load(file)

    assert len(saved_tasks) == len(context.todo_manager.tasks), "Mismatch in the number of tasks."
    
    for saved_task, original_task in zip(saved_tasks, context.todo_manager.tasks):
        assert saved_task["description"] == original_task["description"], "Task description mismatch."
        assert saved_task["completed"] == original_task["completed"], "Task completion status mismatch."
