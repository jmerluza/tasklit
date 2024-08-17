
class TaskSettings:
    """Task Settings scripting object."""
    def __init__(self, task_definition):
        self.task_def = task_definition
        self.task_settings = self.task_def.Settings
    
    def get_task_settings(self) -> dict:
        """Get the settings of a task.
        
        Setting Values:
            `AllowDemandStart`: Gets or sets a boolean value that indicates that the task can be started by using either the run command of the context menu.
            `Enabled`: Gets or sets a boolean value that indicates that the task is enabled. The task can be performed only when this setting is True.
            `Hidden`: Gets or sets a boolean value that indicates that the task will not be visible in the UI. However, admins can override this setting through the use of a 'master switch' that makes all tasks visible in the UI.
            `RestartInterval`: Gets or sets a value that specifies how long the task scheduler will attempt to restart the task.
            `RestartCount`: Gets or sets the number of times that the task scheduler will attempt to restart the task.
            `ExecutionTimeLimit`: Gets or sets the amount of time allowed to complete the task.
            `MultipleInstances`: Gets or sets the policy that defines how the task scheduler deals with multiple instances of the task. 
        """
        settings = {
            "AllowDemandStart": self.task_settings.AllowDemandStart,
            "Enabled": self.task_settings.Enabled,
            "Hidden": self.task_settings.Hidden,
            "RestartInterval": self.task_settings.RestartInterval,
            "RestartCount": self.task_settings.RestartCount,
            "ExecutionTimeLimit": self.task_settings.ExecutionTimeLimit,
            "MultipleInstances": self.task_settings.MultipleInstances
        }

        return settings
    
    def update_task_settings(
        self,
        allow_demand_start: bool,
        enabled: bool,
        hidden: bool,
        restart_interval: bool,
        restart_count: bool,
        execution_time_limit: bool,
        multiple_instances: bool
    ):
        """Updates the settings of a task."""
        self.task_settings.AllowDemandStart = allow_demand_start
        self.task_settings.Enabled = enabled
        self.task_settings.Hidden = hidden
        self.task_settings.RestartInterval = restart_interval
        self.task_settings.RestartCount = restart_count
        self.task_settings.ExecutionTimeLimit = execution_time_limit
        self.task_settings.MultipleInstances = multiple_instances

        return self.task_def 
