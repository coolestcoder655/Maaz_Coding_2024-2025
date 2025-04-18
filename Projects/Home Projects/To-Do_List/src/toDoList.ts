interface Task {
    id: number;
    title: string;
    completed: boolean;
    dueDate: Date | null;
    priority: 'low' | 'medium' | 'high';
}

class ToDoList {
    tasks: Task[];

    constructor() {
        this.tasks = [];
    }

    addTask(newTitle: string, newDueDate: Date | null, newPriority: 'low' | 'medium' | 'high'): Task {
        const newTask: Task = {
            id: this.tasks.length + 1,
            title: newTitle,
            completed: false,
            dueDate: newDueDate,
            priority: newPriority
        };
        this.tasks.push(newTask);
        return newTask;
    }
}