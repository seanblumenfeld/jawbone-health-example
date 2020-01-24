from app.services.fixerio import fixerio
from app.services.fixerio.models import RatesModel
from app.services.fixerio.tests.helpers import FakeFixerio
from app.test_base import TestCaseBase


class FixerioTests(TestCaseBase):
    fake_response = {
        'success': True,
        'timestamp': 1579854366,
        'base': 'EUR',
        'date': '2020-01-24',
        'rates': {'GBP': 0.84212, 'GEL': 3.182798},
    }

    def setUp(self):
        super().setUp()
        self.fake_fixerio = FakeFixerio(access_key='fake-key')
        self.client = fixerio.ApiAdapter(
            access_key='fake-api-key',
            fake_fixerio=self.fake_fixerio
        )

    def test_fixerio_latest(self):
        self.fake_fixerio.latest.return_value = self.fake_response
        self.assertEqual(
            self.client.latest(),
            self.fake_fixerio.latest()
        )

    def test_fixerio_historic_rates(self):
        self.fake_fixerio.historical_rates.return_value = self.fake_response
        self.assertEqual(
            self.client.historical_rates('2020-01-24'),
            self.fake_fixerio.historical_rates('2020-01-24')
        )

    def test_store_rates(self):
        dao = fixerio.DatabaseAdapter()
        dao.store_rates(self.fake_response)
        self.assertEqual(RatesModel.query.count(), 1)
        self.assertEqual(RatesModel.query.first().rates, self.fake_response)
