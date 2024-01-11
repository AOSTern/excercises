# %%
from datetime import datetime
from datetime import timedelta


def add(moment: datetime) -> datetime:
    future_time = moment + timedelta(seconds=10e8)
    return future_time


# %%
