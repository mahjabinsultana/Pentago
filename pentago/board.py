import pygame
import numpy as np

from .constants import BLACK,ROWS,RED,COLS,SQUARE_SIZE,WHITE,GREY,BLUE
from .piece import Piece
import math

class Board:
    def __init__(self):
        self.board = []
        #self.selected_piece = None
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw_squares(self,win):
        

        win.fill(BLACK)
        pygame.draw.rect(win, WHITE, pygame.Rect(10, 10, 585, 585),  5)

        pygame.draw.line(win, WHITE, (300, 60), (300, 545), 8)
        pygame.draw.line(win, WHITE, (60, 300), (545, 300), 8)
        
        # grid 1
        for row in range(ROWS//2):
            
            for col in range(COLS//2):
                if (row+col)%2==1:   
                    pygame.draw.rect(win,RED,(row*SQUARE_SIZE+60,col*SQUARE_SIZE+60,SQUARE_SIZE,SQUARE_SIZE))
                else:
                    pygame.draw.rect(win,GREY,(row*SQUARE_SIZE+60,col*SQUARE_SIZE+60,SQUARE_SIZE,SQUARE_SIZE))
        # grid 2
        for row in range(ROWS//2):
            
            for col in range(COLS//2):
                if (row+col)%2==1:
                    pygame.draw.rect(win,GREY,(row*SQUARE_SIZE+305,col*SQUARE_SIZE+60,SQUARE_SIZE,SQUARE_SIZE))
                else:
                    pygame.draw.rect(win,RED,(row*SQUARE_SIZE+305,col*SQUARE_SIZE+60,SQUARE_SIZE,SQUARE_SIZE))
        # grid 3
        for row in range(ROWS//2):
            
            for col in range(COLS//2):
                if (row+col+1)%2==1:   
                    pygame.draw.rect(win,RED,(row*SQUARE_SIZE+60,col*SQUARE_SIZE+305,SQUARE_SIZE,SQUARE_SIZE))
                else:
                    pygame.draw.rect(win,GREY,(row*SQUARE_SIZE+60,col*SQUARE_SIZE+305,SQUARE_SIZE,SQUARE_SIZE))
        # grid 4
        for row in range(ROWS//2):
            
            for col in range(COLS//2):
                if (row+col+1)%2==1:
                    pygame.draw.rect(win,GREY,(row*SQUARE_SIZE+305,col*SQUARE_SIZE+305,SQUARE_SIZE,SQUARE_SIZE))
                else:
                    pygame.draw.rect(win,RED,(row*SQUARE_SIZE+305,col*SQUARE_SIZE+305,SQUARE_SIZE,SQUARE_SIZE))

        #done
        rect = pygame.Rect(100, 10+15, 40, 40)
        pygame.draw.arc(win, WHITE, rect, 0 ,math.pi , 3)
        pygame.draw.polygon(win, WHITE, [(90, 40), (110, 40), (100, 50)])
        #done
        rect = pygame.Rect(10+15, 100, 40, 40)
        pygame.draw.arc(win, WHITE, rect, math.pi/2 ,math.pi*3/2 , 3)
        pygame.draw.polygon(win, WHITE, [(40, 90), (40, 110), (50, 100)])

        #done
        rect = pygame.Rect(100, 595-15-40, 40, 40)
        pygame.draw.arc(win, WHITE, rect, math.pi ,0 , 3)
        pygame.draw.polygon(win, WHITE, [(90,565), (110, 565), (100, 555)])
        #done
        rect = pygame.Rect(25, 465, 40, 40)
        pygame.draw.arc(win, WHITE, rect, math.pi/2 ,math.pi*3/2 , 3)
        pygame.draw.polygon(win, WHITE, [(40, 495), (40, 515), (50, 505)])

        
        #done
        rect = pygame.Rect(465, 10+15, 40, 40)
        pygame.draw.arc(win, WHITE, rect, 0 ,math.pi , 3)
        pygame.draw.polygon(win, WHITE, [(495, 40), (515, 40), (505, 50)])

        #done
        rect = pygame.Rect(540, 100, 40, 40)
        pygame.draw.arc(win, WHITE, rect, math.pi*3/2 ,math.pi/2 , 3)
        pygame.draw.polygon(win, WHITE, [(565, 90), (565, 110), (555, 100)])

        #done
        rect = pygame.Rect(465, 595-15-40, 40, 40)
        pygame.draw.arc(win, WHITE, rect, math.pi ,0 , 3)
        pygame.draw.polygon(win, WHITE, [(455+40,565), (475+40, 565), (465+40, 555)])

         #done
        rect = pygame.Rect(540, 465, 40, 40)
        pygame.draw.arc(win, WHITE, rect,math.pi*3/2 ,math.pi/2 , 3)
        pygame.draw.polygon(win, WHITE, [(565, 455+40), (565, 475+40), (555, 465+40)])


        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]==1:
                    # draw circle
                    x = 60 
                    y=60
                    if row>=2:
                        y+=5
                    if col>=2:
                        x+=5
                    x = x + 80*col + 40
                    y = y + 80*row + 40

                    # x,y will be centre
                    # Draw the filled circle
                    pygame.draw.circle(win, BLUE, (x,y), 25)
        #done

        
    # board te piece boshaice, eta lagbena
    #def create_board(self):
     #   for row in range(ROWS):
      #      self.board.append([])
       #     for col in range(COLS):
        #        if col%2 == ((row+1)%2):
         #           if row < 3:
          #              self.board[row].append(Piece(row,col,WHITE))
           #         elif row > 4:
            #            self.board[row].append(Piece(row,col,RED))
             #       else:
              #          self.board[row].append(0)
               # else:
                #    self.board[row].append(0)
    
                
    # etao lagbena
    def draw(self,win,selected_row,selected_col):
        self.draw_squares(win)
        #for row in range(ROWS):
            #for col in range(COLS):
        piece = self.board[selected_row][selected_col]
        if piece ==0:
        #    piece.draw(win)
            self.board[selected_row][selected_col] = 1 # 1 means user has given input



        #self.board.append(Piece(selected_row,selected_col,WHITE))
        print(self.board)


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
        print("ROTATED BOARD ",self.board)

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