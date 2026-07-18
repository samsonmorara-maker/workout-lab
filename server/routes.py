from flask import request, make_response
from marshmallow import ValidationError

from server.app import app
from server.models import db, Exercise
from server.schemas import (exercise_schema, exercises_schema)


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