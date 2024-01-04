from behave import *
from todo_list import ToDoListManager

def before_scenario(context):
    context.todo_manager = ToDoListManager()

@given("a list contains tasks")
def step_given_list_contains_tasks(context):
    context.todo_manager = ToDoListManager()
    context.todo_manager.add_task("Pay bills")
    context.todo_manager.add_task("Shopping")
    context.todo_manager.add_task("Planning trip")

@given("index {idx} entered by the user")
def step_given_index_entered_by_user(context, idx):
    context.idx = int(idx)

@when("the user deletes one of the tasks")
def step_when_user_deletes_one_task(context):
    context.deleted_task = context.todo_manager.delete_task(context.idx)

@then("the title task is {title}")
def step_then_title_task_is(context, title):
    assert context.deleted_task["description"] == title, f"Expected task title '{title}', but found '{context.deleted_task['description']}'."
