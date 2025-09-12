def task_manager():
    tasks = {}

    def add_task(name, status="incomplete"):
        tasks[name] = status

    def get_tasks():
        return tasks.copy()

    def complete_task(name):
        if name in tasks:
            tasks[name] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }