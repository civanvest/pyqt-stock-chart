from datetime import datetime
import pandas as pd


def subtract_days(date, days):
    n_days = pd.Timedelta(days=days)
    date = date - n_days
    return date
