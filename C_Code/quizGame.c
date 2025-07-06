#include <stdio.h>
#include <ctype.h>

int main()
{
    char questions[][100] = {
        "What is the largest planet in the solar system?",
        "What is the hottest planet in the solar system?",
        "What planet has the most moons?",
        "Is the Earth flat?"};

    char options[][100] = {
        "A. Jupiter\nB. Saturn\nC. Uranus\nD. Neptune",
        "A. Mercury\nB. Venus\nC. Earth\nD. Mars",
        "A. Earth\nB. Mars\nC. Jupiter\nD. Saturn",
        "A. True\nB. False\nC. Maybe\nD. Sometimes"};

    char answers[] = {'A', 'B', 'D', 'B'};

    int questionCount = sizeof(questions) / sizeof(questions[0]);

    char guess = '\0';
    int score = 0;

    printf("*** QUIZ GAME ***\n");

    for (int i = 0; i < questionCount; i++)
    {
        printf("\n%s\n", questions[i]);
        printf("\n%s\n", options[i]);
        printf("\nEnter your choice: ");
        scanf(" %c", &guess);

        guess = toupper(guess);

        if (guess == answers[i])
        {
            printf("Correct!\n");
            score += 1;
        }
        else
        {
            printf("Wrong!\n");
        };
    };

    float percent = 100 / questionCount * score;

    printf("\nFinal Score: %d/%d or %.0f percent.", score, questionCount, percent);
    return 0;
}