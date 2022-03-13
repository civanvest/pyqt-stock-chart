from typing import Optional
from pyrich.date import to_timestamp


class Transaction:

    def __init__(self, action: str, symbol: str, shares: int, price: float,
                 currency: str = 'USD', datetime: Optional[str] = None) -> None:
        self.action = action
        self.symbol = symbol.upper()
        self.shares = shares
        self.price = price
        self.datetime = datetime
        self.currency = currency

    def _total_transaction_price(self) -> float:
        total_price = self.price * self.shares
        
        return total_price

    def transaction_record(self) -> dict:
        total_price = self._total_transaction_price()
        timestamp = to_timestamp(self.datetime)

        record = {
            'action': self.action,
            'date': timestamp,
            'symbol': self.symbol,
            'price': self.price,
            'shares': self.shares,
            'total_price': total_price,
            'currency': self.currency,
        }

        return record


class Buy(Transaction):
    action = 'buy'

    def __init__(self, **kargs) -> None:
        super().__init__(self.action, **kargs)

    # connect to a databse system to add stock to the portfolio


class Sell(Transaction):
    action = 'sell'

    def __init__(self, **kargs) -> None:
        super().__init__(self.action, **kargs)

    # connect to a databse system to remove the stock from the portfolio

