from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
fake = Faker()

doctors_clinics = db.Table('doctors_clinics',
                           db.Column('doctor_id', db.Integer, db.ForeignKey(
                               'doctor.id'), primary_key=True),
                           db.Column('clinic_id', db.Integer, db.ForeignKey(
                               'clinic.id'), primary_key=True),
                           db.Column('created_at', db.DateTime,
                                     default=datetime.now())
                           )

doctors_languages = db.Table('doctors_languages',
                             db.Column('doctor_id', db.Integer, db.ForeignKey(
                                 'doctor.id'), primary_key=True),
                             db.Column('language_id', db.Integer, db.ForeignKey(
                                 'language.id'), primary_key=True),
                             db.Column('created_at', db.DateTime,
                                       default=datetime.now())
                             )


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    include_medicine = db.Column(db.Boolean, default=True, nullable=False)
    medicine_days = db.Column(db.Integer, nullable=True)
    hours = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    clinics = db.relationship('Clinic', secondary=doctors_clinics)
    languages = db.relationship('Language', secondary=doctors_languages)

    def __init__(self, first_name, last_name, gender, price, include_medicine, medicine_days, hours, category_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.price = price
        self.include_medicine = include_medicine
        self.medicine_days = medicine_days
        self.hours = hours
        self.category_id = category_id

    @classmethod
    def seed(cls, fake):
        mock_hours = [
            "Monday: 9am-3pm, Tuesday: 9am-3pm, Wednesday: 9am-3pm, Thursday: 9am-3pm",
            "Monday: 9am-8pm, Friday: 9am-8pm, Saturday: closed, Sunday: closed, Public Holiday: closed"
        ]
        doctor = Doctor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=fake.random_element(elements=("F", "M")),
            price=fake.random_int(300, 1000, 10),
            include_medicine=fake.boolean(),
            medicine_days=None,
            hours=fake.random_element(elements=mock_hours),
            category_id=fake.random_int(1, 3)
        )
        if doctor.include_medicine:
            doctor.medicine_days = fake.random_int(1, 7)

        save(doctor)
        doctor.add_relationship()

    def add_relationship(self):
        clinic = Clinic.query.get(fake.random_int(1, 5))
        self.clinics.append(clinic)

        language = Language.query.get(fake.random_int(1, 3))
        self.languages.append(language)

        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    doctors = db.relationship('Doctor', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    clinics = db.relationship('Clinic', backref='district', lazy=True)

    def __init__(self, name):
        self.name = name


class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'),
                            nullable=False)
    contact = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, address, district_id, contact):
        self.name = name
        self.address = address
        self.district_id = district_id
        self.contact = contact

    @classmethod
    def seed(cls, fake):
        clinic = Clinic(
            name=fake.company() + " Clinic",
            address=fake.address(),
            district_id=fake.random_int(1, 2),
            contact=fake.phone_number(),
        )

        save(clinic)


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name):
        self.name = name


def save(self):
    db.session.add(self)
    db.session.commit()


@app.route('/', methods=['GET'])
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
