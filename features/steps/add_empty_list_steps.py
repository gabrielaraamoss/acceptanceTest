from behave import *
from todo_list import ToDoListManager

def before_scenario(context):
    context.todo_manager = ToDoListManager()

@given("an empty to-do list")
def step_given_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when("the user adds a task {task_name}")
def step_when_add_task(context, task_name):
    context.todo_manager.add_task(task_name)

@then("the to-do list has {element} task")
def step_then_todo_list_has_element_task(context, element):
    assert int(element) == len(context.todo_manager.tasks)
