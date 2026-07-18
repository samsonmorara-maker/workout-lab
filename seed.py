from datetime import date
from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise


with app.app_context():
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()


    exercises = [
        Exercise(
            name="Bench Press",
            category="Strength",
            equipment_needed=True
        ),
        Exercise(
            name="Push Up",
            category="Strength",
            equipment_needed=False
        ),
        Exercise(
            name="Running",
            category="Cardio",
            equipment_needed=False
        ),
        Exercise(
            name="Plank",
            category="Core",
            equipment_needed=False
        )
    ]
    db.session.add_all(exercises)
    db.session.commit()


    workouts = [
        Workout(
            date=date(2024, 6, 18),
            duration_minutes=60,
            notes="Upper body workout"
        ),
        Workout(
            date=date(2026, 7, 19),
            duration_minutes=45,
            notes="Cardio and core workout"
        )
    ]
    db.session.add_all(workouts)
    db.session.commit()


    workout_exercises = [
        WorkoutExercise(
            workout_id=workouts[0].id,
            exercise_id=exercises[0].id,
            sets=4,
            reps=10,
            duration_seconds=0
        ),
        WorkoutExercise(
            workout_id=workouts[0].id,
            exercise_id=exercises[1].id,
            sets=3,
            reps=15,
            duration_seconds=0
        ),
        WorkoutExercise(
            workout_id=workouts[1].id,
            exercise_id=exercises[2].id,
            sets=1,
            reps=0,
            duration_seconds=1800
        ),
        WorkoutExercise(
            workout_id=workouts[1].id,
            exercise_id=exercises[3].id,
            sets=3,
            reps=1,
            duration_seconds=60
        )
    ]

    db.session.add_all(workout_exercises)
    db.session.commit()

    