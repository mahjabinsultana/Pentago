import pygame
from pentago.constants import WIDTH,HEIGHT,SQUARE_SIZE,WHITE
from pentago.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pentago')

def select_row_col(x,y):
    col = -1
    if x>=60 and x<=140:
        col = 0
    elif x>=140 and x<220:
        col = 1
    elif x>=220 and x<300:
        col = 2
    elif x>=305 and x<385:
        col = 3
    if x>=385 and x<465:
        col = 4
    elif x>=465 and x<545:
        col = 5
    
    row = -1
    if y>=60 and y<=140:
        row = 0
    elif y>=140 and y<220:
        row = 1
    elif y>=220 and y<300:
        row = 2
    elif y>=305 and y<385:
        row = 3
    if y>=385 and y<465:
        row = 4
    elif y>=465 and y<545:
        row = 5
    
    return row,col

def select_grid_to_rotate(x,y):
    grid_no=-1
    rotate = ""
    if(x>=100 and x<=140 and y>=25 and y<=45) :
        grid_no = 0
        rotate = "anticlockwise"
    elif(x>=25 and x<=45 and y>=100 and y<=140) :
        grid_no = 0
        rotate = "clockwise"
    elif(x>=100 and x<=140 and y>=560 and y<=580) :
        grid_no = 2
        rotate = "clockwise"
    elif(x>=25 and x<=45 and y>=465 and y<=465+40) :
        grid_no = 2
        rotate = "anticlockwise"
    elif(x>=465 and x<=465+40 and y>=25 and y<=45) :
        grid_no = 1
        rotate = "clockwise"
    elif(x>=560 and x<=580 and y>=100 and y<=100+40) :
        grid_no = 1
        rotate = "anticlockwise"
    elif(x>=465 and x<=465+40 and y>=560 and y<=580) :
        grid_no = 3
        rotate = "anticlockwise"
    elif(x>=560 and x<=580 and y>=465 and y<=465+40) :
        grid_no = 3
        rotate = "clockwise"
    return grid_no,rotate

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        clock.tick(FPS)

        
        #pygame.draw.rect(WIN, WHITE, pygame.Rect(30, 30, 450, 450),  5)
        #pygame.display.update()
        board.draw_squares(WIN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse coordinates
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row,col = select_row_col(mouse_x,mouse_y)
                grid_no,rotation = select_grid_to_rotate(mouse_x,mouse_y)
                #selected_row = mouse_y // SQUARE_SIZE
                #selected_col = mouse_x // SQUARE_SIZE
                if row>=0 and row<=5 and col>=0 and col<=5 :
                    board.draw(WIN,row,col)
                    print("Selected row:", row)
                    print("Selected col:", col)
                elif grid_no!=-1:
                    print(grid_no,rotation)
                    board.rotate(grid_no,rotation)
                else:
                    print("Nothing selected.")

                    

                
                
                pygame.display.update()
        #board.draw(WIN)
        # ekane draw call korbona, korbo draw_squares,
        # finally draw function muche dibo
        

    pygame.quit()


main()