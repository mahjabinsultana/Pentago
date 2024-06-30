import pygame
#pygame.font.init()
import sys
from pentago.constants import WIDTH, HEIGHT, BLACK, CREAM, WHITE, ROWS, SQAURE_SIZE
from pentago.board import Board
from pentago.game import Game
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pentago')
# Define the initial boards
boards = [[0 for _ in range(ROWS)] for _ in range(4)]


def select_row_col(x,y):
    col = -1
    if x>=190 and x<=190+SQAURE_SIZE:
        col = 0
    elif x>190+SQAURE_SIZE and x<=190+SQAURE_SIZE*2:
        col = 1
    elif x>190+SQAURE_SIZE*2 and x<=190+SQAURE_SIZE*3:
        col = 2
    elif x>190+SQAURE_SIZE*3 and x<=190+SQAURE_SIZE*4:
        col = 3
    if x>=190+SQAURE_SIZE*4 and x<=190+SQAURE_SIZE*5:
        col = 4
    elif x>190+SQAURE_SIZE*5 and x<190+SQAURE_SIZE*6:
        col = 5
    
    row = -1
    if y>90 and y<90+SQAURE_SIZE*1:
        row = 0
    elif y>90+SQAURE_SIZE*1 and y<=90+SQAURE_SIZE*2:
        row = 1
    elif y>90+SQAURE_SIZE*2 and y<=90+SQAURE_SIZE*3:
        row = 2
    elif y>90+SQAURE_SIZE*3 and y<=90+SQAURE_SIZE*4:
        row = 3
    if y>90+SQAURE_SIZE*4 and y<=90+SQAURE_SIZE*5:
        row = 4
    elif y>90+SQAURE_SIZE*5 and y<=90+SQAURE_SIZE*6:
        row = 5
    
    return row,col

def select_grid_to_rotate(x,y):
    grid_no=-1
    rotate = ""
    if(x>=190 and x<=210 and y>=64 and y<=84) :
        grid_no = 0
        rotate = "clockwise"
    elif(x>=160 and x<=180 and y>=104 and y<=124) :
        grid_no = 0
        rotate = "anticlockwise"
    elif(x>=160 and x<=180 and y>=485 and y<=505) :
        grid_no = 2
        rotate = "anticlockwise"
    elif(x>=190 and x<=210 and y>=516 and y<=536) :
        grid_no = 2
        rotate = "clockwise"
    elif(x>=590 and x<=610 and y>=64 and y<=84) :
        grid_no = 1
        rotate = "clockwise"
    elif(x>=620 and x<=640 and y>=104 and y<=124) :
        grid_no = 1
        rotate = "anticlockwise"
    elif(x>=590 and x<=610 and y>=516 and y<=536) :
        grid_no = 3
        rotate = "clockwise"
    elif(x>=620 and x<=640 and y>=485 and y<=505) :
        grid_no = 3
        rotate = "anticlockwise"
    return grid_no,rotate


def game_over(winner): # when game is over it is called, winner name will showed in the display
    """""
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        WIN.blit(CREAM, (0, 0))
        
        pygame.draw.rect(WIN,(116, 116, 116), (0, 400, WIDTH+200, 100))
        
        if(winner == 1):
            livees_label = main_font.render(f"YOU WIN", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+150, 400+20))
        else:
            livees_label = main_font.render(f"YOU LOSE", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+130, 400+20))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    """
    # Create a font object
    main_font = pygame.font.SysFont("comicsans", 50)
    if(winner == 1):
        message = "You won"
    elif(winner==-1):
       message = "AI won"
    message_surface = main_font.render(message, True, WHITE)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the window
        WIN.fill((0, 0, 0))

        # Blit the message onto the window
        WIN.blit(message_surface, (300, 300))

        # Update the display
        pygame.display.update()

    

    
    



def main():
    run = True
    clock = pygame.time.Clock()
    ## constant fps maintain kore game run korar jono. 
    ## pc'r speed er upor depend korbe na
    board = Board()

    #
    WIN.fill(CREAM)
    board.draw_cubes(WIN)
    pygame.display.update()
    board.draw_rotatesym(WIN)
    pygame.display.update()

    game = Game(WIN, board)
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
           pygame.display.set_caption('AI')
           #value, new_board = minimax(game.get_board(), 3, WHITE, game)
           #game.ai_move(new_board)
           #print(value)
        else:
           pygame.display.set_caption('Your turn')
        
        if board.winner()!= 0:
            print(board.winner())
            
            game_over(board.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                row, col = select_row_col(x,y)
                grid_no, rotation = select_grid_to_rotate(x, y)
                if not game.move:
                    game.place_marble(WIN, row, col)
                if game.move and not game.rotate:
                    game.rotate_quad(WIN, grid_no, rotation)
                if game.move and game.rotate:
                    game.change_turn()
                board.get_valid_moves()
                
                
                

                
        game.update()
                    
    pygame.quit()
    
main()