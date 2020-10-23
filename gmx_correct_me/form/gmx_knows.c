#include <stdio.h>

int gmx_knows(char x, char *str)
{
    int i;
    int nu;

    i = 0;
    nu = 0;
    while (str[i])
    {
        if (str[i] == x)
            nu++;
        i++;
    }
    return (nu);
}