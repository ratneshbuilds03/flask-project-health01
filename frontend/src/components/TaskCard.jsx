import { useState } from 'react'
import { FiEdit2, FiTrash2, FiChevronDown, FiCheck } from 'react-icons/fi'
import './TaskCard.css'

export default function TaskCard({ task, onUpdate, onDelete }) {
  const [isExpanded, setIsExpanded] = useState(false)
  const [isEditing, setIsEditing] = useState(false)
  const [title, setTitle] = useState(task.title)
  const [description, setDescription] = useState(task.description || '')
  const [priority, setPriority] = useState(task.priority)
  const [status, setStatus] = useState(task.status)

  const handleSave = async () => {
    await onUpdate(task.id, { title, description, priority, status })
    setIsEditing(false)
  }

  const getStatusColor = (status) => {
    const colors = {
      pending: '#ffa500',
      in_progress: '#667eea',
      completed: '#4caf50',
    }
    return colors[status] || '#999'
  }

  const getPriorityColor = (priority) => {
    const colors = {
      low: '#4caf50',
      medium: '#ff9800',
      high: '#f44336',
    }
    return colors[priority] || '#999'
  }

  return (
    <div className="task-card">
      {!isEditing ? (
        <>
          <div className="task-header">
            <div className="task-title-section">
              <button
                className="btn-expand"
                onClick={() => setIsExpanded(!isExpanded)}
              >
                <FiChevronDown style={{ transform: isExpanded ? 'rotate(180deg)' : 'rotate(0deg)' }} />
              </button>
              <h3 className="task-title">{title}</h3>
            </div>
            <div className="task-badges">
              <span className="badge status" style={{ backgroundColor: getStatusColor(status) }}>
                {status}
              </span>
              <span className="badge priority" style={{ backgroundColor: getPriorityColor(priority) }}>
                {priority}
              </span>
            </div>
          </div>

          {isExpanded && (
            <div className="task-details">
              {description && <p className="task-description">{description}</p>}
              <div className="task-meta">
                <small>{new Date(task.created_at).toLocaleDateString()}</small>
              </div>
            </div>
          )}

          <div className="task-actions">
            <button
              className="btn-action edit"
              onClick={() => setIsEditing(true)}
              title="Edit task"
            >
              <FiEdit2 />
            </button>
            <button
              className="btn-action delete"
              onClick={() => onDelete(task.id)}
              title="Delete task"
            >
              <FiTrash2 />
            </button>
            {status !== 'completed' && (
              <button
                className="btn-action complete"
                onClick={() => onUpdate(task.id, { status: 'completed' })}
                title="Mark as complete"
              >
                <FiCheck />
              </button>
            )}
          </div>
        </>
      ) : (
        <div className="task-edit-form">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="edit-input"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="edit-textarea"
            rows={3}
          />
          <div className="edit-selects">
            <select value={status} onChange={(e) => setStatus(e.target.value)}>
              <option value="pending">Pending</option>
              <option value="in_progress">In Progress</option>
              <option value="completed">Completed</option>
            </select>
            <select value={priority} onChange={(e) => setPriority(e.target.value)}>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>
          <div className="edit-actions">
            <button type="button" className="btn-cancel" onClick={() => setIsEditing(false)}>
              Cancel
            </button>
            <button type="button" className="btn-save" onClick={handleSave}>
              Save
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
