import os

from flask_restful import Resource

from app.services.fixerio import fixerio


class RatesApi(Resource):

    def __init__(self):
        super().__init__()
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = fixerio.ApiAdapter(
                access_key=os.getenv('FIXERIO_API_KEY')
            )
        return self._client

    def get(self, date):
        return self.client.historical_rates(date)

    def post(self, date):
        rates = self.client.historical_rates(date)
        row = fixerio.DatabaseAdapter.store_rates(rates)
        return row.to_dict(), 201
