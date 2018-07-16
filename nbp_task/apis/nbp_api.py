import requests
from retrying import retry

class NbpAPI:
    def __init__(self):
        self.uri = 'http://api.nbp.pl/api/exchangerates/tables/a/?format=json'

    @retry(wait_fixed=500)
    def get_api_data(self):
        response = requests.get(self.uri).json()
        currency_rates = response[0].get('rates')
        return currency_rates
