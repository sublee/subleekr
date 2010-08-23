import datetime
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.sql import functions as func
from subleekr.ubiq import app


db = app.super_app.db


class Status(db.Model):

    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    brightness = Column(Integer)
    temperature = Column(Integer)
    logged_at = Column(DateTime(timezone=True), nullable=False,
                                                default=func.now(),
                                                server_default=func.now())

    def __init__(self, brightness, temperature):
        self.brightness, self.temperature = brightness, temperature
        self.logged_at = datetime.datetime.now()

    def __repr__(self):
        return "<Status {0}>".format((self.brightness, self.temperature))

