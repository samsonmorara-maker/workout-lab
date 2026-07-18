# WORKOUT TRACKER
The Workout Tracker  is a Flask backend application that allows personal trainers to create workouts, manage reusable exercises, and associate exercises with workouts. Each exercise can be used in multiple workouts, while each workout can contain multiple exercises with workout-specific details such as sets, reps, and duration.
The application is built using Flask, SQLAlchemy, Marshmallow, and Flask-Migrate, with SQLite as the database.

## Features
- Create, view, and delete workouts
- Create, view, and delete exercises
- Add exercises to workouts
- Many-to-many relationship between workouts and exercises using a join table
- Model, schema, and database-level validations
- Database migrations using Flask-Migrate
- Seed file for generating sample data
 
 ## Tech Used
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Marshmallow
- SQLite
- Pipenv
## Installation
Clone the repository:
git clone git@github.com:samsonmorara-maker/workout-lab.git
cd workout lab
Install dependencies:
pipenv install
Activate the virtual environment:
pipenv shell
## Database Setup
Initialize the database (first time only):
flask db init
Create a migration:
flask db migrate -m "Initial migration"
Apply the migration:
flask db upgrade
Seed the database with sample data:
python seed.py
## Running the Application
Start the development server:
flask run
Then click the link
## Author
Developed by Samson Manoti Morara