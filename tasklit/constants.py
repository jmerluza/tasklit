from dataclasses import dataclass

@dataclass
class TaskCreation:
    """
    Task logon types. API reference can be found here:
    https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder-registertask

    Attributes:
        TASK_VALIDATE_ONLY:
            The Task Scheduler checks the syntax of the XML that describes the task but does not \
            register the task. This constant cannot be combined with the TASK_CREATE, \
            TASK_UPDATE, or TASK_CREATE_OR_UPDATE value

        TASK_CREATE:
            The Task Scheduler registers the task as a new task.

        TASK_UPDATE:
            The Task Scheduler registers the task as an updated version of an existing task. When \
            a task with a registration trigger is updated, the task will \
            execute after the update occurs.

        TASK_CREATE_OR_UPDATE:
            The Task Scheduler either registers the task as a new task or as an updated version \
            if the task already exists. Equivalent to TASK_CREATE | TASK_UPDATE.
        
        TASK_DISABLE:
            The Task Scheduler disables the existing task.

        TASK_DONT_ADD_PRINCIPAL_ACE:
            The Task Scheduler is prevented from adding the allow access-control entry (ACE) \
            for the context principal. When the TaskFolder.RegisterTask function is called with \
            this flag to update a task, the Task Scheduler service does not add the ACE for the \
            new context principal and does not remove the ACE from the old context principal.

        TASK_IGNORE_REGISTRATION_TRIGGERS:
            The Task Scheduler creates the task, but ignores the registration triggers in the \
            task. By ignoring the registration triggers, the task will not execute when it is \
            registered unless a time-based trigger causes it to execute on registration.
    """
    TASK_VALIDATE_ONLY = 1
    TASK_CREATE = 2
    TASK_UPDATE = 4
    TASK_CREATE_OR_UPDATE = 6
    TASK_DISABLE = 8
    TASK_DONT_ADD_PRINCIPAL_ACE = 16
    TASK_IGNORE_REGISTRATION_TRIGGERS = 32

@dataclass
class TaskLogon:
    """
    Task logon types. API reference can be found here:
    https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder-registertask

    Attributes:
        TASK_LOGON_NONE:
            The logon method is not specified. Used for non-NT credentials.

        TASK_LOGON_PASSWORD:
            Use a password for logging on the user. The password must be supplied at \
            registration time.

        TASK_LOGON_S4U:
            Use an existing interactive token to run a task. The user must log on \
            using a service for user (S4U) logon. When an S4U logon is used, no \
            password is stored by the system and there is no access to either the \
            network or to encrypted files.

        TASK_LOGON_INTERACTIVE_TOKEN:
            User must already be logged on. The task will be run only in an \
            existing interactive session.

        TASK_LOGON_GROUP:
            Group activation. The groupId field specifies the group.

        TASK_LOGON_SEVICE_ACCOUNT:
            Indicates that a Local System, Local Service, or Network Service \
            account is being used as a security context to run the task.

        TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD
            First use the interactive token. If the user is not logged on \
            (no interactive token is available), then the password is used. The password must be \
            specified when a task is registered. This flag is not recommended for new tasks \
            because it is less reliable than TASK_LOGON_PASSWORD.
    """
    TASK_LOGON_NONE = 0
    TASK_LOGON_PASSWORD = 1
    TASK_LOGON_S4U = 2
    TASK_LOGON_INTERACTIVE_TOKEN = 3
    TASK_LOGON_GROUP = 4
    TASK_LOGON_SERVICE_ACCOUNT = 5
    TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD = 6

@dataclass
class ActionTypes:
    """
    Task action types. API reference can be found here: 
    https://learn.microsoft.com/en-us/windows/win32/taskschd/action-type

    Attributes:
        TASK_ACTION_EXEC:
            This action performs a command-line operation. For example, the action could run a 
            script, launch an executable, or, if the name of a document is provided, find its 
            associated application and launch the application with the document.
        TASK_ACTION_COM_HANDLER:
            This action fires a handler.
        TASK_ACTION_SEND_EMAIL:
            This action sends an email message.
        TASK_ACTION_SHOW_MESSAGE:
            This action shows a message box.
                        
    """
    TASK_ACTION_EXEC = 0
    TASK_ACTION_COM_HANDLER = 5
    TASK_ACTION_SEND_EMAIL = 6
    TASK_ACTION_SHOW_MESSAGE = 7

TASK_RESULTS = {
    0:"Operation completed successfully.",
    1:"General failure.",
    2:"The system cannot find the file specified.",
    10:"System environment failure.",
    267011:"The task has not yet run.",
    2147750687:"Task scheduler is not available.",
    2147943645:"The device is not ready.",
    267009:"Task is currently running."
}

TASK_STATES = {
    0:"UNKNOWN",
    1:"DISABLED",
    2:"QUEUED",
    3:"READY",
    4:"RUNNING"
}

TASK_TRIGGERS = {
    "Event":0, # Triggers a task when a specific event occurs.
    "Time":1, # Triggers a task at a specific time of day.
    "Daily":2, # Triggers a task on a daily schedule. For example, the task starts at a specific time every day, every-other day, every third day, and so on.
    "Weekly":3, # Triggers a task on a weekly schedule. For example, the task starts at 8:00 am on a specific day every week or other week.
    "Monthly":4, # Triggers a task on a monthly schedule. For example, the task starts on specific days of specific months.
    "Monthly DOW":5 # Triggers a task on a monthly day-of-week schedule. For example, the task starts on a specifc days of the week, weeks of the month, and months of the year.
}

DAYS_OF_WEEK = {
    "Sunday":1,
    "Monday":2,
    "Tuesday":4,
    "Wednesday":8,
    "Thursday":16,
    "Friday":32,
    "Saturday":64
}

TASK_INSTANCES_POLICY = {
    0:"Starts a new instance while an existing instance of the task is running.",
    1:"Starts a new instance of the task after all other instances of the task are complete.",
    2:"Does not start a new instance if an existing instance of the task is running.",
    3:"Stops an existing instance of the task before it starts a new instance."
}