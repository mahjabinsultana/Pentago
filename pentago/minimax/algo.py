from copy import deepcopy
import pygame
from pentago.constants import WHITE, BLACK




#position হল কারেন্ট পজিশন, depth হল ট্রি কত ডেপথ পর্যন্ত ট্রাই করবো
#minmax একটা বোর্ড রিটার্ন করবে, moves.append[new_board] এইলাইনে বোর্ড এর সিচুয়েশন এসাইন হচ্ছে
def minimax(position,depth,max_player, game):
    if depth == 0 or position.winner()!= None:
        return position.evaluate(), position
    #যখন ট্রির ডেপথ ০ হয়ে গেসে তখন আমরা ইভাল্যুয়েট করবো, এখানে position.evaluate মানে হল 
# board.evaluate, তাহলে এই বোর্ডের কারেন্ট সিচুয়েশনে আমার red piece কত, white piece কত এটা
#কাউন্ড করে ইভ্যালুয়েশন করছে।
    
    
    #এখানে ট্রি এর প্রথম এ White চাললো, এরপরে রেড চালবে, তাহলে সবগুলা মুভ সিমুলেট করে হিসাব করবে AI 
  # তাই maxEval এবং minEval সিমুলেট
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_move(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            #প্রতিটা মুভ এর জন্য ইভালুয়েশন করতেসে, রিকার্সিভ কল
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_move(position, BLACK, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
        
        
        

def simulate_move(move,board,game):
    (row, col, grid_no, rotation) = move
    board.draw(row, col, game.turn)
    board.rotate(grid_no, rotation)
    return board

    
       
def get_all_move(board, color, game):
    moves = []
    valid_moves = board.get_valid_moves()
    for move in valid_moves:
        temp_board = deepcopy(board)
        new_board = simulate_move(move, temp_board, game)
        moves.append(new_board)
    return moves
"""""
def draw_moves(game, board):
    valid_moves = board.get_valid_moves()
    board.draw(game.win)
    pygame.draw.circle(game.win,(0,255,0),(piece.x,piece.y),50,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)

"""
            