#include "gmx.h"
#include <stdio.h>

int main()
{
    gmx_print_me("aaaaaaaaaaa");
    printf("/");
    gmx_print_me("bbbbbbbbbbb");
    printf("/");
    gmx_print_me("123");
    printf("/");
    gmx_print_me("");
}