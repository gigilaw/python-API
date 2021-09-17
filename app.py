from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    include_medicine = db.Column(db.Boolean, default=True, nullable=False)
    medicine_days = db.Column(db.Integer, nullable=True)
    hours = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, first_name, last_name, gender, price, include_medicine, medicine_days, hours):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.price = price
        self.include_medicine = include_medicine
        self.medicine_days = medicine_days
        self.hours = hours


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name):
        self.name = name


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name):
        self.name = name


class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, address, district_id, contact):
        self.name = name
        self.address = address
        self.district_id = district_id
        self.contact = contact


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name


@app.route('/', methods=['GET'])
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
