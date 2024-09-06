import polars as pl
from datetime import datetime, timedelta
from pytask_scheduler import TaskValueDefinitions

class TasksDataFrame(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def preprocess(self):
        """Preprocess the tasks data frame."""
        df = self.df.with_columns(
            pl.col("task_state")
            .cast(str)
            .replace(TaskValueDefinitions.TASK_STATE_DEFINITION)
            .alias("task_state_definition"),
            pl.col("last_task_result")
            .cast(str)
            .replace(TaskValueDefinitions.TASK_RESULT_DEFINITION)
            .alias("last_task_result_definition"),
            pl.col("next_run_time").cast(pl.Datetime),
            pl.col("last_run_time").cast(pl.Datetime)
        )
        return TasksDataFrame(df)

    def count_task_by_state(self, task_state: int):
        """Count the number of tasks by state."""
        return self.df.filter(pl.col("task_state")==task_state)["task_state"].count()

    def get_tasks_scheduled_by_date(self, date: datetime|None=datetime.today()):
        """Get the tasks that were last run or scheduled to run within the date."""
        MAX_HOUR = 23
        MAX_MIN = 59
        MAX_SEC = 59
        MAX_MSEC = 999999
        thour = date.hour
        tmin = date.minute
        tsec = date.second
        tmsec = date.microsecond

        lower_date = (date -
            timedelta(
                hours=thour,
                minutes=tmin,
                seconds=tsec,
                microseconds=tmsec
            )
        )

        upper_date = (date +
            timedelta(
                hours=MAX_HOUR-thour,
                minutes=MAX_MIN-tmin,
                seconds=MAX_SEC-tsec,
                microseconds=MAX_MSEC-tmsec
            )
        )

        next_df = self.df.filter(pl.col("next_run_time").is_between(lower_date, upper_date))
        last_df = self.df.filter(pl.col("last_run_time").is_between(lower_date, upper_date))

        df = next_df.vstack(last_df)
        return TasksDataFrame(df)

class HistoryDataFrame(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def preprocess(self):
        """Preprocessing for the historical data frame."""
        df = (self.df
            .rename({
                "event_created_time":"Event Created",
                "event_level":"Event Level",
                "event_id":"Event ID",
                "task_name":"Task Name",
                "event_id_description":"Event ID Description",
                "event_log_description":"Event Log Description"
            }) 
            .with_columns(
                pl.col("Event Created").str.strptime(pl.Datetime,"%Y-%m-%d %H:%M:%S%.6f"),
                pl.col("Event Level").cast(pl.Int64),
                pl.col("Event ID").cast(pl.Int64)
            )
        )
        return HistoryDataFrame(df)

    def get_todays_history(self):
        """Filter the history data frame based on today's date."""
        df = self.df.filter(
            pl.col("Event Created").cast(pl.Date)==datetime.today().date()
        )
        return HistoryDataFrame(df)

    def __event_count_by_criteria(self, filter_col: str, filter_criteria: str) -> int:
        """Counts the number of events based on the filter column and criteria."""
        return self.df.filter(pl.col(filter_col)==filter_criteria).shape[0]

    def information_event_count(self) -> int:
        """Returns the count of information events."""
        return self.__event_count_by_criteria("Event Log Description","INFORMATION")

    def error_event_count(self) -> int:
        """Returns the count of error events."""
        return self.__event_count_by_criteria("Event Log Description","ERROR")

    def warning_event_count(self) -> int:
        """Returns the count of warning events."""
        return self.__event_count_by_criteria("Event Log Description","WARNING")
