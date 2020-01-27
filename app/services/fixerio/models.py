from datetime import datetime

from sqlalchemy.dialects.postgresql import JSON

from app.main import db


class RatesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rates = db.Column(JSON, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    updated = db.Column(db.DateTime, default=datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'rates': self.rates,
            'created': self.created.isoformat(),
            'updated': self.updated.isoformat(),
        }
