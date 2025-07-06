#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

void clearOutput();

int main()
{
    srand(time(NULL)); // Seed the random number generator
    bool isRunning = true;
    char playAgain = '\0';

    while (isRunning)
    {
        int choice = 0;
        int randomNum = rand() % 10 + 1; // Random number between 1-10
        bool gameWon = false;

        clearOutput();
        printf("\n=== Guess the Number Game ===\n");
        printf("I'm thinking of a number between 1 and 10!\n\n");

        while (!gameWon)
        {
            printf("Choose a number: ");
            fflush(stdout); // Ensure prompt is displayed
            scanf("%d", &choice);

            if (choice == randomNum)
            {
                printf("\nYou Win!!!!!!!!!!!\n");
                gameWon = true;
            }
            else
            {
                printf("%s\n", (choice > randomNum ? "Too High!" : "Too Low!"));
            }
        }

        printf("The number was: %d\n\n", randomNum);
        printf("Play Again? (y/N): ");
        fflush(stdout); // Ensure prompt is displayed
        scanf(" %c", &playAgain);
        playAgain = tolower(playAgain);

        if (playAgain != 'y')
        {
            isRunning = false;
            printf("Thanks for playing!\n");
        }
    }

    return 0;
};

void clearOutput()
{
    system("cls"); // Use "cls" for Windows
    return;
}