from typing import Literal
from tasklit.constants import TASK_STATES, TASK_RESULTS
import polars as pl


class TaskData(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def total_task_count(self) -> int:
        """Total task count."""
        return self.df.shape[0]

    def total_missed_runs(self) -> int:
        """Total missed runs"""
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
        df = (self.df
            .with_columns(
                pl.col("state").replace(TASK_STATES).alias("state_description").str.to_titlecase())
            .group_by("state_description","state")
            .agg(pl.col("state").count().alias("count"))
            .rename(
                {   
                    "state_description":"State Description",
                    "state":"State Code",
                    "count":"Number of Tasks"
                }
            )
        )
        return df
    
    def task_results(self):
        df = (self.df
            .with_columns(
                pl.col("last_task_result").replace(TASK_RESULTS).alias("result_description").str.to_titlecase())
            .group_by("result_description","last_task_result")
            .agg(pl.col("last_task_result").count().alias("count"))
            .rename(
                {   
                    "result_description":"Result Description",
                    "last_task_result":"Result Code",
                    "count":"Number of Tasks"
                }
            )
        )
        return df
    
    def task_by_author(self):
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
