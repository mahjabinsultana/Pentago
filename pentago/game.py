import pygame
from .board import Board
from .constants import WHITE, BLACK

class Game:
    def __init__(self, win, board):
        self.board = board
        self.turn = BLACK
        self.valid_moves = {}
        self.win = win
        self.move = False
        self.rotate = False

    def update(self):
        self.board.draw_cubes(self.win)
        pygame.display.update()
    """""
    def winner(self):
        return self.board.winner()
    """
    def change_turn(self):
        self.move = False
        self.rotate = False
        if self.turn==BLACK:
            pygame.display.set_caption('Your Turn')
            self.turn= WHITE
            
        else:
            pygame.display.set_caption('AI Turn')
            self.turn=BLACK
            


    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        pygame.display.set_caption('AI Turn')
        pygame.time.delay(5000)
        self.board = board
        self.change_turn()
    

    def place_marble(self, win, row, col):
        if self.move == False and self.rotate == False:
            if row >= 0 and row <= 5 and col >= 0 and col <= 5:
                self.board.draw(row,col, self.turn)
                self.board.draw_cubes(win)
                print("Selected row:", row)
                print("Selected col:", col)
                pygame.display.update()
                self.move = True
                if self.turn == BLACK:
                    self.board.b_left -=1
                elif self.turn == WHITE:
                    self.board.w_left -=1
        
    def rotate_quad(self, win, grid_no, rotation):
        if self.move and self.rotate == False:
            if grid_no != -1:
                print(grid_no, rotation)
                self.board.rotate(grid_no, rotation)
                self.board.draw_cubes(win)
                self.rotate = True
                pygame.display.update()
                return True
            
    