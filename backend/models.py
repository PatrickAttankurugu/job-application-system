from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    location = db.Column(db.String(100))
    status = db.Column(db.String(50), default='Applied')
    interview_date = db.Column(db.DateTime, nullable=True)
    offer_details = db.Column(db.String(200), nullable=True)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
