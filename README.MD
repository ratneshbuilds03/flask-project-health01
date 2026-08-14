# Task Manager API

A production-ready RESTful API for task management, built with Flask, MySQL, and JWT authentication. Features user-specific task isolation, filtering, pagination, and full CI/CD pipeline with Docker.

## Live Demo

🔗 [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features

- User authentication (signup/login) with JWT tokens
- Password hashing using bcrypt
- CRUD operations for tasks (Create, Read, Update, Delete)
- User-specific task isolation (users only see their own tasks)
- Filtering by status and priority
- Pagination support
- Global error handling
- Automated testing with pytest
- Dockerized with docker-compose (multi-container setup)
- CI/CD pipeline with GitHub Actions

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (SQLAlchemy ORM)
- **Authentication:** JWT (Flask-JWT-Extended), bcrypt
- **Testing:** pytest
- **DevOps:** Docker, docker-compose, GitHub Actions
- **Deployment:** Render

## Architecture

Client → Flask API (Routes) → Services (Business Logic) → Models (SQLAlchemy) → MySQL Database → JWT Middleware (Authentication)

## Project Structuretask-manager/

├── app/
│ ├── models/ # Database models
│ ├── routes/ # API endpoints
│ ├── services/ # Business logic
│ ├── utils/ # Helper functions & error handlers
│ └── config.py # Configuration
├── tests/ # Pytest test cases
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/ # CI/CD pipeline

## API Endpoints

| Method | Endpoint      | Description                                    | Auth Required |
| ------ | ------------- | ---------------------------------------------- | ------------- |
| POST   | `/signup`     | Register new user                              | No            |
| POST   | `/login`      | Login, get JWT token                           | No            |
| GET    | `/tasks`      | List all tasks (supports filters & pagination) | Yes           |
| POST   | `/tasks`      | Create new task                                | Yes           |
| GET    | `/tasks/<id>` | Get single task                                | No            |
| PUT    | `/tasks/<id>` | Update task                                    | No            |
| DELETE | `/tasks/<id>` | Delete task                                    | No            |

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com", "password": "secret123"}'
```

## Setup Instructions

### Local Setup

1. Clone the repo

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up `.env` file (see `.env.example`)

5. Run the app

```bash
python run.py
```

### Docker Setup

```bash
docker-compose up --build
```

### Running Tests

```bash
pytest tests/ -v
```

## What I Learned

- Designing RESTful APIs following industry conventions (proper HTTP methods, status codes)
- Implementing secure authentication with JWT and password hashing
- Structuring Flask applications using the App Factory pattern and Blueprints
- Containerizing multi-service applications with Docker Compose
- Setting up CI/CD pipelines for automated testing and deployment
- Writing unit tests with pytest using isolated test databases

## Future Improvements

- Add refresh tokens for better session management
- Implement rate limiting
- Add email verification on signup
- Redis caching for frequently accessed data
