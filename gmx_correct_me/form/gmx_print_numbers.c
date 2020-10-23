#include <unistd.h>

void gmx_print_numbers(void)
{
    write(1, "0123456789", 10);
}