#include <stdio.h>

typedef int Number;
typedef char String[50];
typedef char Initals[3];

int main()
{
    Initals user1 = "MK";
    Initals user2 = "SS";
    Initals user3 = "AH";
    Initals user4 = "ST";

    printf("%s\n", user1);
    printf("%s\n", user2);
    printf("%s\n", user3);
    printf("%s\n", user4);

    return 0;
}