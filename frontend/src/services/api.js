import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const authAPI = {
  signup: (name, email, password) =>
    api.post('/signup', { name, email, password }),
  login: (email, password) =>
    api.post('/login', { email, password }),
}

export const taskAPI = {
  getTasks: (status = null, priority = null, page = 1, per_page = 10) => {
    const params = { page, per_page }
    if (status) params.status = status
    if (priority) params.priority = priority
    return api.get('/tasks', { params })
  },
  getTask: (taskId) => api.get(`/tasks/${taskId}`),
  createTask: (title, description, priority) =>
    api.post('/tasks', { title, description, priority }),
  updateTask: (taskId, data) =>
    api.put(`/tasks/${taskId}`, data),
  deleteTask: (taskId) =>
    api.delete(`/tasks/${taskId}`),
}

export default api
