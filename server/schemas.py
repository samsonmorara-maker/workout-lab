from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate, auto_field

from server.models import Exercise, Workout, WorkoutExercise


class ExerciseSchema(SQLAlchemyAutoSchema):
    name = auto_field(validate=validate.Length(min=3))
    category = auto_field(validate=validate.Length(min=3))
    class Meta:
        model = Exercise
        include_relationships = True
        load_instance = True


class WorkoutSchema(SQLAlchemyAutoSchema):
    duration_minutes = auto_field(validate=validate.Range(min=1))
    class Meta:
        model = Workout
        include_relationships = True
        load_instance = True


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    sets = auto_field(validate=validate.Range(min=1))

    reps = auto_field(validate=validate.Range(min=0))
    duration_seconds = auto_field(validate=validate.Range(min=0))   
    class Meta:
        model = WorkoutExercise
        include_relationships = True
        load_instance = True

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)