from datetime import datetime, date, time, timedelta
from sqlalchemy import Date, DateTime, Time, cast, and_
from sqlalchemy import func
from app.db import db


class Vehicle(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer, nullable=False, unique=False)
    motor_1 = db.Column(db.Integer, nullable=False, unique=False)
    motor_2 = db.Column(db.Integer, nullable=False, unique=False)
    speed = db.Column(db.Float, nullable=True, unique=False)
    bumper_status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, unique=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()
    
    @staticmethod
    def max_version():
        return db.session.query(func.max(Vehicle.version)).scalar()

    @staticmethod
    def last(quantity):
        query = Vehicle.query
        query = query.order_by(
            cast(Vehicle.created_at, DateTime).desc(), cast(Vehicle.created_at, DateTime).asc())
        return query.limit(quantity).all()
