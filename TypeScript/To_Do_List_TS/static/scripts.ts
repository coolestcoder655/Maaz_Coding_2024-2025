const taskContainer: any = document.getElementById("taskContainer");
const taskInput: any = document.getElementById("taskInput");
const addTaskButton: any = document.getElementById("addTaskButton");

addTaskButton.addEventListener("click", addTask);

function addTask(): void {
    let task: any = document.createElement("li");
    task.innerHTML = taskInput.value;
    task.onclick = removeTask;

    taskContainer.appendChild(task);
    taskInput.value = "";
}

function removeTask(): void {
    taskContainer.removeChild(this)
}