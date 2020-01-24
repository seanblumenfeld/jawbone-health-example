from dateutil.parser import parse
from werkzeug.routing import BaseConverter


class DateConverter(BaseConverter):
    """Converts a date in a url path to a python object and vice versa."""

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return parse(value)

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')
