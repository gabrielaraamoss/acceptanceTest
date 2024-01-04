from behave import *
from todo_list import ToDoListManager


def before_scenario(context):
    context.todo_manager = ToDoListManager()

@given("a non-empty list")
def step_given_non_empty_list(context):
    todo_list = ToDoListManager()
    todo_list.add_task("Buy groceries")
    context.task_list = todo_list


@when("the user adds one task {task_name}")
def step_when_add_one_task(context, task_name):
    context.task_list.add_task(task_name)


@then("the list has more than {element} task")
def step_then_list_has_more_than_element_task(context, element):
    assert int(element) < len(context.task_list.tasks)
