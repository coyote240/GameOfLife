#Game of Life
##Rally Software, Exercise 4

## Instructions

Write some code that evolves generations through the "game of life".  The input
will be a game board of cells, either alive (1) or dead (0).  The code should
take this board and create a new board for the next generation based on the
following rules:

1. Any live cell with fewer than two live neighbours dies (under- population)
2. Any live cell with two or three live neighbours lives on to the next
   generation (survival)
3. Any live cell with more than three live neighbours dies (overcrowding)
4. Any dead cell with exactly three live neighbours becomes a live cell
   (reproduction)

As an example, this game board as input:

    01000 
    10011 
    11001 
    01000 
    10001

Will have

    00000
    10111
    11111
    01000
    00000

## Solution

life.py has no external dependencies.

Running life.py from the terminal:

    python life.py

The program will load and parse the included board.txt, print it, and then
print the following generation.  The included board.txt mimics the input
from the exercise instructions and matches the expected output.

Alternately, I've included life2.py which accepts a number as an argument
and will create a board of that size, output it, and output one generation.

    python life2.py 20
