import streamlit as st

class TaskDefinition:
    """TaskDefinition scripting object."""
    def __init__(self, scheduler_client):
        self.scheduler = scheduler_client

    def get_task_definition(self, folder_name: str, task_name: str):
        """Get task definition by task name.
        
        Parameters:
            folder_name (`str`): Folder name.
            task_name (`str`): Name of task within the folder.
        """
        folder = self.scheduler.GetFolder(folder_name)
        task = folder.GetTask(task_name)
        task_definition = task.Definition
        return task_definition

    def create_task_definition(self):
        """Create a new task definition. Used for creating a new task."""
        task_definition = self.scheduler.NewTask(0)
        return task_definition
    


    