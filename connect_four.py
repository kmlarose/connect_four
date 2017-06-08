from game_board import GameBoard


board = GameBoard()
board.draw_board()

player_x_turn = True
if player_x_turn:
    print('Your turn...')
    drop_row = int(input('Which row will you drop a chip into?: '))
    board.x_cells.append((1, drop_row))
board.draw_board()
