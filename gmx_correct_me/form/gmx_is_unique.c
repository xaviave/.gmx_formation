#include <stdio.h>

void gmx_is_unique(void)
{
    int i;
    int j;
    int k;

    i = 0;
    while (i < 10)
    {
        j = 1 + i;
        while (j < 10)
        {
            k = 1 + j;
            while (k < 10)
            {
                printf("%i%i%i", i, j, k);
                if (i < 7)
                    printf(" ");
                k++;
            }
            j++;
        }
        i++;
    }
}