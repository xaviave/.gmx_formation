#include <stdio.h>

int main(int ac, char **av)
{
    int i;

    i = 0;
    if (ac < 2)
        return (0);
    while (av[1][i])
    {
        if (av[1][i] > 96 && av[1][i] < 123)
            av[1][i] -= 32;
        i++;
    }
    printf("%s", av[1]);
    return (1);
}