# phase-4-week-1-code-
# Phase 4 Week 1 Code Challenge: Superheroes API
## Overview

This is a Flask API for managing superheroes and their superpowers.
It allows you to:

View all heroes and their powers

View all powers

Add new hero powers

Update existing powers

This project uses SQLite as the database and Flask-Migrate for database migrations.

## Features

Heroes have multiple powers through HeroPower

Powers can belong to multiple heroes

HeroPower tracks the strength of a hero’s power (Strong, Average, Weak)

Validations ensure data integrity:

Power descriptions must be at least 20 characters

HeroPower strength must be Strong, Average, or Weak


## Setup Instructions

Clone the repository:

git clone <your-repo-url>
cd phase4-superheroes


Create a virtual environment:

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt


Make sure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed.

# Set Flask environment variables:

export FLASK_APP=app.py
export FLASK_ENV=development


# On Windows PowerShell:

set FLASK_APP=app.py
set FLASK_ENV=development


# Run database migrations:

flask db init        # only the first time
flask db migrate -m "Initial migration"
flask db upgrade


# Seed the database:

python seed.py


# Start the Flask server:

python app.py


By default, the server runs at http://127.0.0.1:5000 (or port 5555 if specified).

# API Endpoints
Route	Method	Description
/heroes	GET	List all heroes
/heroes/<id>	GET	Get hero by ID with hero powers
/powers	GET	List all powers
/powers/<id>	GET	Get power by ID
/powers/<id>	PATCH	Update a power description
/hero_powers	POST	Create a new hero power
Example JSON

GET /heroes

[
  {"id":1,"name":"Kamala Khan","super_name":"Ms. Marvel"},
  {"id":2,"name":"Doreen Green","super_name":"Squirrel Girl"},
  {"id":3,"name":"Gwen Stacy","super_name":"Spider-Gwen"}
]


POST /hero_powers

{
  "strength": "Average",
  "hero_id": 2,
  "power_id": 1
}


Response:

{
  "id": 3,
  "hero_id": 2,
  "power_id": 1,
  "strength": "Average",
  "hero": {"id":2,"name":"Doreen Green","super_name":"Squirrel Girl"},
  "power": {"id":1,"name":"Super Strength","description":"Gives the wielder super-human strength"}
}

## Author

Abdirahman Sheikh
