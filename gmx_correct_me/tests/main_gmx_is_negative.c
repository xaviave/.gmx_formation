#include "gmx.h"
#include <stdio.h>

int main()
{
    printf("%s/", gmx_is_negative(0));
    printf("%s/", gmx_is_negative(-1));
    printf("%s/", gmx_is_negative(2345));
    printf("%s", gmx_is_negative(134556));
}