from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate

from server.models import Exercise, Workout, WorkoutExercise


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        include_relationships = True
        load_instance = True


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        include_relationships = True
        load_instance = True


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        include_relationships = True
        load_instance = True

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_xercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)