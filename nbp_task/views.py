from pyramid.view import view_config, view_defaults
from nbp_task.apis.nbp_api import NbpAPI
from nbp_task.services.exchange_rate_service import ExchangeRateService


@view_defaults(renderer='templates/home.jinja2')
class Index:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'title': 'NBP Currencies'}


@view_defaults(renderer='templates/results.jinja2')
class Results:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='results')
    def results(self):
        nbp_api = NbpAPI()
        exchange_rate_service = ExchangeRateService(self.request.db)
        results = nbp_api.get_api_data()
        exchange_rate_service.save_exchange_rates_to_db(results)
        results = exchange_rate_service.get_all()

        return {'title': 'NBP Currencies',
                'results': results}
