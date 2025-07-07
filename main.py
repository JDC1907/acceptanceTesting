from todo_list import ToDoList

def print_tasks(todo):
    print("\n--- Lista de tareas actual ---")
    if not todo.list_tasks():
        print("No hay tareas.")
    for task in todo.list_tasks():
        estado = "Completada" if task.completed else "Pendiente"
        print(f"- {task.description} [{estado}]")
    print("------------------------------\n")


if __name__ == "__main__":
    todo = ToDoList()

    # Agregar tareas
    todo.add_task("Comprar leche")
    todo.add_task("Estudiar para el examen")
    print("Se agregaron 2 tareas.")
    print_tasks(todo)

    # Listar tareas
    print("Listar tareas (solo imprime, ya lo hicimos arriba):")
    print_tasks(todo)

    # Marcar como completada
    todo.mark_task_completed("Comprar leche")
    print("Se marcó 'Comprar leche' como completada.")
    print_tasks(todo)

    # Borrar una tarea
    todo.delete_task("Estudiar para el examen")
    print("Se eliminó 'Estudiar para el examen'.")
    print_tasks(todo)

    # Editar tarea
    todo.add_task("Leer libro")
    todo.edit_task("Leer libro", "Leer el capítulo 5 del libro")
    print("Se editó 'Leer libro' a 'Leer el capítulo 5 del libro'.")
    print_tasks(todo)

    # Limpiar toda la lista
    todo.clear_tasks()
    print("Se limpiaron todas las tareas.")
    print_tasks(todo)
