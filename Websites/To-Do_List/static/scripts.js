const taskList = document.getElementById("taskList");

document.getElementById("addTaskButton").addEventListener("click", addTask);
document.getElementById("loadListButton").addEventListener("click", loadList);

function addTask() {
    let task = document.createElement("li");
    task.innerHTML = document.getElementById("taskInput").value;
    task.onclick = removeTask;
    taskList.appendChild(task);
    saveList();
}

function removeTask() {
    taskList.removeChild(this);
}

function saveList() {
    localStorage.setItem("taskList", JSON.stringify(taskList));
}

function loadList() {
    let jsonString = localStorage.getItem("taskList");
    localStorage.setItem("taskList", JSON.parse(jsonString));
    if (taskList.length <= 0) {
        console.error("There is no task list in local storage. Please create a new list. If this error continues occurring, please contact developer.");
    }
}

