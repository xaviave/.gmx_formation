#include "gmx.h"
#include <stdio.h>

int main()
{
    printf("%i/", gmx_knows('a', "aaaaaaaaaaaaa"));
    printf("%i/", gmx_knows('|', "bonjour|ca|va"));
    printf("%i/", gmx_knows('-', "xavou bg"));
    printf("%i", gmx_knows(' ', "et oui"));
}