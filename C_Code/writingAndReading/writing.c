#include <stdio.h>

int main()
{
    FILE *pFile = fopen("output.txt", "w");

    char text[] = "Who is the Sigma?\nI AM THE SIGMA!!!!!!!!!!!!!";

    if (pFile == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    };

    fprintf(pFile, "%s", text);

    printf("File was written sucessfully.");

    fclose(pFile);

    return 0;
}