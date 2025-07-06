#include <stdio.h>

int main()
{
    int numbers[][3] = {{1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9}};

    for (int i = 0; i < 3; i++)
    {
        printf("| ");
        for (int x = 0; x < 3; x++)
        {
            printf("%d ", numbers[i][x]);
        };
    };
    return 0;
}