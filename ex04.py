#!/usr/bin/env python


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
            for y, line in enumerate(f):
                line = line.rstrip('\n')
                for x, char in enumerate(line):
                    cell = Cell((x, y), bool(char))
                    board.add_cell((x, y), cell)

        return board

    @classmethod
    def make_board(cls, dimension=5):
        '''Create a new board.
        Given a dimension, generate a board.
        '''
        pass

    def add_cell(self, coords, cell):
        self.cells[coords] = cell


class Cell:
    '''Cell.
    An object representing a single cell on a Game of Life board.
    '''

    def __init__(self, coords, value):
        self.coords = coords
        self.value = value


if __name__ == '__main__':

    b = Board.read_board('board.txt')
    print b
