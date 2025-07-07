class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()

    def clear_tasks(self):
        self.tasks.clear()


#: Eliminar una tarea por nombre   -- 1era funcionalidad extra
    def delete_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]


#: Eliminar una tarea por nombre   -- 2da funcionalidad extra
    def edit_task(self, old_description, new_description):
        for task in self.tasks:
            if task.description == old_description:
                task.description = new_description
                break

