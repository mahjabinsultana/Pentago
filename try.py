import pygame
import sys

# Define your constants
ROWS = 8
SQUARE_SIZE = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARKRED = (139, 0, 0)
border_thickness = 2
# Function to rotate the board
def rotate_board(board):
    return [[row[i] for row in reversed(board)] for i in range(len(board[0]))]

# Function to draw the board
def draw_board(win, i, board):
    border_thickness = 2

    # Calculate the position offset based on the board number 'i'
    offset_x = (i % 2) * (ROWS * SQUARE_SIZE + border_thickness)
    offset_y = (i // 2) * (ROWS * SQUARE_SIZE + border_thickness)

    surface = pygame.Surface((ROWS * SQUARE_SIZE, ROWS * SQUARE_SIZE))
    surface.fill(BLACK)

    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(surface, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        if row % 2 == 0:
            for col in range(1, ROWS, 2):
                pygame.draw.rect(surface, DARKRED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        else:
            for col in range(0, ROWS, 2):
                pygame.draw.rect(surface, DARKRED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Draw the border for the board
    pygame.draw.rect(surface, WHITE, (0, 0, ROWS * SQUARE_SIZE, ROWS * SQUARE_SIZE), border_thickness)

    win.blit(surface, (offset_x, offset_y))

# Initialize pygame
pygame.init()
win = pygame.display.set_mode((2 * (ROWS * SQUARE_SIZE + border_thickness), 2 * (ROWS * SQUARE_SIZE + border_thickness)))
clock = pygame.time.Clock()

# Define the initial boards
boards = [[0 for _ in range(ROWS)] for _ in range(4)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the boundaries of any board
            mouse_pos = pygame.mouse.get_pos()
            for i in range(4):
                offset_x = (i % 2) * (ROWS * SQUARE_SIZE + border_thickness)
                offset_y = (i // 2) * (ROWS * SQUARE_SIZE + border_thickness)
                if offset_x <= mouse_pos[0] < offset_x + ROWS * SQUARE_SIZE and offset_y <= mouse_pos[1] < offset_y + ROWS * SQUARE_SIZE:
                    # Rotate the board when clicked
                    boards[i] = rotate_board(boards[i])

    # Draw the boards
    win.fill(BLACK)
    for i, board in enumerate(boards):
        draw_board(win, i, board)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
