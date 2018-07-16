from ..models.exchange_rate import ExchangeRate


class ExchangeRateService:
    def __init__(self, db_session):
        self.db_session = db_session

    def save_exchange_rates_to_db(self, currency_rates):
        self.db_session.query(ExchangeRate).delete()

        for currency_rate in currency_rates:
            self.save_exchange_rate_to_db(currency_rate)
        self.db_session.commit()

    def save_exchange_rate_to_db(self, currency_rate):
        exchange_rate = ExchangeRate(currency_rate['currency'],
                                           currency_rate['code'],
                                           currency_rate['mid'])
        self.db_session.add(exchange_rate)

    def get_all(self):
        query = self.db_session.query(ExchangeRate).all()
        results = [{'currency': result.currency,
                    'currency_code': result.currency_code,
                    'exchange_rate': result.exchange_rate} for result in query]
        return results
