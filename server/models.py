from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    
    
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Exercise name is required")

        if len(name) < 3:
            raise ValueError(
                "Exercise name must be at least 3 characters"
            )

        return name
    
    def __repr__(self):
        return f"<Exercise {self.name}>"