from toDo_List import ToDo_List
from datetime import date
from globalVariables import *
from state import State
from colorama import Style, Fore, Back


def main():
    try:
        global state
        global ToDo_List
        global running
        state = State.Main_Menu
        ToDo_List = ToDo_List(tasks=readFile())
        running = True


        print("Welcome to the To-Do List App!")

        while running:
            if state == State.Main_Menu:
                print("Main Menu:")
                print("1. Add Task")
                print("2. Remove Task")
                print("3. Complete Task")
                print("4. View Tasks")
                print("0. Exit")

                print("Today's Date:", ToDo_List.today)

                print(ToDo_List.__repr__())

                try:
                    state = State(int(input("Select an option: ")))
                except ValueError:
                    print("Invalid Input.")

            elif state == State.Add_Task:
                print("Add Task:")
                taskName = input("Task Name: ")
                description = input("Description: \n    ")
                try:
                    year, month, day = map(int, input("Deadline (YYYY-MM-DD): ").split("-"))
                    deadline = ToDo_List.createDate(year, month, day)
                except ValueError:
                    print("Invalid Input.")
                    continue
                try:
                    priority = int(input("Priority (1-5): "))
                except ValueError:
                    print("Invalid Input.")
                    continue
                ToDo_List.addTask(taskName, description, deadline, priority)
                state = State.Main_Menu
            elif state == State.Remove_Task:
                print("Remove Task:")
                taskName = input("Task Name: ")
                remove = ToDo_List.removeTask(taskName)
                print("Task Removed." if remove else ToDo_List.taskError)
                state = State.Main_Menu
            elif state == State.Complete_Task:
                print("Complete Task:")
                taskName = input("Task Name: ")
                ToDo_List.completeTask(taskName)
                state = State.Main_Menu
            elif state == State.View_Tasks:
                print("View Tasks:")
                ToDo_List.viewTasks()
                input("Press Enter to Continue.")
                Style.RESET_ALL # Reset the color scheme
                state = State.Main_Menu
            elif state == State.Exit:
                running = False
    except KeyboardInterrupt:
        print("Exiting...")
    del ToDo_List



if __name__ == "__main__":
    main()
