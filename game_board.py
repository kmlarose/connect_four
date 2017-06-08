import os


class GameBoard:
    def __init__(self):
        self.cells = [(row, column) for row in range(6, 0, -1) for column in range(1, 8)]
        self.x_cells = []
        self.o_cells = []

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Connect Four!')
        print(' _'*7)
        tile = '|{}'
        for idx, cell in enumerate(self.cells):
            if idx in [6, 13, 20, 27, 34, 41]:
                if cell in self.x_cells:
                    print(tile.format('x|'))
                elif cell in self.o_cells:
                    print(tile.format('o|'))
                else:
                    print(tile.format('_|'))
            else:
                if cell in self.x_cells:
                    print(tile.format('x'), end='')
                elif cell in self.o_cells:
                    print(tile.format('o'), end='')
                else:
                    print(tile.format('_'), end='')
        print('='*15)
        for num in range(6):
            print(' {}'.format(num+1), end='')
        print(' 7')
