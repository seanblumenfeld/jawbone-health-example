from fixerio import Fixerio

from app.main import db
from app.services.fixerio.models import RatesModel


class ApiAdapter:
    """
    This adapter to abstract our communication with the fixerio library.

    Although this adapter does not do much it allows us to fake out the api
    connection for tests and and internal logic our service might need that is
    not supported in the external library we are using.
    """

    def __init__(self, access_key, fake_fixerio=None):
        self.fixerio = fake_fixerio or Fixerio(access_key=access_key)

    def latest(self):
        return self.fixerio.latest()

    def historical_rates(self, date):
        return self.fixerio.historical_rates(date)


class DatabaseAdapter:
    """
    This adapter to abstract our communication with the database.
    """

    @staticmethod
    def store_rates(rates):
        row = RatesModel(rates=rates)
        db.session.add(row)
        db.session.commit()
        return row
