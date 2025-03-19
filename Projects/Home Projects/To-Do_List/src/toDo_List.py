from datetime import date
from fileManagement import writeFile
from colorama import Fore, Style, Back

class ToDo_List():
    today = date.today()
    isToday = lambda task_date: task_date <= ToDo_List.today
    isWeek = lambda date: ToDo_List.today.isocalendar()[1] == date.isocalendar()[1]
    isYear = lambda date: ToDo_List.today.year == date.year
    createDate = lambda year, month, day: date(year, month, day)
    taskError = "Task Not Found, No Task Modified."

    def __init__(self, tasks: list = []) -> None:
        self.tasks = tasks

    def __str__(self) -> str:
        return "\n".join(
            f"{task[0]}: {task[1]}\nDeadline: {task[2]}\nPriority: {task[3]}\nCompleted: {task[4]}\n"
            for task in self.tasks
        )
    
    def __repr__(self) -> list:
        return self.tasks

    def __del__(self):
        writeFile(self.tasks)

    def sortList(self) -> None:
        self.tasks = sorted(self.tasks, key = lambda task: (task[2], task[3]))



    def addTask(self, taskName: str, description: str, deadline: date, priority: int) -> None:
        self.tasks.append((taskName, description, deadline, priority, False))
        self.sortList()
    
    def removeTask(self, taskName: str) -> bool:
        before = self.tasks.copy()
        try:
            self.tasks = [task for task in self.tasks if task[0] != taskName]
            if self.tasks == before:
                raise ValueError
        except ValueError:
            print(__class__.taskError)
            return False
        self.sortList()
        return True

    def completeTask(self, taskName: str) -> None:
        try:
            for task in self.tasks:
                if task[0] == taskName:
                    task = (task[0], task[1], task[2], task[3], True)
                    break
            else:
                raise ValueError
        except ValueError:
            print(__class__.taskError)
        self.sortList()

    def viewTasks(self) -> None:
        for task in self.tasks:
            Style.RESET_ALL
            if __class__.isToday(task[2]):
                print(Back.RED + Fore.BLACK + Style.BRIGHT, end="")
            elif __class__.isWeek(task[2]):
                print(Fore.RED, Style.BRIGHT, end="")
            elif __class__.isYear(task[2]):
                print(Fore.BLACK, Style.DIM, end="")
            else:
                print(Fore.BLACK, Style.NORMAL, end="")
            print(f"{task[0]}: {task[1]}")
            print(f"Deadline: {task[2]}")
            print(f"Priority: {task[3]}")
            print(f"Is Completed: {task[4]}")
            print()