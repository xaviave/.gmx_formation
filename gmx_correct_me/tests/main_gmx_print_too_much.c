#include "gmx.h"
#include <stdio.h>

int main()
{
    gmx_print_too_much("bonjour", 3);
    printf("/");
    gmx_print_too_much("ueueueue", 0);
    printf("/");
    gmx_print_too_much("coucou", 10);
    printf("/");
    gmx_print_too_much("error", -1);
    printf("/");
    gmx_print_too_much("xavoubgxavoubgxavoubgxavoubgxavoubgxavoubgxavoubgxavoubg", 30);
}