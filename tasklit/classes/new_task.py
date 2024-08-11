from datetime import datetime
from tasklit.constants import TASK_TRIGGERS, ActionTypes, TaskCreation, TaskLogon

class NewTask:
    def __init__(self, scheduler_client):
        self.scheduler = scheduler_client

    def create_task_definition(self):
        task_definition = self.scheduler.NewTask(0)
        return task_definition

    def create_task_trigger(
        self,
        task_definition,
        cadence: int,
        start_date: datetime.date,
        start_time: datetime.time,
        interval: int,
        dow: int|None=None
    ):
        """Creates the trigger for task.
        
        Parameters:
            task_definition: `create_task_definition`.
            cadence (`int`): When the task is executed. Daily, weekly, etc.
            start_date (`datetime.date`): Start date for when the task is executed.
            start_time (`datetime.time`): Start time for when the task is executed.
            interval (`int`): Intervals for when the task is executed. \
                Everyday, every other day, etc.

        """
        trigger = task_definition.Triggers.Create(TASK_TRIGGERS.get(cadence))
        trigger.StartBoundary = datetime.combine(start_date, start_time).isoformat()

        # match cadence to know which trigger interval to use.
        match cadence:
            case "Daily":
                trigger.DaysInterval = interval
            case "Weekly":
                trigger.WeeksInterval = interval
                trigger.DaysOfWeek = dow

        return trigger
    
    def create_task_action(self, task_definition, action_file: str, action_arg: str|None='/c "exit"'):
        """Creates the actions for task."""

        action = task_definition.Actions.Create(ActionTypes.TASK_ACTION_EXEC)
        action.Path = action_file
        action.Arguments = action_arg

        return action

    def create_task_information(self, task_definition, task_description: str):
        """Creates the information about the task."""
        task_definition.RegistrationInfo.Description = task_description
        task_definition.Settings.Enabled = True
        task_definition.Settings.StopIfGoingOnBatteries = False
        return task_definition

    def create_new_task(self, task_definition, folder: str, task_name: str):
        """Registers the new task with task scheduler."""
        task_folder = self.scheduler.GetFolder(folder)
        task_folder.RegisterTaskDefinition(
            task_name,
            task_definition,
            TaskCreation.TASK_CREATE_OR_UPDATE,
            "", # no username
            "", # no password
            TaskLogon.TASK_LOGON_NONE
        )

