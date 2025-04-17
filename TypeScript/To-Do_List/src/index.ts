// Entry point for the to-do list application

import * as readline from 'readline';

interface Task {
  id: number;
  title: string;
  description?: string;
  dueDate?: Date;
  priority?: 'low' | 'medium' | 'high';
  isCompleted: boolean;
}

export class ToDoList {
  private tasks: Task[] = [];

  addTask(title: string, description?: string, dueDate?: Date, priority?: 'low' | 'medium' | 'high'): Task {
    const newTask: Task = {
      id: this.tasks.length + 1,
      title,
      description,
      dueDate,
      priority,
      isCompleted: false,
    };
    this.tasks.push(newTask);
    return newTask;
  }

  editTask(id: number, updates: Partial<Task>): Task | undefined {
    const task = this.tasks.find((task) => task.id === id);
    if (task) {
      Object.assign(task, updates);
    }
    return task;
  }

  deleteTask(id: number): boolean {
    const index = this.tasks.findIndex((task) => task.id === id);
    if (index !== -1) {
      this.tasks.splice(index, 1);
      return true;
    }
    return false;
  }

  listTasks(): Task[] {
    return this.tasks;
  }
}

const toDoList = new ToDoList();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function showMenu() {
  console.log('\nTo-Do List Application');
  console.log('1. Add Task');
  console.log('2. Remove Task');
  console.log('3. View Tasks');
  console.log('4. Exit');
  rl.question('Choose an option: ', handleMenu);
}

function handleMenu(option: string) {
  switch (option) {
    case '1':
      rl.question('Enter task title: ', (title) => {
        rl.question('Enter task description (optional): ', (description) => {
          rl.question('Enter due date (YYYY-MM-DD, optional): ', (dueDate) => {
            rl.question('Enter priority (low, medium, high, optional): ', (priority) => {
              const task = toDoList.addTask(
                title,
                description || undefined,
                dueDate ? new Date(dueDate) : undefined,
                (priority as 'low' | 'medium' | 'high') || undefined
              );
              console.log('Task added:', task);
              showMenu();
            });
          });
        });
      });
      break;
    case '2':
      rl.question('Enter task ID to remove: ', (id) => {
        const success = toDoList.deleteTask(Number(id));
        if (success) {
          console.log('Task removed successfully.');
        } else {
          console.log('Task not found.');
        }
        showMenu();
      });
      break;
    case '3':
      console.log('Current Tasks:', toDoList.listTasks());
      showMenu();
      break;
    case '4':
      rl.close();
      break;
    default:
      console.log('Invalid option. Please try again.');
      showMenu();
      break;
  }
}

showMenu();