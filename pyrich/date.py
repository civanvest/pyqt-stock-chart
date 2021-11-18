import pandas as pd


def to_timestamp(datetime: str) -> pd.Timestamp:
    if datetime is None:
        datetime = pd.Timestamp.now()
    timestamp = pd.to_datetime(datetime)

    return timestamp