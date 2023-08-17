from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    gender = db.Column(db.String())
    hobbies = db.Column(db.String())
    country = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"
    