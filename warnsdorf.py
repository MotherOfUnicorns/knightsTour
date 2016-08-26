'''Solves the knight's tour problem by Warnsdorf's rule.

last modified on Aug 26, 2016
by Yun'''

import matplotlib.pyplot as plt

BOARD_SIZE = (8, 8)
START_POS = (1, 0)

class Board():
    '''controls the whole chess board
    
    squares: list of Squares -> all squares on the chess board
    size: tuple -> size of the chess board
    start_pos: tuple -> starting position for the knight
    current_square: Square -> current square of the knight
    unvisited: int -> number of unvisited squares
    
    get_square()
    find_neighbours()
    possible_moves()
    next_move()
    tour() '''

    def __init__(self, size, start_pos):
        self.size = size
        self.start_pos = start_pos
        self.squares = [Square((row, col)) for row in range(self.size[0])
                for col in range(self.size[1])]
        # initialise the starting square
        self.current_square = self.get_square(self.start_pos)
        self.current_square.is_visited = True
        self.unvisited = self.size[0] * self.size[1] - 1

    def get_square(self, pos):
        '''gets the Square from self.squares given its position.'''
        return self.squares[pos[0] * self.size[1] + pos[1]]

    def find_neighbours(self, square):
        '''finds unvisited neighbours of curresnt square'''
        relative_pos = [(x,y) for x in [-1,1] for y in [-2,2]] + \
                       [(x,y) for x in [-2,2] for y in [-1,1]]
        neighbours = []
        for pos in relative_pos:
            new_x = pos[0] + square.position[0]
            new_y = pos[1] + square.position[1]
            if 0 <= new_x < self.size[0] and 0 <= new_y < self.size[1]:
                neigh = self.get_square((new_x, new_y))
                if neigh.is_visited == False:
                    neighbours.append(neigh)
        return neighbours

    def get_possible_moves(self, square):
        '''number of possible moves from the current square.'''
        return len(self.find_neighbours(square))

    def next_move(self):
        '''finds the next move'''
        #print 'current square: %s' % (str(self.current_square.position))
        neighbours = self.find_neighbours(self.current_square)
        possible_moves = [self.get_possible_moves(s) for s in neighbours]
        next_idx = possible_moves.index(min(possible_moves))
        next_square = neighbours[next_idx]
        # mark the next square as visited
        next_square.visit()
        self.unvisited -= 1
        self.current_square = next_square
        #print 'next square: %s' % (str(next_square.position))
        return next_square

    def tour(self):
        '''the knight tours through the board'''
        pos = [self.start_pos]
        while self.unvisited != 0 and self.next_move != None:
            pos.append(self.next_move().position)
        return pos

class Square():
    '''controls each square on the chess board.

    position: tuple -> position on board
    is_visited: bool -> whether the current square has been visited

    visit()'''

    def __init__(self, position):
        self.position = position
        self.is_visited = False

    def visit(self):
        '''the knight visits a square'''
        self.is_visited = True


class Draw():
    '''draws everything'''

    def __init__(self):
        self.board = Board(BOARD_SIZE, START_POS)
        self.points_x = range(self.board.size[0]) * self.board.size[1]
        self.points_y = [y for y in range(self.board.size[1])
                           for dummy in range(self.board.size[0])]
        self.draw_board()

    def draw_board(self):
        '''draws and empty board'''
        pt = plt.scatter(self.points_x, self.points_y, s=5)
        plt.ion()
        plt.xlim(-1, 8)
        plt.ylim(-1, 8)
        plt.axis('equal')
        plt.pause(.05)

    def draw_tour(self):
        '''tours through the board'''
        all_pos = self.board.tour()
        marker_style = dict(color='cornflowerblue', linestyle=':', marker='o',
                markersize=15, markerfacecoloralt='gray')
        for step in range(len(all_pos) - 1):
            x = [all_pos[step][0], all_pos[step+1][0]]
            y = [all_pos[step][1], all_pos[step+1][1]]
            plt.plot(x, y, **marker_style)
            plt.pause(.05)
        while True:
            plt.pause(1)



if __name__ == "__main__":
    draw_board = Draw()
    draw_board.draw_tour()

    
