#include <stdio.h>

int main(int ac, char **av)
{
    int i;

    i = 0;
    if (ac < 2)
        return (0);
    while (av[1][i])
        i++;
    printf("%i", i);
    return (1);
}