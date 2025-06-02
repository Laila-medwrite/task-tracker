# Task Tracker

A simple Django REST API for managing tasks.

## Features

- Create, list, update, and delete tasks
- API endpoints for task management
- Uses Django REST Framework

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Laila-medwrite/task-tracker.git
   cd task-tracker
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/tasks/` — List all tasks
- `POST /api/tasks/` — Create a new task
- `GET /api/tasks/<id>/` — Retrieve a task by ID
- `PUT /api/tasks/<id>/` — Update a task
- `DELETE /api/tasks/<id>/` — Delete a task

## Running Tests

```sh
pytest
```


