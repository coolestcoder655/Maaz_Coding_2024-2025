#include <stdio.h>
#include <stdbool.h>

bool EvenOrOdd(int n);

int main()
{

    int choice = 0;

    printf("*** EVEN OR ODD ***\n");

    printf("\nPlease enter a number: ");
    scanf("%d", &choice);

    if (EvenOrOdd(choice))
    {
        printf("Your number is even!");
    }
    else
    {
        printf("Your number is odd!");
    };

    return 0;
};

bool EvenOrOdd(int n)
{
    return n % 2 == 0;
};