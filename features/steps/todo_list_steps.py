from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty")
def step_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when("the user adds a task {task}")
def step_add_task(context, task):
    context.todo_manager.add_task(task)

@then("the to-do list should contain {task}")
def step_check_task(context, task):
    tasks = context.todo_manager.tasks
    assert any(task in t['description'] for t in tasks)

@given("the to-do list contains tasks:")
def step_todo_list_contains_tasks(context):
    table = context.table
    for row in table:
        task = row['Task']
        status = row['Status']
        context.todo_manager.add_task(task, status)

@given(u'the to-do list contains tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the to-do list contains tasks')


@when("the user lists all tasks")
def step_list_all_tasks(context):
    context.task_list = context.todo_manager.list_tasks()

@then("the output should contain:")
def step_check_task_list(context):
    expected_tasks = [row['Task'] for row in context.table]
    for task in expected_tasks:
        assert any(task in t for t in context.task_list)

@when("the user marks task {task} as completed")
def step_mark_completed(context, task):
    context.todo_manager.mark_task_completed(task)

@then("the to-do list should show task {task} as completed")
def step_check_completed(context, task):
    tasks = context.todo_manager.tasks
    assert any(task in t['description'] and t['completed'] for t in tasks)

@when("the user clears the to-do list")
def step_clear_list(context):
    context.todo_manager.clear_tasks()

@then("the to-do list should be empty")
def step_check_empty_list(context):
    assert len(context.todo_manager.tasks) == 0

@when("the user adds tasks {task_list}")
def step_add_multiple_tasks(context, task_list):
    tasks = task_list.split(" and ")
    context.todo_manager.add_task(*tasks)

@when("the user marks tasks {task_list} as completed")
def step_mark_multiple_completed(context, task_list):
    tasks = task_list.split(" and ")
    context.todo_manager.mark_task_completed(*tasks)
