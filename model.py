from app import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow())

    def __repr__(self):
        return "Database Created: {}".format(self.title)
