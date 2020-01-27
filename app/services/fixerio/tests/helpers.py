from unittest.mock import create_autospec

import fixerio

from app.services.fixerio.fixerio import ApiAdapter

FakeFixerio = create_autospec(fixerio.Fixerio)
FakeApiAdapter = create_autospec(ApiAdapter)
