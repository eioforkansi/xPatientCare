from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import random

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=lambda:random.randint(100000, 999999))
    password = db.Column(db.String(1000))
    title = db.Column(db.String(80), default="")
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50) , default="")
    last_name = db.Column(db.String(50), default="")
    user_role = db.Column(db.String(50), default="Patient")
    date_of_birth = db.Column(db.String(10), default="")
    gender = db.Column(db.String(10), default="")
    contact_number = db.Column(db.String(15), default="")
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(255), default="")
    emergency_contact_name = db.Column(db.String(100), default="")
    emergency_contact_number = db.Column(db.String(15), default="")
    medical_history = db.Column(db.Text, default="")  # Stores a summary of past medical history
    allergies = db.Column(db.Text, default="")  # Stores allergy information
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  
    

class Bookings(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    hospital = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    reason = db.Column(db.String(1000), nullable=False)
    booking_status = db.Column(db.String(1000), nullable=False, default="Pending")


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=lambda:random.randint(100000, 999999))
    user_id = db.Column(db.Integer)
    date_of_visit = db.Column(db.String(100))
    review = db.Column(db.Text)
    physician_name = db.Column(db.String(100))
    diagnosis = db.Column(db.String(255))
    plan = db.Column(db.Text)
    follow_up_date = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Medications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer)
    dosage_form = db.Column(db.String(50))
    medication_name = db.Column(db.String(100))
    frequency = db.Column(db.String(50)) 
    duration = db.Column(db.String(100))
    prescribed_by = db.Column(db.String(100))
    dispensed_by = db.Column(db.String(100), default="Pending")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Documentations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer)
    documentation = db.Column(db.Text)
    documentation_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    