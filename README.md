
# Student CRUD REST API

A RESTful API developed using FastAPI, Python, and SQLite to manage student records.

## Features
- Create student records
- Retrieve student details
- Update student information
- Delete student records
- Search student records
- Email validation
- Automated API testing

## Technologies
- Python
- FastAPI
- SQLite
- Pydantic
- Pytest
- GitHub Actions

## Installation

Clone the repository:

git clone https://github.com/mishraritu875-lgtm/Student-CRUD-API.git

cd Student-CRUD-API

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn main:app --reload

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Automated Testing

Run:

python -m pytest -v

The project includes automated API tests using Pytest.

## Continuous Integration

GitHub Actions automatically runs API tests when code is pushed to the repository.

## Database

SQLite is used for storing student records.

## Author

Ritu Mishra

GitHub: https://github.com/mishraritu875-lgtm
