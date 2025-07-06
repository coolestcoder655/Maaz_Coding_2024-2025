#include <stdio.h>

int main()
{
    float number1;
    float number2;
    float result;
    char operator;

    while (1)
    {
        printf("Calculator: \n");
        printf("Enter Number 1: ");
        scanf("%f", &number1);

        printf("\nEnter Operator (+, -, /, *): ");
        scanf(" %c", &operator);

        printf("\nEnter Number 2: ");
        scanf("%f", &number2);

        switch (operator)
        {
        case '+':
            result = number1 + number2;
            break;

        case '-':
            result = number1 - number2;
            break;

        case '/':
            result = number1 / number2;
            break;

        case '*':
            result = number1 * number2;
            break;

        default:
            printf("\nError: You entered an incorrect operation. \n");
            continue; // Skip to next iteration if invalid operator
        }

        // Display result as integer if it's a whole number, otherwise as float
        if (result == (int)result)
        {
            printf("Result: %d\n", (int)result);
        }
        else
        {
            printf("Result: %.2f\n", result);
        }

        break;
    }

    printf("Thank you for using the calculator!\n");

    return 0;
}