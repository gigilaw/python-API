from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from app import app, District, Category, Clinic, Doctor, Language

fake = Faker()
db = SQLAlchemy(app)

# Seed Category Table
db.session.add(Category("General Practitioner"))
db.session.add(Category("Pediatrician"))
db.session.add(Category("Cardiologist"))

# Seed District Table
db.session.add(District("Wan Chai"))
db.session.add(District("Price Edward"))

# Seed Language Table
db.session.add(Language("English"))
db.session.add(Language("Cantonese"))
db.session.add(Language("Mandarin"))

db.session.commit()

# Seed Clinic Table
for _ in range(5):
    Clinic.seed(fake)

# Seed Doctor Table
for _ in range(5):
    Doctor.seed(fake)
