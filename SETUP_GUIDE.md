# Task Manager - Setup & Running Guide

## Prerequisites

- Node.js (v16+) and npm
- Python 3.8+
- MySQL (already running)

## Backend Setup

### 1. Install Backend Dependencies

```bash
cd d:\vscodefiles\task-manager
pip install -r requirements.txt
```

### 2. Run the Backend

```bash
cd d:\vscodefiles\task-manager
python run.py
```

The backend will start on `http://localhost:5000`

## Frontend Setup

### 1. Install Frontend Dependencies

```bash
cd d:\vscodefiles\task-manager\frontend
npm install
```

### 2. Run the Frontend Development Server

```bash
cd d:\vscodefiles\task-manager\frontend
npm run dev
```

The frontend will start on `http://localhost:3000`

## Running Everything Together

### Terminal 1 - Backend

```bash
cd d:\vscodefiles\task-manager
python run.py
```

### Terminal 2 - Frontend

```bash
cd d:\vscodefiles\task-manager\frontend
npm install  # First time only
npm run dev
```

Then open your browser and go to: **http://localhost:3000**

## Features Overview

### Authentication

- Sign up with name, email, and password
- Secure login with JWT tokens
- Automatic logout

### Task Management

- ✅ Create new tasks with title, description, and priority
- 📋 View all your tasks in a beautiful grid
- ✏️ Edit tasks anytime
- 🏷️ Filter by status (Pending, In Progress, Completed)
- 🎯 Filter by priority (Low, Medium, High)
- 📄 Pagination for large task lists
- 🗑️ Delete tasks
- ✔️ Mark tasks as complete with one click
- 📅 View task creation dates

## API Endpoints

### Authentication

- `POST /api/signup` - Create new account
- `POST /api/login` - Login to account

### Tasks

- `GET /api/tasks` - Get all tasks (supports filters & pagination)
- `POST /api/tasks` - Create new task (requires auth)
- `GET /api/tasks/<id>` - Get single task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task
- `GET /api/health` - Health check

## Customization

### Change Frontend Port

Edit `frontend/vite.config.js`:

```javascript
server: {
  port: 3000,  // Change this to your desired port
}
```

### Change Backend Port

Edit `run.py`:

```python
app.run(host="0.0.0.0", port=5000, debug=True)  # Change port here
```

### Update API URL

If backend is on different URL, edit `frontend/src/services/api.js`:

```javascript
const API_BASE_URL = "http://localhost:5000/api"; // Update this
```

## Troubleshooting

### Frontend can't connect to backend

- Make sure backend is running on port 5000
- Check CORS is enabled in backend (it is by default)
- Check browser console for error messages

### "npm: command not found"

- Install Node.js from https://nodejs.org

### "python: command not found"

- Install Python from https://python.org

### Backend port already in use

- Kill the process: `lsof -ti:5000 | xargs kill -9`
- Or change the port in `run.py`

## Build for Production

### Frontend

```bash
cd frontend
npm run build
```

This creates an optimized build in `frontend/dist/`

### Deploy Frontend

You can deploy the `frontend/dist/` folder to any static hosting (Netlify, Vercel, AWS S3, etc.)

## Project Structure

```
task-manager/
├── app/                          # Flask backend
│   ├── routes/                   # API routes
│   ├── models/                   # Database models
│   ├── services/                 # Business logic
│   └── utils/                    # Helper functions
├── frontend/                     # React frontend
│   ├── src/
│   │   ├── components/          # Reusable components
│   │   ├── pages/               # Full pages
│   │   ├── services/            # API calls
│   │   └── App.jsx
│   └── package.json
├── run.py                        # Flask entry point
└── requirements.txt              # Python dependencies
```

## Next Steps

1. Start both servers (backend and frontend)
2. Create an account at login page
3. Start creating and managing your tasks
4. Explore all features!

Enjoy your task manager! 🎉
