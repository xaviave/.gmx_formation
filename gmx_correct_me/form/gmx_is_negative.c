#include <stdio.h>

char *gmx_is_negative(int number)
{
    if (number < 0)
        return "foo";
    else
        return "bar";
}