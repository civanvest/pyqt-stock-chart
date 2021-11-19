import pytest
import pandas as pd
from pyrich.date import to_timestamp


class TestDate:

    @pytest.mark.parametrize(
        'datetime',
        [
            ('2021-11-18 10:58'),
            (None),
        ]
    )
    def test_datetime_input(self, datetime):
        timestamp = to_timestamp(datetime)
        assert isinstance(timestamp, pd.Timestamp)
