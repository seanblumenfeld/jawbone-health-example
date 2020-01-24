import os
from pprint import pprint

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.api.converters import DateConverter

DB_CONN_STRING = 'postgresql://{username}:{password}@{host}:{port}/{db}'

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN_STRING.format(
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host='postgres',
    port='5432',
    db=os.getenv('POSTGRES_DB'),
)

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

api = Api()


def init_app():
    from app.api.routes import add_resources
    db.create_all(app=app)
    add_resources(api)
    api.init_app(app)


@app.cli.command('init_app')
def init_app_command():
    """Initializes the application."""
    init_app()


@app.cli.command('get_latest_rate')
def get_latest_rate_command():
    from app.services.fixerio import fixerio
    latest = fixerio.ApiAdapter(os.getenv('FIXERIO_API_KEY')).latest()
    pprint(latest)
