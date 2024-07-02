import pygame
#pygame.font.init()
import sys
from pentago.constants import WIDTH, HEIGHT, BLACK, CREAM, WHITE, ROWS, SQAURE_SIZE
from pentago.board import Board
from pentago.game import Game
from pentago.minimax.algo import AlphaBeta, iterative_deepening, Genetic_Algorithm
FPS = 60
mode = 0
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


def game_over(winner): 
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont(None, 48)  # None uses the default font, 48 is the size

    if winner == -1:
        print("user won")
        screen = pygame.transform.scale(pygame.image.load('pentago/img/youwon.png'), (WIDTH,HEIGHT))
        WIN.blit(screen,(0,0))
        pygame.display.update()
    else:
        print("AI won")
        screen = pygame.transform.scale(pygame.image.load('pentago/img/aiwon.png'), (WIDTH,HEIGHT))
        WIN.blit(screen,(0,0))
        pygame.display.update()


    # Event loop to wait for mouse button click
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x>=710 and x<=769 and y>=52 and y<=85:
                    in_screen()    

def select_mode():
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        
        #WIN.fill(RED)
        screen = pygame.transform.scale(pygame.image.load('pentago\img\mode.png'), (WIDTH,HEIGHT))
        WIN.blit(screen,(0,0))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x,y) 
                if x>=710 and x<=769 and y>=52 and y<=85:
                    in_screen()
                if x>=214 and x<=593 and y>=245 and y<=310:
                    mode = 1
                    main_game(mode)
                if x>=214 and x<=593 and y>=332 and y<=397:
                    mode = 2
                    main_game(mode)
                if x>=214 and x<=593 and y>=421 and y<=485:
                    mode = 3
                    main_game(mode)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()    

def game_rules():
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        
        #WIN.fill(RED)
        screen = pygame.transform.scale(pygame.image.load('pentago\img\gamerules.png'), (WIDTH,HEIGHT))
        WIN.blit(screen,(0,0))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x,y) 
                if x>=710 and x<=769 and y>=52 and y<=85:
                    in_screen()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()      

def in_screen():
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        
        #WIN.fill(RED)
        screen = pygame.transform.scale(pygame.image.load('pentago\img\initial_screen.png'), (WIDTH,HEIGHT))
        WIN.blit(screen,(0,0))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x>=441 and x<=686 and y>=329 and y<=386:
                    select_mode()
                if x>=441 and x<=686 and y>=437 and y<=495:
                    game_rules()    
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
       
 
def main_game(mode):
    run = True
    clock = pygame.time.Clock()
    ## constant fps maintain kore game run korar jono. 
    ## pc'r speed er upor depend korbe na
    board = Board()
    print("board declared", board.board)
    #
    WIN.fill(CREAM)
    board.draw_cubes(WIN)
    pygame.display.update()
    board.draw_rotatesym(WIN)
    pygame.display.update()

    game = Game(WIN, board)
    print("initial board ", game.get_board().board)
    
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
           
           if mode == 1:
                # function call for mode 1 : Genetic algo
                pygame.display.set_caption('AI')
                new_board = Genetic_Algorithm(game.get_board(), WHITE, game)
                game.ai_move(new_board, mode)   
           if mode == 2:
                # function call for mode 2: minimax algo
                pygame.display.set_caption('AI')
                new_board = iterative_deepening(game.get_board(), 3, WHITE, game)
                print("original board ", board.board)
                print("new board ", new_board.board)
                game.ai_move(new_board, mode)
                print("win ", board.winner())

           if mode == 3:
                # function call for mode 3 : alpha beta pruning
                pygame.display.set_caption('AI')
                new_board = iterative_deepening(game.get_board(), 10, WHITE, game)
                game.ai_move(new_board, mode)
        else:
           pygame.display.set_caption('Your turn')
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
                   # board.get_valid_moves()
                game.update()
        
        #print("game update",game.get_board())
        #print("win ", board.winner())
        if game.board.winner()!= 0:
            pygame.time.delay(2000)
            print(game.board.winner())    
            game_over(game.board.winner())
            run=False
            

        

          
    pygame.quit()
    
in_screen()