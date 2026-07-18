from flask import request, make_response
from marshmallow import ValidationError
from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise
from server.schemas import (
    exercise_schema, 
    exercises_schema, 
    workout_schema, 
    workouts_schema, 
    workout_exercise_schema, 
    workout_exercises_schema
    )


@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(
        exercises_schema.dump(exercises),
        200
    )

@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()

    if not exercise:
        return make_response(
            {"error": "Exercise not found"},
            404
        )
    return make_response(
        exercise_schema.dump(exercise),
        200
    )

@app.route("/exercises", methods=["POST"])
def create_exercise():
    try:
        exercise = exercise_schema.load(request.json)
        db.session.add(exercise)
        db.session.commit()
        return make_response(
            exercise_schema.dump(exercise),
            201
        )
    except ValidationError as error:
        return make_response(
            {"errors": error.messages},
            400
        )

@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response(
            {"error": "Exercise not found"},
            404
        )
    db.session.delete(exercise)
    db.session.commit()
    return make_response({}, 204)


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return make_response(
            {"error": "Workout not found"},
            404
        )

    return make_response(
        workout_schema.dump(workout),
        200
    )

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return make_response(
        workouts_schema.dump(workouts),
        200
    )
@app.route("/workouts", methods=["POST"])
def create_workout():
    try:
        workout = workout_schema.load(request.json)

        db.session.add(workout)
        db.session.commit()
        return make_response(
            workout_schema.dump(workout),
            201
        )
    except ValidationError as err:
        return make_response(
            {"errors": err.messages},
            400
        )
    
@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return make_response(
            {"error": "Workout not found"},
            404
        )
    db.session.delete(workout)
    db.session.commit()

    return make_response({}, 204)


@app.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"]
)
def add_exercise_to_workout(workout_id, exercise_id):

    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if workout is None:
        return make_response({"error": "Workout not found"}, 404)

    if exercise is None:
        return make_response({"error": "Exercise not found"}, 404)

    data = request.get_json()
    workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        sets=data["sets"],
        reps=data["reps"],
        duration_seconds=data["duration_seconds"]
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return make_response(
        workout_exercise_schema.dump(workout_exercise),
        201
    )