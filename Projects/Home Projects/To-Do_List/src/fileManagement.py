from json import load, dump
from datetime import datetime

def readFile() -> list:
    with open("taskFile.json", "r") as file:
        data = load(file)
        data = data["tasks"]
    tasks = [
        (taskName, taskDetails["description"], (datetime.strptime(taskDetails["deadline"], "%Y-%m-%d").date()), taskDetails["priority"], taskDetails["isCompleted"])
        for taskName, taskDetails in data.items()
    ]
    return tasks

def truncateFile() -> None:
    with open("taskFile.json", "w") as file:
        file.write("") # Clear the file

def writeFile(tasks) -> None:
    truncateFile()

    with open("taskFile.json", "w") as file:
        data = {
            "tasks": {
                task[0]: {
                    "description": task[1],
                    "deadline": task[2],
                    "priority": task[3],
                    "isCompleted": task[4]
                }
                for task in tasks
            }
        }
        dump(data, file, indent=4)