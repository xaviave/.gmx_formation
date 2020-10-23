#ifndef GMX_H
#define GMX_H

void gmx_putchar(char c);
void gmx_print_alphabet(void);
void gmx_print_numbers(void);
void gmx_print_me(char *me);
char *gmx_is_negative(int number);
void gmx_is_unique(void);
void gmx_print_too_much(char *str, int x);
int gmx_knows(char x, char *str);

#endif