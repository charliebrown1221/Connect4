import numpy as np

def  create_board():
    board =np.zeros((6,7))
    return board


board = create_board()
game_over=False
turn=0 





while not game_over:
    if turn==0:
        selection =input("Player one Make your selection")
