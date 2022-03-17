from abc import ABC, abstractmethod
import finnhub
import pandas as pd
import pyqtgraph as pg
import yaml
from pyqt.date import get_timestamp
from pyqt.date import get_n_days_ago
from pyqt.util import resource_path


class Stock(ABC):

    def __init__(self, symbol):
        self.symbol = symbol
        self.finnhub_client = finnhub.Client(api_key=self.get_api_key())
        self.daily = 'D'
        one_year_ago = get_n_days_ago(365)
        today = pd.Timestamp.today().normalize()
        self.start = get_timestamp(one_year_ago)
        self.end = get_timestamp(today)

    def get_api_key(self):
        path = resource_path('api.yaml')
        with open(path) as f:
            yml = yaml.load(f, Loader=yaml.FullLoader)
            api_key = yml['FINNHUB_APIKEY']
        return api_key

    @abstractmethod
    def get_price(self):
        pass

    def get_price_now(self):
        return self.finnhub_client.quote(self.symbol)

    def draw_chart(self):
        pg.setConfigOption('background', 'w')
        price = self.get_price()
        close = price['c']
        date = price['t']
        plt = pg.PlotWidget()
        plt.resize(500, 300)
        plt.plot(date, close, pen=pg.mkPen('b', width=5))
        plt.setAxisItems({'bottom': pg.DateAxisItem()})
        plt.showGrid(x=True, y=True)
        plt.setMouseEnabled(x=False, y=False)

        return plt


class UsStock(Stock):

    def __init__(self, symbol):
        super().__init__(symbol)

    def get_price(self):
        res = self.finnhub_client.stock_candles(
                self.symbol,
                self.daily,
                self.start,
                self.end
            )
        return res


class Crypto(Stock):

    def __init__(self, symbol):
        super().__init__(symbol)

    def get_price(self):
        res = self.finnhub_client.crypto_candles(
                self.symbol,
                self.daily,
                self.start,
                self.end
            )
        return res


