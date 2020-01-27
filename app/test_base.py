import unittest

from app.api.routes import add_resources
from app.main import api, app, db


class TestCaseBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.sqlite3'

        if not api.resources:
            add_resources(api)
            api.init_app(app)

        cls.test_client = app.test_client()

    def setUp(self):
        db.create_all(app=app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=app)
