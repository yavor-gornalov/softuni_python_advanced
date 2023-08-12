from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task):
        if any([new_task.name == task.name for task in self.tasks]):
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        current_task = None
        for task in self.tasks:
            if task.name == task_name:
                current_task = task
                break

        if not current_task:
            return f"Could not find task with the name {task_name}"

        current_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                amount_of_removed_tasks += 1
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        section_tasks = "\n".join([t.details() for t in self.tasks])
        result = f"Section {self.name}:\n{section_tasks}"
        return result
