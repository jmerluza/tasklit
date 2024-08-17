

class TaskDefinition:
    """TaskDefinition scripting object."""
    def __init__(self, scheduler_client):
        self.scheduler = scheduler_client

    def get_task_definition(self, folder_obj, task_name: str):
        """Get task definition by task name.
        
        Parameters:
            folder_obj (`win32com.client.CDispatch`): Folder object.
            task_name (`str`): Name of task within the folder.

        Examples:
            >>> from tasklit.functions.functions import connect_to_task_scheduler
            >>> # Connect to Task Scheduler service
                scheduler = connect_to_task_scheduler()

            >>> # Access the root folder (change to subfolder path if needed)
                root_folder = scheduler.GetFolder("Jalen_Tasks")

            >>> # Task name to modify (replace with your task's name)
                task_name = "Test"

            >>> task_definition = TaskDefinition(scheduler).get_task_definition(root_folder, task_name)
        """
        try:
            task = folder_obj.GetTask(task_name)
            task_definition = task.Definition
            return task_definition
        except Exception:
            print("Please verify task name exists.")
        
    def create_task_definition(self):
        """Create a new task definition. Used for creating a new task."""
        task_definition = self.scheduler.NewTask(0)
        return task_definition
    


    