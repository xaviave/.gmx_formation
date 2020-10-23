# Day 1 of gmx programming formation
# A. Vocabulary and word meaning:
	
1. Question google, the people around you and obviously you: What is a programming and scripting language and why are there so many of them?
2. Read [this](https://learnxinyminutes.com/docs/c/).
3. Re-read it and on every word you had a doubt, search on the internet what it’s real meaning.
4. Now, you’ve faced a programming way to “quickly understand” a language, read [this](https://developerinsider.co/c-programming-language-cheat-sheet/).


# B. Terminal:

1. Biggest notion to understand here, the terminal and everything that you can do with it. Read [this](https://gist.github.com/poopsplat/7195274)
2. Now, that you know how to use the terminal, you have to ONLY use it while manipulating files.
3. Read [this](https://www.freecodecamp.org/news/how-you-can-be-more-productive-right-now-using-bash-29a976fb1ab4/) too, it may be useful.
4. You’ve seen the command `man` right, each time you wanted an information or anything about a command or a function -> man `function/command`
5. C is a language that need to be compiled, but you know it now, so read how to do it: [XavBg](https://www.geeksforgeeks.org/compiling-a-c-program-behind-the-scenes/)

# C. C:
	
Remember your past lecture…

To invoque `gmx`, the one and only corrector, use `gmx correct me` followed by your files directory.

All files you gonna create must be in a directory else gmx coud not correct yout exercices.
Also, always use the flags `-Wall -Wextra -Werror`.

## I. Introduction

1. *file name*: *gmx_putchar.c* - Write a function that prints the parameter pass to it.
prototype: `void gmx_putchar(char c);`
Use `write(1, &c, 1);`
2. *file name*: *gmx_print_alphabet.c* - Write a function that prints the alphabet and a newline at the end.
- prototype: `void gmx_print_alphabet(void);`
3. *file name*: *gmx_print_numbers.c* - Write a function that prints all the numbers.
- prototype: `void gmx_print_numbers(void);`
4. *file name*: *gmx_my_name.c* - Write a function that prints your name but inverted and tabulation at the end.
- prototype: `void gmx_my_name(void);`


## II. Variables and logic
	
*From here, you can now use `printf()`.
Don’t forget to think about the crash and the way to avoid it*.
1. *file name*: *gmx_print_me.c* - Write a function that prints the var given.
- prototype: `void gmx_print_me(char *me);`
2. *file name*: *gmx_is_negative.c* - Write a function that returns `foo` if a number is negative and `bar` if it’s positive.
- prototype: `char *gmx_is_negative(int number);`
3. *file name*: *gmx_is_unique.c* - Write a function that prints every unique combinations of three numbers in ascending order. Example, I can print 012 but not 021 like 987 is not ok because of 789. 001 isn’t a choose, guess what, just two differents numbers.
        
        012 013 014 ...

- prototype: `void gmx_is_unique(void);`

~~Help: you see here somethins like `void`, `int` or `char` and `char *`, this is the type of a variable, for iteration in `char *` arrays, you will face a problem, how to stop the looping, check wtf is~~`\0`

4. *file name*: *gmx_print_too_much.c* - Ok you know for sure how to print now but that's not the main things in here, let's loop in `int` and `char arrays` __define by the *__ - Write a function that prints in the first time the letter at the position `x` in the string `str` then your function have to print all the character before this position.

        Example: char *str = "bonjour", int x = 3`, the print will be: `jbon` or `jnob`

- prototype: `void gmx_print_too_much(char *str, int x);`
5. *file name*: *gmx_knows.c* - Write a function that returns the number of char `x` matching with the characters in the string `str` given.
- prototype: `int gmx_knows(char x, char *str);`

## III. Programs

1.	*file name*: *lenght.c* - Write a program that takes a string in argument and prints it’s length.
2.	*file name*: *uppercase.c* - Write a program that takes a string in argument and prints it but uppercase.
3.	*file name*: *xavbg.c* - Write a program that outputs the string representation of numbers from 1 to 50. But for multiples of three it should output “Xavou” instead of the number and for the multiples of five output “Bg”. For numbers which are multiples of both three and five output “XavouBg”. Don't forget the newline after each iteration.

# D. End of the day

### Questions time and interrogations.
*No questions about the function's and program's names are allowed*

Think about the logic behind everything you've just done. The main subject here is to visualize abstract concept that you have faced. Like highschool maths, some things are too conceptual and your brain gonna wanted to erase it this night but I'm here to answer questions.
This will allow you to assimilate theories and your dreams will be arithmeticaly sweet.
