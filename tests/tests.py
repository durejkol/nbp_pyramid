import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from nbp_task.views import Index
        request = testing.DummyRequest()
        info = Index.home(request)
        self.assertEqual(info['title'], 'NBP Currencies')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from nbp_task import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'POBIERZ WALUTY' in res.body)

    def test_results(self):
        res = self.testapp.get('/results', status=200)
        self.assertTrue(b'Currency' in res.body)
        self.assertTrue(b'Code' in res.body)
        self.assertTrue(b'Exchange rate' in res.body)
        self.assertTrue(str(res.body).count('PLN'), 10)


class ApiTests(unittest.TestCase):
    def setUp(self):
        from nbp_task.apis import nbp_api
        self.nbp_api = nbp_api.NbpAPI()

    def test_get_data(self):
        results = self.nbp_api.get_api_data()
        self.assertTrue(len(results), 35)
        self.assertTrue(type(results) == list)
