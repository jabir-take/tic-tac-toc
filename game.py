import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range (9)]
        self.currentWinner = None
        
    def board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_square(self):
        return " " in self.board
    def num_empty_square(self):
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        return False
        
            
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = "X"
    while game.empty_square:
        if letter == "O":
            square= o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            print(letter+f"makes a move to square{square}")
    
        
        
        
        
        
        
        
        
        
        
        
# moves = []
# for i,spot in enumerate(self.board):
#     if spot == " ":
#         moves.append(i)
# return moves
# f_l = []
# for j in range(3):
#     i_l = []
#     for i in range(j*3, (j+1)*3):
#         i_l.append(str(i+1))
#     f_l.append(i_l)
# print(f_l)
# for row in range(3):
#     print(f"|   "*4,)

