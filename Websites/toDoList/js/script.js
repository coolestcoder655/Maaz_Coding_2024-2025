function addTask() {
    const taskInput = document.getElementById("taskInput").value;
    if (taskInput.trim() === "") {
        alert("Please enter a task.");
        return;
    }
    const taskList = document.getElementById("taskList")
    taskList.innerHTML += `<li>${taskInput} <button onclick="removeTask(this)">Remove</button></li>`;   
}