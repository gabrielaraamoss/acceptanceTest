from behave import *
from todo_list import ToDoListManager

def before_scenario(context):
    context.todo_manager = ToDoListManager()

@given("a list with one task")
def step_given_list_with_one_task(context):
    context.task_list = ToDoListManager()
    context.task_list.add_task("Buy groceries")

@given("users enter index {idx}")
def step_given_users_enter_index(context, idx):
    context.user_index = int(idx)

@when("the user marks it as complete")
def step_when_user_marks_as_complete(context):
    context.task_list.mark_complete(context.user_index)

@then("the task's status is {status}")
def step_then_task_status_is(context, status):
    task_index = context.user_index - 1
    if 0 <= task_index < len(context.task_list.tasks):
        task_status = "Completed" if context.task_list.tasks[task_index]["completed"] else "Pending"
        assert status == task_status, f"Expected task status '{status}', but found '{task_status}'."
    else:
        assert False, f"Invalid task index: {context.user_index}"

