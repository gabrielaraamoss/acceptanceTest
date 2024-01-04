from behave import *
from todo_list import ToDoListManager

def before_scenario(context):
    context.todo_manager = ToDoListManager()

@given("a list with tasks")
def step_given_list_with_tasks(context):
    context.task_list = ToDoListManager()
    context.task_list.add_task("Pay bills")
    context.task_list.add_task("Shopping")
    context.task_list.add_task("Planning trip")

@when("the user deletes all the tasks")
def step_when_user_deletes_all_tasks(context):
    context.task_list.clean_tasks()

@then("the list is empty")
def step_then_list_is_empty(context):
    assert 0 == len(context.task_list.tasks), f"Expected an empty list, but found {len(context.task_list.tasks)} tasks."

