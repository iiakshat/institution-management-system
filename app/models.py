from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrollment_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_primary = db.Column(db.String(20))
    phone_secondary = db.Column(db.String(20))
    course = db.Column(db.String(100))
    year = db.Column(db.String(10))
    roll_number = db.Column(db.String(20))
    cgpa = db.Column(db.Float)
    attendance_percentage = db.Column(db.Float)
    address = db.Column(db.String(200))
    linkedin_url = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    profile_picture = db.Column(db.String(200))
    password = db.Column(db.String(200), nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    result_date = db.Column(db.Date, default=datetime.utcnow)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    notes_url = db.Column(db.String(200))
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    profile_picture = db.Column(db.String(200))

class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fee_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, default=datetime.utcnow)

# Optional: Flask-Login user loader
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
