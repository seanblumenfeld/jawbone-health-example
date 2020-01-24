from unittest.mock import patch

from app.test_base import TestCaseBase


class RatesApiTests(TestCaseBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fake_data = {
            'success': True,
            'timestamp': 1579854366,
            'base': 'EUR',
            'date': '2020-01-24',
            'rates': {'GBP': 0.84212, 'GEL': 3.182798},
        }

    @patch('app.services.fixerio.fixerio.ApiAdapter.historical_rates')
    def test_get_rates_for_given_date(self, fake_historical_rates):
        fake_historical_rates.return_value = self.fake_data

        response = self.test_client.get('/rates/2020-01-24')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.fake_data)

    @patch('app.services.fixerio.fixerio.ApiAdapter.historical_rates')
    def test_get_returns_404_if_bad_date_format(self, fake_historical_rates):
        response = self.test_client.get('/rates/bad-date')
        # Ideally we would return a 400 here with a message about the bad
        # date format. Given more we could make the app us the custom
        # converter to return correct http responses
        self.assertEqual(response.status_code, 404)

    @patch('app.services.fixerio.fixerio.ApiAdapter.historical_rates')
    def test_store_rates_for_given_date(self, fake_historical_rates):
        fake_historical_rates.return_value = self.fake_data
        response = self.test_client.post('/rates/2020-01-24')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['rates'], self.fake_data)

    @patch('app.services.fixerio.fixerio.ApiAdapter.historical_rates')
    def test_post_returns_404_if_bad_date_format(self, fake_historical_rates):
        response = self.test_client.post('/rates/bad-date')
        self.assertEqual(response.status_code, 404)
