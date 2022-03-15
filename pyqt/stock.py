from abc import ABC, abstractmethod
from dotenv import load_dotenv
import finnhub
import os
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

