from behave import given, when, then
from todo_list import ToDoList

# ESCENARIO 1: Agregar una tarea
@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t.description for t in context.todo.list_tasks()]
    assert task in tasks


# ESCENARIO 2 y 4: Compartimos esta función para cargar tareas desde tabla
@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.task_output = context.todo.list_tasks()

@then('the output should contain:')
def step_impl(context):
    output_descriptions = [task.description for task in context.task_output]
    expected_descriptions = [row['Task'] for row in context.table]
    for task in expected_descriptions:
        assert task in output_descriptions

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.list_tasks()) == 0


# ESCENARIO 3: Marcar una tarea como completada
@given('the to-do list contains a task "{task}" that is pending')
def step_impl(context, task):
    context.todo = ToDoList()
    context.todo.add_task(task)

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.todo.list_tasks():
        if t.description == task:
            assert t.completed is True


# ESCENARIO 5: Eliminar una tarea
@given('the to-do list contains a task "{task}"')
def step_impl(context, task):
    context.todo = ToDoList()
    context.todo.add_task(task)

@when('the user deletes the task "{task}"')
def step_impl(context, task):
    context.todo.delete_task(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    tasks = [t.description for t in context.todo.list_tasks()]
    assert task not in tasks


# ESCENARIO 6: Editar el nombre de una tarea
@when('the user edits task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    context.todo.edit_task(old_task, new_task)

