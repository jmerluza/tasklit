from typing import Literal
from tasklit.constants import TASK_STATES, TASK_RESULTS
import polars as pl


class TaskData(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data
        self.empty = self.df.is_empty()

    def total_task_count(self) -> int:
        """Total task count."""
        if self.empty:
            return 0
        else:
            return self.df.shape[0]

    def total_missed_runs(self) -> int:
        """Total missed runs"""
        if self.empty:
            return 0
        else:
            return self.df["missed_runs"].sum()
    
    def task_states(self):
        """Get the total number of tasks by task state.
        
        >>> shape: (2, 3)
            ┌───────────────────┬────────────┬─────────────────┐
            │ State Description ┆ State Code ┆ Number of Tasks │
            │ ---               ┆ ---        ┆ ---             │
            │ str               ┆ i64        ┆ u32             │
            ╞═══════════════════╪════════════╪═════════════════╡
            │ Running           ┆ 4          ┆ 3               │
            │ Ready             ┆ 3          ┆ 19              │
            └───────────────────┴────────────┴─────────────────┘
        """
        if self.empty:
            return pl.DataFrame()
        else:
            df = (self.df
                .group_by("state")
                .agg(pl.col("state").count().alias("count"))
                .rename(
                    {   
                        "state":"States",
                        "count":"Number of Tasks"
                    }
                )
            )
            return df
    
    def task_results(self):
        if self.empty:
            return pl.DataFrame()
        else:
            df = (self.df
                .group_by("last_task_result")
                .agg(pl.col("last_task_result").count().alias("count"))
                .rename(
                    {   
                        "last_task_result":"Results",
                        "count":"Number of Tasks"
                    }
                )
            )
            return df
    
    def task_by_author(self):
        if self.empty:
            return pl.DataFrame()
        else:
            df = (self.df
                .group_by("author")
                .agg([pl.count("name"), pl.sum("missed_runs")])
                .sort("author")
                .rename(
                    {
                        "author":"Author",
                        "name":"Number of Tasks",
                        "missed_runs":"Number of Missed Runs"
                    }
                )
            )
            return df
