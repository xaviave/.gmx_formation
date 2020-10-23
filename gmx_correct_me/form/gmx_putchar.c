#include <unistd.h>

void gmx_putchar(char c)
{
    write(1, &c, 1);
}