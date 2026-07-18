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
## License  Used
MIT License

Copyright (c) 2026 samsonmorara-maker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.