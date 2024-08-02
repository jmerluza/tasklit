from dataclasses import dataclass


@dataclass
class SuccessErrorCodes:
    SUCCESS = 0  # The operation completed successfully (often means the task ran without errors).
    GENERAL_FAILURE = 1  # Incorrect function (general failure, often indicating some error but not very specific).
    FILE_NOT_FOUND = 2  # The system cannot find the file specified (often means the script or executable could not be found).
    ENVIRON_FAILURE = 10  # The environment is incorrect (often means there was an issue with the system environment).
    NOT_YET_RUN = 267011  # (0x00041303) The task has not yet run.
    SCHEDULER_FAILURE = (
        2147750687  # (0x8004131F) The task scheduler service is not available.
    )
    DEVICE_FAILURE = 2147943645  # (0x80070015) The device is not ready.
    SYSTEM_FAILURE = (
        2147942402  # (0x80070002) The system cannot find the file specified.
    )


@dataclass
class TaskStates:
    UNKNOWN = 0
    DISABLES = 1
    QUEUED = 2
    READY = 3
    RUNNING = 4


@dataclass
class TriggerCadence:
    TASK_TRIGGER_EVENT = 0  # Triggers a task when a specific event occurs.
    TASK_TRIGGER_TIME = 1  # Triggers a task at a specific time of day.
    TASK_TRIGGER_DAILY = 2  # Triggers a task on a daily schedule. For example, the task starts at a specific time every day, every-other day, every third day, and so on.
    TASK_TRIGGER_WEEKLY = 3  # Triggers a task on a weekly schedule. For example, tFhe task starts at 8:00 am on a specific day every week or other week.
    TASK_TRIGGER_MONTHLY = 4  # Triggers a task on a monthly schedule. For example, the task starts on specific days of specific months.
    TASK_TRIGGER_MONTHLYDOW = 5  # Triggers a task on a monthly day-of-week schedule. For example, the task starts on a specifc days of the week, weeks of the month, and months of the year.


@dataclass
class WeeklyDaysOfWeek:
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 4
    WEDNESDAY = 8
    THURSDAY = 16
    FRIDAY = 32
    SATURDAY = 64
