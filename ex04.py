#!/usr/bin/env python

import random


class Board:
    '''Board.
    An object representing a Game of Life board.
    '''

    def __init__(self):
        self.cells = {}

    @classmethod
    def read_board(cls, filename):
        '''Read a board from a text file.
        Given a text file in the format of n cells per line,
        read the file and initialize the board.
        '''

        board = cls()

        with open(filename, 'r') as f:
            for x, line in enumerate(f):
                line = line.rstrip('\n')
                for y, char in enumerate(line):
                    cell = Cell((x, y), int(char))
                    board.add_cell((x, y), cell)

                    board.width = x + 1
                board.height = y + 1

        return board

    @classmethod
    def make_board(cls, width=5, height=5):
        '''Create a new board.
        Given dimensions, generate a board with cells of random value.
        '''
        board = cls()
        board.width = width
        board.height = height

        for x in range(width):
            for y in range(height):
                cell = Cell((x, y), random.randint(0, 1))
                board.add_cell((x, y), cell)

        return board

    def add_cell(self, coords, cell):
        cell.board = self
        self.cells[coords] = cell

    def get_cell(self, coord):
        return self.cells.get(coord, None)

    def __str__(self):
        out = ''
        for x in range(self.width):
            for y in range(self.height):
                value = self.cells.get((x, y)).value
                out += str(value)
            out += '\n'
        return out


class Cell:
    '''Cell.
    An object representing a single cell on a Game of Life board.
    '''

    def __init__(self, coords, value):
        self.coords = coords
        self.value = value

    @property
    def value(self):
        if self._value:
            return 1
        return 0

    @value.setter
    def value(self, val):
        self._value = bool(val)

    def get_neighbors(self):
        '''Get neighbors.
        Return a dict of coord => cell for all adjacent cells.
        '''
        neighbors = {}
        x, y = self.coords
        for coord in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if coord in self.board.cells:
                neighbors[coord] = self.board.get_cell(coord)

        return neighbors


if __name__ == '__main__':

    #b = Board.read_board('board.txt')
    b = Board.make_board(20, 20)
    #print b.cells.get((4, 4)).get_neighbors()
    print b
