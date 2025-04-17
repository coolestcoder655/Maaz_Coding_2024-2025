import express from 'express';
import bodyParser from 'body-parser';
import { ToDoList } from './index';

const app = express();
const port = 3000;
const toDoList = new ToDoList();

app.use(bodyParser.json());

// API to list all tasks
app.get('/tasks', (req, res) => {
  res.json(toDoList.listTasks());
});

// API to add a new task
app.post('/tasks', (req, res) => {
  const { title, description, dueDate, priority } = req.body;
  if (!title) {
    return res.status(400).json({ error: 'Title is required' });
  }
  const task = toDoList.addTask(
    title,
    description,
    dueDate ? new Date(dueDate) : undefined,
    priority
  );
  res.status(201).json(task);
});

// API to edit a task
app.put('/tasks/:id', (req, res) => {
  const { id } = req.params;
  const updates = req.body;
  const updatedTask = toDoList.editTask(Number(id), updates);
  if (updatedTask) {
    res.json(updatedTask);
  } else {
    res.status(404).json({ error: 'Task not found' });
  }
});

// API to delete a task
app.delete('/tasks/:id', (req, res) => {
  const { id } = req.params;
  const success = toDoList.deleteTask(Number(id));
  if (success) {
    res.status(204).send();
  } else {
    res.status(404).json({ error: 'Task not found' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});