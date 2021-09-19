from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker
from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
fake = Faker()
ma = Marshmallow(app)


doctor_language = db.Table('doctor_language',
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
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinic.id'),
                          nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    languages = db.relationship(
        'Language', secondary=doctor_language, lazy="joined")
    clinic = db.relationship('Clinic', backref='doctor')

    def __init__(self, first_name, last_name, gender, category_id, clinic_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.category_id = category_id
        self.clinic_id = clinic_id

    @classmethod
    def seed(cls, fake):
        doctor = Doctor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=fake.random_element(elements=("F", "M")),
            category_id=fake.random_int(1, 3),
            clinic_id=fake.random_int(1, 5)
        )
        save(doctor)
        doctor.add_mock_relationship()

    def add_mock_relationship(self):
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
    district_id = db.Column(db.Integer, db.ForeignKey(
        'district.id'), nullable=False)
    contact = db.Column(db.String, nullable=False)
    hours = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    include_medications = db.Column(db.Boolean, nullable=False)
    medication_days = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, address, district_id, contact, hours, price, include_medications, medication_days):
        self.name = name
        self.address = address
        self.district_id = district_id
        self.contact = contact
        self.hours = hours
        self.price = price
        self.include_medications = include_medications
        self.medication_days = medication_days

    @classmethod
    def seed(cls, fake):
        mock_hours = [
            "Monday: 9am-3pm, Tuesday: 9am-3pm, Wednesday: 9am-3pm, Thursday: 9am-3pm",
            "Monday: 9am-8pm, Friday: 9am-8pm, Saturday: closed, Sunday: closed, Public Holiday: closed"
        ]

        clinic = Clinic(
            name=fake.company() + " Clinic",
            address=fake.address(),
            district_id=fake.random_int(1, 2),
            contact=fake.phone_number(),
            hours=fake.random_element(elements=mock_hours),
            price=fake.random_int(100, 1000, 10),
            include_medications=fake.boolean(),
            medication_days=None
        )

        if clinic.include_medications:
            clinic.medication_days = fake.random_int(1, 7)
        save(clinic)


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name):
        self.name = name


class DistrictSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class ClinicSchema(SQLAlchemyAutoSchema):
    district = ma.Nested(DistrictSchema)

    class Meta:
        model = Clinic
        exclude = ('created_at', 'id')


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ('id', 'name')


class DoctorSchema(ma.Schema):
    clinic = ma.Nested(ClinicSchema)
    category = ma.Nested(CategorySchema)

    class Meta:
        fields = ('category', 'clinic', 'first_name', 'last_name')


doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "working"})


@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if(request.method == 'GET'):
        if not request.query_string:
            all_doctors = Doctor.query.all()
        else:
            query = doctor_query_builder()
            all_doctors = query.all()

        result = doctors_schema.dump(all_doctors)
        return jsonify(result)

    new_doctor = add_doctor()
    return doctor_schema.jsonify(new_doctor)


@app.route('/doctor/<id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    return doctor_schema.jsonify(doctor)


def doctor_query_builder():
    district_id = request.args.get('districtId')
    category_id = request.args.get('categoryId')
    language_id = request.args.get('languageId')
    greater_than = request.args.get('gt')
    less_than = request.args.get('lt')

    query = Doctor.query.join(Clinic)
    if category_id:
        query = query.filter(Doctor.category_id == category_id)

    if language_id:
        query = query.filter(Doctor.languages.any(id=language_id))

    if district_id:
        query = query.filter(
            Clinic.district_id == district_id)

    if less_than and greater_than:
        query = query.filter(
            Clinic.price >= greater_than, Clinic.price <= less_than)

    return query


def add_doctor():
    first_name = request.json['firstName']
    last_name = request.json['lastName']
    gender = request.json['gender']
    category_id = request.json['categoryId']
    clinic_id = request.json['clinicId']
    languages = request.json['languages']

    doctor = Doctor(first_name, last_name, gender, category_id, clinic_id)

    save(doctor)

    for languageId in languages:
        language = Language.query.get(languageId)
        doctor.languages.append(language)
        db.session.commit()

    return doctor


def save(self):
    db.session.add(self)
    db.session.commit()


if __name__ == '__main__':
    app.run()
