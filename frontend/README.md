# Task Manager Frontend

A modern React frontend for the Task Manager application.

## Features

- 🔐 User Authentication (Login/Signup)
- 📝 Create, Read, Update, Delete tasks
- 🏷️ Filter tasks by status and priority
- 📊 Pagination support
- 🎨 Beautiful, responsive UI
- ⚡ Built with React, Vite, and Axios

## Installation

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Build for Production

```bash
npm run build
```

## Environment Setup

Make sure your backend is running on `http://localhost:5000`

The API base URL is set to `http://localhost:5000/api` in `src/services/api.js`

## Project Structure

```
frontend/
├── src/
│   ├── components/         # Reusable components
│   │   ├── TaskCard.jsx
│   │   ├── TaskForm.jsx
│   │   └── TaskList.jsx
│   ├── pages/              # Page components
│   │   ├── Login.jsx
│   │   ├── Signup.jsx
│   │   └── Dashboard.jsx
│   ├── services/           # API services
│   │   └── api.js
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── index.html
├── vite.config.js
└── package.json
```

## Usage

### Authentication

- Sign up with your name, email, and password
- Login with your credentials
- JWT token is stored in localStorage

### Task Management

- Create new tasks with title, description, and priority
- Filter tasks by status and priority
- Edit tasks by clicking the edit button
- Mark tasks as complete
- Delete tasks
- Navigate through paginated results

## Technologies Used

- **React 18** - UI framework
- **Vite** - Build tool
- **Axios** - HTTP client
- **React Router** - Routing
- **React Icons** - Icon library

## Notes

- Ensure the backend is running before starting the frontend
- CORS should be enabled in your backend for frontend to communicate
- JTW tokens are used for authentication
