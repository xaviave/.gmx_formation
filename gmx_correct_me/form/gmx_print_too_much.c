#include <stdio.h>

void gmx_print_too_much(char *str, int x)
{
    int i;
    int len;

    i = -1;
    len = 0;
    while (str[len])
        len++;
    if (x > len || x < 0)
        return;
    printf("%c", str[x]);
    while (++i < x)
        printf("%c", str[i]);
}