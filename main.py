import pygame
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
    board.draw_marbles(WIN)
    pygame.display.update()
    board.draw_rotatesym(WIN)
    pygame.display.update()

    game = Game(WIN)

    flag1= 0
    flag2 = 0
    while run:
        clock.tick(FPS)

        if game.turn == BLACK: #black mane ai move dibe
            game.ai_move(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if game.turn == WHITE: #white mane user move dibe. white hoile mouse click check
                if not flag1 and not flag2:
                    pygame.display.set_caption('Place a marble')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        row, col = select_row_col(x,y)
                        if row >= 0 and row <= 5 and col >= 0 and col <= 5:
                            board.draw(WIN,row,col)
                            print("Selected row:", row)
                            print("Selected col:", col)
                            pygame.display.update()
                            flag1 = 1
                            print("Flag1 : ", flag1)
            
                elif flag1 and not flag2:
                    pygame.display.set_caption('Rotate a quadrant')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        print("x: ", x)
                        print("y: ", y)
                        grid_no, rotation = select_grid_to_rotate(x, y)
                        if grid_no != -1:
                            print(grid_no, rotation)
                            board.rotate(grid_no, rotation)
                            board.draw_cubes(WIN)
                            flag2 = 1
                            pygame.display.update()

                elif flag1 and flag2:
                    flag1 = 0
                    flag2 = 0
                    game.change_turn()
                    continue

            else:
                continue
                
                

                
        game.update()
                    
    pygame.quit()
    
main()