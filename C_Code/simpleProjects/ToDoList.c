#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// ✅ Teaches: Arrays, strings, loops, file I/O, JSON handling

// Store 10 tasks in an array and persist them to tasks.json

// Let the user add, remove, or view tasks

#define MAX_TASKS 10
#define MAX_TASK_LENGTH 100
#define FILENAME "tasks.json"

typedef enum
{
    VIEW,
    ADD,
    REMOVE,
    MAINMENU
} State;

void showTasks(char tasks[][MAX_TASK_LENGTH], int *taskCount);
void addTask(char tasks[][MAX_TASK_LENGTH], int *taskCount);
void removeTask(char tasks[][MAX_TASK_LENGTH], int *taskCount);
void removeItem(char tasks[][MAX_TASK_LENGTH], int *taskCount, int indexToRemove);
void clearOutput();
void saveTasksToFile(char tasks[][MAX_TASK_LENGTH], int taskCount);
void loadTasksFromFile(char tasks[][MAX_TASK_LENGTH], int *taskCount);

int main()
{
    char tasks[MAX_TASKS][MAX_TASK_LENGTH] = {0};
    int taskCount = 0;
    State state = MAINMENU;
    bool isRunning = true;
    int choice;

    // Load existing tasks from file
    loadTasksFromFile(tasks, &taskCount);

    do
    {
        clearOutput();
        printf("=== TO-DO LIST MENU ===\n");
        printf("1. View Tasks\n");
        printf("2. Add Task\n");
        printf("3. Remove Task\n");
        printf("4. Exit\n");
        printf("Enter your choice (1-4): ");
        scanf("%d", &choice);
        
        switch (choice)
        {
        case 1:
            state = VIEW;
            showTasks(tasks, &taskCount);
            printf("\nPress any key to continue...");
            getchar(); // consume newline
            getchar(); // wait for user input
            break;

        case 2:
            state = ADD;
            addTask(tasks, &taskCount);
            saveTasksToFile(tasks, taskCount); // Save after adding
            break;

        case 3:
            state = REMOVE;
            removeTask(tasks, &taskCount);
            saveTasksToFile(tasks, taskCount); // Save after removing
            break;
            
        case 4:
            isRunning = false;
            break;

        default:
            printf("\nIncorrect choice. Please try again.");
            printf("\nPress any key to continue...");
            getchar(); // consume newline
            getchar(); // wait for user input
            break;
        }
    } while (isRunning);

    clearOutput();
    printf("Thank you for using the To-Do List app, created by Maaz Khokhar!");
    return 0;
}

void showTasks(char tasks[][MAX_TASK_LENGTH], int *taskCount)
{
    if (*taskCount == 0)
    {
        printf("\nNo tasks available!\n");
        return;
    }
    
    printf("\n=== YOUR TASKS ===\n");
    for (int i = 0; i < *taskCount; i++)
    {
        printf("%d. %s\n", i + 1, tasks[i]);
    }
}

void addTask(char tasks[][MAX_TASK_LENGTH], int *taskCount)
{
    if (*taskCount >= MAX_TASKS)
    {
        printf("\nTask list is full! Cannot add more tasks.\n");
        printf("Press any key to continue...");
        getchar(); // consume newline
        getchar(); // wait for user input
        return;
    }
    
    printf("\nEnter a name for the new task: ");
    getchar(); // consume newline from previous input
    fgets(tasks[*taskCount], MAX_TASK_LENGTH, stdin);
    
    // Remove newline character if present
    size_t len = strlen(tasks[*taskCount]);
    if (len > 0 && tasks[*taskCount][len-1] == '\n')
    {
        tasks[*taskCount][len-1] = '\0';
    }
    
    (*taskCount)++;
    printf("Task added successfully!\n");
    printf("Press any key to continue...");
    getchar(); // wait for user input
}

void removeTask(char tasks[][MAX_TASK_LENGTH], int *taskCount)
{
    if (*taskCount == 0)
    {
        printf("\nNo tasks to remove!\n");
        printf("Press any key to continue...");
        getchar(); // consume newline
        getchar(); // wait for user input
        return;
    }
    
    printf("\n=== CURRENT TASKS ===\n");
    for (int i = 0; i < *taskCount; i++)
    {
        printf("%d. %s\n", i + 1, tasks[i]);
    }

    int indexToRemove;
    printf("\nEnter task number to remove (1 - %d): ", *taskCount);
    scanf("%d", &indexToRemove);
    
    if (indexToRemove < 1 || indexToRemove > *taskCount)
    {
        printf("Invalid task number!\n");
        printf("Press any key to continue...");
        getchar(); // consume newline
        getchar(); // wait for user input
        return;
    }

    removeItem(tasks, taskCount, indexToRemove - 1); // Convert to 0-based index
    printf("Task removed successfully!\n");
    printf("Press any key to continue...");
    getchar(); // consume newline
    getchar(); // wait for user input
}

void removeItem(char tasks[][MAX_TASK_LENGTH], int *taskCount, int indexToRemove)
{
    // Shift elements to the left
    for (int i = indexToRemove; i < *taskCount - 1; i++)
    {
        strcpy(tasks[i], tasks[i + 1]);
    }

    (*taskCount)--; // reduce task count
}

void clearOutput()
{
    system("cls");
}

void saveTasksToFile(char tasks[][MAX_TASK_LENGTH], int taskCount)
{
    FILE *file = fopen(FILENAME, "w");
    if (file == NULL)
    {
        printf("Error: Could not create/open %s for writing.\n", FILENAME);
        return;
    }

    fprintf(file, "{\n");
    fprintf(file, "  \"tasks\": [\n");
    
    for (int i = 0; i < taskCount; i++)
    {
        fprintf(file, "    \"%s\"", tasks[i]);
        if (i < taskCount - 1)
        {
            fprintf(file, ",");
        }
        fprintf(file, "\n");
    }
    
    fprintf(file, "  ],\n");
    fprintf(file, "  \"count\": %d\n", taskCount);
    fprintf(file, "}\n");

    fclose(file);
}

void loadTasksFromFile(char tasks[][MAX_TASK_LENGTH], int *taskCount)
{
    FILE *file = fopen(FILENAME, "r");
    if (file == NULL)
    {
        // File doesn't exist yet, start with empty task list
        *taskCount = 0;
        return;
    }

    char line[256];
    int currentTask = 0;
    bool inTasksArray = false;
    
    *taskCount = 0;

    while (fgets(line, sizeof(line), file) != NULL)
    {
        // Remove trailing newline
        line[strcspn(line, "\n")] = '\0';
        
        // Look for "tasks": [
        if (strstr(line, "\"tasks\"") && strstr(line, "["))
        {
            inTasksArray = true;
            continue;
        }
        
        // Look for end of tasks array
        if (inTasksArray && strstr(line, "]"))
        {
            inTasksArray = false;
            continue;
        }
        
        // Parse task lines
        if (inTasksArray)
        {
            char *start = strchr(line, '"');
            if (start != NULL)
            {
                start++; // Skip opening quote
                char *end = strrchr(line, '"');
                if (end != NULL && end > start)
                {
                    *end = '\0'; // Terminate at closing quote
                    strcpy(tasks[currentTask], start);
                    currentTask++;
                    (*taskCount)++;
                    
                    if (currentTask >= MAX_TASKS)
                        break;
                }
            }
        }
    }

    fclose(file);
}