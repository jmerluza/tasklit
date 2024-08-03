from typing import Literal
import polars as pl


class TaskData(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def filter_tasks_by_state(self, state_code: Literal[0, 1, 2, 3, 4]):
        """
        Filter the tasks data by state code.

        Parameters:
            state_code (`int`): State Code.
                0: Unknown,
                1: Disabled,
                2: Queued,
                3: Ready,
                4: Running
        """
        df = self.df.filter(pl.col("state") == state_code)
        return TaskData(df)

    def filter_tasks_by_last_result(
        self,
        result_code: Literal[0, 1, 2, 10, 267011, 2147750687, 2147943645, 2147942402],
    ):
        """
        Filter the tasks data by last result code.

        Parameters:
            result_code (`int`): Last Result Code.
            0: The operation completed successfully (often means the task ran without errors).
            1: Incorrect function (general failure, often indicating some error but not very specific).
            2: The system cannot find the file specified (often means the script or executable could not be found).
            10: The environment is incorrect (often means there was an issue with the system environment).
            267011: (0x00041303) The task has not yet run.
            2147750687: (0x8004131F) The task scheduler service is not available.
            2147943645: (0x80070015) The device is not ready.
            2147942402: (0x80070002) The system cannot find the file specified.
        """
        df = self.df.filter(pl.col("last_task_result") == result_code)
        return TaskData(df)
