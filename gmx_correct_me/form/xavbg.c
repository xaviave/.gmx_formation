#include <stdio.h>

int main()
{
    int i;

    i = 0;
    while (++i < 50)
    {
        if (i % 3 == 0)
            printf("Xav");
        else if (i % 5 == 0)
            printf("Bg");
        else
            printf("%i", i);
        printf("\n");
    }
    return (1);
}