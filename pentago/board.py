import pygame
import sys
from copy import deepcopy
import numpy as np
from .constants import BLACK, RED, ROWS, COLS, SQAURE_SIZE, DARKRED, WHITE, BORDERCOLOR
pygame.font.init()
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.b_left =18
        self.w_left = 18
        self.create_board()
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    # Function to rotate the board
    def rotate_board(self, board):
        return list(zip(*reversed(board)))

    
    def draw_cubes(self, win):
        border_thickness = 2

        # Calculate the position offset based on the board number 'i'
        offset_x = 190
        offset_y = 90

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (offset_x + row * SQAURE_SIZE, offset_y + col * SQAURE_SIZE, SQAURE_SIZE, SQAURE_SIZE))
            if row % 2 == 0:
                for col in range(1, ROWS, 2):
                    pygame.draw.rect(win, DARKRED, (offset_x + row * SQAURE_SIZE, offset_y + col * SQAURE_SIZE, SQAURE_SIZE, SQAURE_SIZE))
            else:
                for col in range(0, ROWS, 2):
                    pygame.draw.rect(win, DARKRED, (offset_x + row * SQAURE_SIZE, offset_y + col * SQAURE_SIZE, SQAURE_SIZE, SQAURE_SIZE))
        
        # Draw the border for the board
        pygame.draw.rect(win, BORDERCOLOR, (offset_x, offset_y, (ROWS//2) * SQAURE_SIZE, (ROWS//2) * SQAURE_SIZE), border_thickness)
        pygame.draw.rect(win, BORDERCOLOR, (offset_x+210, offset_y, (ROWS//2) * SQAURE_SIZE, (ROWS//2) * SQAURE_SIZE), border_thickness)
        pygame.draw.rect(win, BORDERCOLOR, (offset_x, offset_y+210, (ROWS//2) * SQAURE_SIZE, (ROWS//2) * SQAURE_SIZE), border_thickness)
        pygame.draw.rect(win, BORDERCOLOR, (offset_x+210, offset_y+210, (ROWS//2) * SQAURE_SIZE, (ROWS//2) * SQAURE_SIZE), border_thickness)        
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]==1:

                    # draw circle
                    x = 190+ (SQAURE_SIZE//2) + (SQAURE_SIZE//2)*(col*2) 
                    y= 90 + (SQAURE_SIZE//2) + (SQAURE_SIZE//2)*(row*2)

                    # x,y will be centre
                    # Draw the filled circle
                    pygame.draw.circle(win, WHITE, (x,y), 25)
                elif self.board[row][col]==-1:
                    # draw circle
                    x = 190+ (SQAURE_SIZE//2) + (SQAURE_SIZE//2)*(col*2) 
                    y= 90 + (SQAURE_SIZE//2) + (SQAURE_SIZE//2)*(row*2)

                    # x,y will be centre
                    # Draw the filled circle
                    pygame.draw.circle(win, BLACK, (x,y), 25)
        

    def draw_marbles(self, win):
        radius = 10
        for i in range(self.b_left):
            pygame.draw.circle(win, BLACK, (95, 45+radius+(i*30)), 10)
            pygame.display.update()
        
        for i in range(self.w_left):
            pygame.draw.circle(win, WHITE, (705, 45+radius+(i*30)), 10)
            pygame.display.update()
    

    def draw_rotatesym(self, win):
        
        font = pygame.font.SysFont("Segoe UI Symbol", 36)
        clock = font.render("↻", True, BLACK)
        text_rect = clock.get_rect()

        text_rect.center = (200, 70)
        win.blit(clock, text_rect)

        text_rect.center = (200, 520)
        win.blit(clock, text_rect)

        text_rect.center = (600, 70)
        win.blit(clock, text_rect)

        text_rect.center = (600, 520)
        win.blit(clock, text_rect)

        anticlock = font.render("↺", True, BLACK)
        text_rect = anticlock.get_rect()

        text_rect.center = (170, 110)
        win.blit(anticlock, text_rect)

        text_rect.center = (170, 490)
        win.blit(anticlock, text_rect)

        text_rect.center = (630, 110)
        win.blit(anticlock, text_rect)
        
        text_rect.center = (630, 490)
        win.blit(anticlock, text_rect)
    


    def construct_board():
        BOARD_SIZE = 6
        return np.array([[0] * BOARD_SIZE for _ in range(BOARD_SIZE)], int)

    def is_board_full(board):
        for x, line in enumerate(board, 0):
            for y, value in enumerate(line, 0):
                if value == 0:
                    return False
        return True
    
    def get_position_if_valid(board, x, y):
        try:
            r = range(0, 6)
            # If position is outside boundaries or on an already filled position.
            if x not in r or y not in r or board[x, y] != 0:
                return None

            # Return 2 dim array relative position (e.g (0, 0))
            return (x, y)
        except:
            return None
        
    def draw(self,selected_row,selected_col, turn):
        piece = self.board[selected_row][selected_col]
        if piece ==0:
            if turn == WHITE:
                self.board[selected_row][selected_col] = 1 # 1 means AI has given input
            elif turn == BLACK:
                self.board[selected_row][selected_col] = -1 # -1 means USER has given input
        
   

    def rotate_board(self, start_row, end_row, start_col, end_col, rotate):
        my_board = np.array(self.board)

    # Extract the portion of the matrix to rotate
        portion = my_board[start_row:end_row + 1, start_col:end_col + 1]

    # Rotate the portion clockwise or anticlockwise
        if rotate=="anticlockwise":
            rotated_portion = np.rot90(portion,1)
        elif rotate=="clockwise":
            rotated_portion = np.rot90(portion,3)

    # Replace the portion in the original matrix with the rotated portion
        my_board[start_row:end_row + 1, start_col:end_col + 1] = rotated_portion
        self.board = my_board.tolist()

        #return matrix


    def rotate(self,grid_no,rotation):
            if(grid_no==0):
                start_row = 0
                end_row = 2
                start_col = 0
                end_col = 2
            elif(grid_no==1):
                start_row = 0
                end_row = 2
                start_col = 3
                end_col = 5
            elif(grid_no==2):
                start_row = 3
                end_row = 5
                start_col = 0
                end_col = 2
            elif(grid_no==3):
                start_row = 3
                end_row = 5
                start_col = 3
                end_col = 5
            
            self.rotate_board(start_row,end_row,start_col,end_col,rotation)

    
    def get_valid_moves(self):
        moves = set()  # Initialize moves as a set
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    moves.add((row, col, 0, 'clockwise'))  # Add clockwise move
                    moves.add((row, col, 0, 'anticlockwise'))  # Add anticlockwise move
                    moves.add((row, col, 1, 'clockwise'))  # Add clockwise move
                    moves.add((row, col, 1, 'anticlockwise'))  # Add anticlockwise move
                    moves.add((row, col, 2, 'clockwise'))  # Add clockwise move
                    moves.add((row, col, 2, 'anticlockwise'))  # Add anticlockwise move
                    moves.add((row, col, 3, 'clockwise'))  # Add clockwise move
                    moves.add((row, col, 3, 'anticlockwise'))  # Add anticlockwise move
        return moves
       

    def winner(self): # check korbe row,column or diagonally same value ache kina, winner identify korbe.
        # Check horizontal
        for row in range(6):
            for col in range(2):
                if all(self.board[row][col+i] == 1 for i in range(5)):
                    return 1

        # Check vertical
        for col in range(6):
            for row in range(2):
                if all(self.board[row+i][col] == 1 for i in range(5)):
                    return 1

        # Check main diagonal
        for row in range(2):
            for col in range(2):
                if all(self.board[row+i][col+i] == 1 for i in range(5)):
                    return 1

        # Check anti-diagonal
        for row in range(2):
            for col in range(4, 6):
                if all(self.board[row+i][col-i] == 1 for i in range(5)):
                    return 1


        # Check horizontal
        for row in range(6):
            for col in range(2):
                if all(self.board[row][col+i] == -1 for i in range(5)):
                    return -1

        # Check vertical
        for col in range(6):
            for row in range(2):
                if all(self.board[row+i][col] == -1 for i in range(5)):
                    return -1

        # Check main diagonal
        for row in range(2):
            for col in range(2):
                if all(self.board[row+i][col+i] == -1 for i in range(5)):
                    return -1

        # Check anti-diagonal
        for row in range(2):
            for col in range(4, 6):
                if all(self.board[row+i][col-i] == -1 for i in range(5)):
                    return -1
        
        return 0
