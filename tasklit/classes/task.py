

class ExistingTask:
    def __init__(self, scheduler_client):
        self.scheduler = scheduler_client

    def update_task(self, folder_obj, task_definition, task_name: str):
        """Updating a task."""

        folder_obj.RegisterTaskDefinition(
            task_name,
            task_definition,
            6,
            None,
            None,
            3
        )
        