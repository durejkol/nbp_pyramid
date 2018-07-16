from nbp_task.models import Base
from sqlalchemy import Column, Float, Integer, String


class ExchangeRate(Base):
    __tablename__ = 'currencies'

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    currency_code = Column(String)
    exchange_rate = Column(Float)

    def __init__(self, currency, currency_code, exchange_rate):
        self.currency = currency
        self.currency_code = currency_code
        self.exchange_rate = exchange_rate

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.currency,
                                      self.currency_code,
                                      self.exchange_rate)
