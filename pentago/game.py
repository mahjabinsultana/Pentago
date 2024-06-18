import pygame
from .board import Board
from .constants import WHITE, BLACK

class Game:
    def __init__(self, win):
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw_cubes(self.win)
        pygame.display.update()
    """""
    def winner(self):
        return self.board.winner()
    """
    def change_turn(self):
        self.valid_moves = {}
        if self.turn==BLACK:
            self.turn= WHITE
            
        else:
            self.turn=BLACK
            


    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        pygame.display.set_caption('AI Turn')
        pygame.time.delay(5000)
        self.board = board
        self.change_turn()
    

    
