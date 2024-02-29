# Shell basics and C basics

## Topics

- Shell basics
- Shell permissions
- C basics
- C variables and loops

## Requirements

- The usage of any external help is not allowed, wich include: others help, any LLM such as chatGPT, copilot, etc.
- The concepts are the topics covered in past 2 weeks.
- Fork this repository and clone it to your local machine.
- Create a branch with your name.

- There are two types of questions:

  - Conceptual Questions: save the answer in a file called `checkpoint-01-answers`.

    - Format:

    ```
    1. a.
    2. b.
    ...
    ```

    - Once you have completed your test you can run `./checker.py` to check if your answers are correct.

  - Practical Questions: complete the file for each question.
    - Format:
    ```
    7-hello_holberton.c
    8-calculate_area.c
    9-print_even_numbers.c
    ```

## Question

1. Whats is a shell?

   a. A type of seafood

   b. A command-line interface

   c. A type of programming language

   d. A type of hardware device

2. Explaing the difference between `chmod` and `chown`.

   a. `chmod` changes file ownership, `chown` changes file permissions.

   b. `chmod` changes file permissions, `chown` changes file ownership.

   c. `chmod` is used in C programming, `chown` is used in shell scripting.

   d. `chmod` and `chown` are synonyms.

3. What is the purpose of a header file in C?

   a. To include additional libraries

   b. to declare variables

   c. To provide function prototypes

   d. to print output to the console

4. Describe the difference between `int` and `float` in C.

   a. `int` stores integer values, `float` stores floating-point values.

   b. `int` is used for input, `float` is used for output.

   c. `int` and `float` are synonyms.

   d. `int` is for text, `float` is for numbers.

5. What are variables in C? How are the declared?

   a. Variables store constant values, and they aredeclared using the `constant` keyword.

   b. Variables store data values, and they are declared using `data` keyword.

   c. Variables store information, and they are declared by specifying their type and name.

   d. Variables store file paths, and they are declared using the `path` keyword.

6. What are loops in programming, and what kind of loops are available in C?

   a. Loops are used for input/output operations, and there are two types of loops in C: `input` and `output`.

   b. Loops repeat a block of code until a specified condition is false, and there are three types of loops in C: `for`, `while`, and `do-while`.

   c. Loops are used to declare variables, and there are two types of loops in C: `int` and `float`.

   d. Loops are used to declare functions, and there are three types of loops in C: `main`, `puts`, and `printf`.

---

7. Write a C program to print `Hello, Holberton`, followed by a new line.

expected output:

```bash
$ gcc -Wall -Werror -Wextra -pedantic 7-hello_holberton.c -o hello_holberton && ./hello_holberton
Hello, Holberton
```

---

8. Write a c program to calculate the area of a rectangle.

expected output:

```bash
$ gcc -Wall -Werror -Wextra -pedantic 8-calculate_area.c -o calculate_area && ./calculate_area
Enter the width of the rectangle: 3
Enter the height of the rectangle: 5

Area of the rectangle: 15
```

---

9. Write a C program to print the first 10 even numbers.

Expected output:

```bash
$ gcc -Wall -Werror -Wextra -pedantic 9-print_even_numbers.c -o print_even_numbers && ./print_even_numbers
Frist 10 even numbers:
2
4
6
8
10
12
14
16
18
20
```
