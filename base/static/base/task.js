let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

function renderTasks() {
  const container = document.getElementById('taskListContainer');
  if (tasks.length === 0) {
    container.innerHTML = '<div style="text-align:center; padding:1rem;">No tasks yet. Add a new one.</div>';
    return;
  }
  container.innerHTML = tasks.map((task, idx) => `
    <div class="task-item ${task.completed ? 'completed' : ''}">
      <div class="task-info">
        <input type="checkbox" ${task.completed ? 'checked' : ''} data-idx="${idx}" class="task-check">
        <div>
          <div class="task-text">${escapeHtml(task.text)}</div>
          <div class="task-details">
            <span>📅 Due: ${task.dueDate || 'No date'} ⏰ ${task.dueTime || 'No time'}</span>
          </div>
        </div>
      </div>
      <div class="task-actions">
        <button class="icon-btn delete-task" data-idx="${idx}">🗑️</button>
      </div>
    </div>
  `).join('');
  
  document.querySelectorAll('.task-check').forEach(cb => {
    cb.addEventListener('change', (e) => {
      const idx = e.target.dataset.idx;
      tasks[idx].completed = e.target.checked;
      saveTasks();
      renderTasks();
    });
  });
  document.querySelectorAll('.delete-task').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const idx = btn.dataset.idx;
      tasks.splice(idx, 1);
      saveTasks();
      renderTasks();
    });
  });
}

function escapeHtml(str) {
  return str.replace(/[&<>]/g, function(m) {
    if (m === '&') return '&amp;';
    if (m === '<') return '&lt;';
    if (m === '>') return '&gt;';
    return m;
  });
}

document.getElementById('addTaskBtn').addEventListener('click', () => {
  const taskInput = document.getElementById('taskInput');
  const dueDate = document.getElementById('dueDate');
  const dueTime = document.getElementById('dueTime');
  
  const text = taskInput.value.trim();
  if (text === '') {
    alert('Please enter a task description');
    return;
  }
  tasks.push({
    text: text,
    dueDate: dueDate.value || '',
    dueTime: dueTime.value || '',
    completed: false
  });
  saveTasks();
  renderTasks();
  taskInput.value = '';
  dueDate.value = '';
  dueTime.value = '';
});

renderTasks();