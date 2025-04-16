var taskContainer = document.getElementById("taskContainer");
var taskInput = document.getElementById("taskInput");
var addTaskButton = document.getElementById("addTaskButton");
addTaskButton.addEventListener("click", addTask);
function addTask() {
    var task = document.createElement("li");
    task.innerHTML = taskInput.value;
    task.onclick = removeTask;
    taskContainer.appendChild(task);
    taskInput.value = "";
}
function removeTask() {
    taskContainer.removeChild(this);
}
