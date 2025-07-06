#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void clearOutput();

int main()
{
    int product = 0;

    printf("Enter a number: ");
    scanf("%d", &product);

    clearOutput();

    for (int i = 1; i <= 12; i++)
    {
        printf("%d * %d = %d\n", product, i, product * i);
        Sleep(100);
    };

    return 0;
}

void clearOutput()
{
    system("cls");
    return;
};