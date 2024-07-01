from copy import deepcopy
import pygame
from pentago.constants import WHITE, BLACK
#from pentago.game import Game
#from pentago.board import Board
import random
import copy

#################  Iterative Deepening, Alpha Beta, Transposition Table implementation started

transposition_table = {}

def AlphaBeta(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    pos_key = tuple(map(tuple, position.board))  # Hashable board representation
    if pos_key in transposition_table:
        return transposition_table[pos_key]

    if depth == 0 or position.winner() != 0:
        eval_score = evaluate(position)
        transposition_table[pos_key] = (eval_score, position)
        return eval_score, position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        moves = get_all_move(position, WHITE, game)
        #print(moves)
        moves = sorted(moves, key=lambda move: evaluate(move), reverse=True)  # Move ordering
        for move in moves:
            evaluation = AlphaBeta(move, depth-1, False, game, alpha, beta)[0]
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        transposition_table[pos_key] = (maxEval, best_move)
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        moves = get_all_move(position, BLACK, game)
        moves = sorted(moves, key=lambda move: evaluate(move))  # Move ordering
        for move in moves:
            evaluation = AlphaBeta(move, depth-1, True, game, alpha, beta)[0]
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        transposition_table[pos_key] = (minEval, best_move)
        return minEval, best_move

def iterative_deepening(position, max_depth, max_player, game):
    best_move = None
    for depth in range(1, max_depth + 1):
        _, best_move = AlphaBeta(position, depth, max_player, game)
    return best_move

#################  Iterative Deepening, Alpha Beta, Transposition Table implementation ended




#################  Minimax Algorithm implementation started

def minimax(position, depth, max_player, game):
    ##print("came to minimax")
    if depth == 0 or position.winner() != 0:
        ##if(position.winner()!=0):
        ##   print("winner is ", position.winner())
        ##print("minimax ", position.board)
        return evaluate(position), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        ##print("came")
        for move in get_all_move(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            
        ##print("maxeval", best_move.board)
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_move(position, BLACK, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            
        ##print("mineval", best_move.board)
        return minEval, best_move
    
#################  Minimax Algorithm implementation ended






################# Genetic Algorithm implementation started

def Genetic_Algorithm(board, color , game):
    print("GENETIC ALGORITHM CALLED")

    # Constants for Genetic Algorithm
    POPULATION_SIZE = 20
    MUTATION_RATE = 0.1
    NUM_GENERATIONS = 100

    # Fitness function to evaluate the board
    def fitness(board):
        return evaluate(board)

    # Create initial population of moves
    def create_population(board,game):
        return get_all_move(board, color ,game)

    # Select the best moves
    def select_population(population):
        sorted_population = sorted(population, key=lambda move: fitness(move), reverse=True)
        return sorted_population[:POPULATION_SIZE // 2]

    # Crossover to combine two moves
    def crossover(parent1, parent2):
        # In this context, crossover isn't very meaningful because moves are single actions,
        # so we'll just return one of the parents randomly
        return random.choice([parent1, parent2])

    # Mutation to introduce variations
    def mutate(move,game,population):
        if random.random() < MUTATION_RATE:
            return random.choice(population)
        return move

    
    # Genetic Algorithm to find the best move
    population = create_population(board,game)
    
    for _ in range(NUM_GENERATIONS):
        selected_population = select_population(population)
        #print("selcted pupulationnnnnnnnnnn")
        new_population = []
        
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)
            child = crossover(parent1, parent2)
            #print("crossoverrrrrrrrrrrrr")
            child = mutate(child,game,population)
            #print("mutatedddddddddddd")
            new_population.append(child)
        
        updated_population = new_population
    
    best_move = max(updated_population, key=lambda move: fitness(move))
    print("Best move of genetic algorithm")
    print(best_move)
    return best_move
#################  Genetic Algorithm implementation ended


def simulate_move(move, board, game):
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


def evaluate(board):
    #if check_win(board, 1) and check_win(board, -1):
    #    return 10
    if check_win(board)==1:
        return 1000
    if check_win(board)==-1:
        return -1000
    if is_board_full(board):
        return 0
    # Further evaluation logic for intermediate states
    score = 0
    score = 0
    score += check_4_in_a_row(board, 1) * 50
    score -= check_4_in_a_row(board, -1) * 50
    score += check_3_in_a_row(board, 1) * 10
    score -= check_3_in_a_row(board, -1) * 10

    return score

def check_win(board):
        board = board.board
        for row in range(6):
            for col in range(2):
                if all(board[row][col+i] == 1 for i in range(5)):
                    return 1

        # Check vertical
        for col in range(6):
            for row in range(2):
                if all(board[row+i][col] == 1 for i in range(5)):
                    return 1

        # Check main diagonal
        for row in range(2):
            for col in range(2):
                if all(board[row+i][col+i] == 1 for i in range(5)):
                    return 1

        # Check anti-diagonal
        for row in range(2):
            for col in range(4, 6):
                if all(board[row+i][col-i] == 1 for i in range(5)):
                    return 1


        # Check horizontal
        for row in range(6):
            for col in range(2):
                if all(board[row][col+i] == -1 for i in range(5)):
                    return -1

        # Check vertical
        for col in range(6):
            for row in range(2):
                if all(board[row+i][col] == -1 for i in range(5)):
                    return -1

        # Check main diagonal
        for row in range(2):
            for col in range(2):
                if all(board[row+i][col+i] == -1 for i in range(5)):
                    return -1

        # Check anti-diagonal
        for row in range(2):
            for col in range(4, 6):
                if all(board[row+i][col-i] == -1 for i in range(5)):
                    return -1
        
        return 0
def is_board_full(board):
    board = board.board
    return all(cell != 0 for row in board for cell in row)

def check_4_in_a_row(board, player):
    board = board.board
    # Similar to check_win but returns the count of 4 in a row occurrences
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 4 + 1):
            if all(board[row][col + i] == player for i in range(4)):
                count += 1

    for col in range(len(board[0])):
        for row in range(len(board) - 4 + 1):
            if all(board[row + i][col] == player for i in range(4)):
                count += 1

    for row in range(len(board) - 4 + 1):
        for col in range(len(board[row]) - 4 + 1):
            if all(board[row + i][col + i] == player for i in range(4)):
                count += 1
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                count += 1

    return count

def check_3_in_a_row(board, player):
    board = board.board
    # Similar to check_4_in_a_row but for 3 in a row occurrences
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 3 + 1):
            if all(board[row][col + i] == player for i in range(3)):
                count += 1

    for col in range(len(board[0])):
        for row in range(len(board) - 3 + 1):
            if all(board[row + i][col] == player for i in range(3)):
                count += 1

    for row in range(len(board) - 3 + 1):
        for col in range(len(board[row]) - 3 + 1):
            if all(board[row + i][col + i] == player for i in range(3)):
                count += 1
            if all(board[row + 2 - i][col + i] == player for i in range(3)):
                count += 1

    return count

