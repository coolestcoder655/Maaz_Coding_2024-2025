document.getElementById("addTaskButton").addEventListener("click", function() {
    let task = document.getElementById("taskInput").value;

    if (task.trim() === "") {
        console.error("Cannot Be Empty String");
        return false;
    }

    let taskList = document.getElementById("taskList");
    let child = document.createElement("li");
    child.textContent = task;

    taskList.appendChild(child);
    return true;
});