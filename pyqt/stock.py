from abc import ABC, abstractmethod
from dotenv import load_dotenv
import finnhub
import os
import pandas as pd
import pyqtgraph as pg


class Stock(ABC):

    def __init__(self, symbol):
        self.symbol = symbol
        self.finnhub_client = finnhub.Client(api_key=self.get_api_key())

    def get_api_key(self):
        load_dotenv()
        api_key = os.environ.get('FINNHUB_APIKEY')
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

