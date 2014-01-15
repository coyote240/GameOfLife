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

        What this method does NOT do is check for a valid format.
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
    def make_board(cls, width=5, height=None):
        '''Create a new board.
        Given dimensions, generate a board with cells of random value.
        '''
        if height is None:
            height = width

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

    def generate(self, generations=1):
        '''Advance board state n generations.
        Default to advancing one generation.

        **NOTE:
        It is VERY important that calc_next_state() and update()
        are called in separate loops.  Otherwise changes made during each
        generation would affect later state changes within the same
        generation.
        '''
        for g in range(generations):
            for cell in self.cells.values():
                cell.calc_next_state()
            for cell in self.cells.values():
                cell.update()

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

        The method to calculate the coordinates of neighbors is a bit
        brutal.  If I were to live with this code, I'd likely try to
        clean it up a bit.
        '''
        neighbors = {}
        x, y = self.coords
        for coord in [(x+1, y), (x-1, y), (x, y+1), (x, y-1),
                      (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)]:
            if coord in self.board.cells:
                neighbors[coord] = self.board.get_cell(coord)

        return neighbors

    def live_count(self):
        '''Return the number of living neighbors.'''
        neighbors = self.get_neighbors()
        alive = [c for c in neighbors.values() if c.value]
        return len(alive)

    def calc_next_state(self):
        '''Calculate next state.
        Calculate state of this cell after the next generation
        and store it locally.  This is the value of the cell after
        update() is called.
        '''
        alive = self.live_count()
        self.next_state = self.value

        if self.value:
            if alive < 2 or alive > 3:
                self.next_state = 0
        else:
            if alive == 3:
                self.next_state = 1

    def update(self):
        '''Update current state.
        Must be called after calc_next_state(), updates the value of
        this cell after n generations.
        '''
        self.value = self.next_state
        self.next_state = None


if __name__ == '__main__':

    b = Board.read_board('board.txt')
    #b = Board.make_board(20)
    print b

    b.generate()
    print b
