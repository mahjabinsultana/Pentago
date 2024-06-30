from copy import deepcopy
import pygame
from pentago.constants import WHITE, BLACK

transposition_table = {}

def minimax(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
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
        moves = sorted(moves, key=lambda move: evaluate(move), reverse=True)  # Move ordering
        for move in moves:
            evaluation = minimax(move, depth-1, False, game, alpha, beta)[0]
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
            evaluation = minimax(move, depth-1, True, game, alpha, beta)[0]
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        transposition_table[pos_key] = (minEval, best_move)
        return minEval, best_move

# Implementing Iterative Deepening
def iterative_deepening(position, max_depth, max_player, game):
    best_move = None
    for depth in range(1, max_depth + 1):
        _, best_move = minimax(position, depth, max_player, game)
    return best_move


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
    if check_win(board, 1) and check_win(board, -1):
        return 10
    if check_win(board, 1):
        return 5
    if check_win(board, -1):
        return -5
    if is_board_full(board):
        return 0
    # Further evaluation logic for intermediate states
    score = 0
    if check_4_in_a_row(board, 1):
        score += 3
    if check_4_in_a_row(board, -1):
        score -= 3
    if check_3_in_a_row(board, 1):
        score += 1
    if check_3_in_a_row(board, -1):
        score -= 1
    return score

def check_win(board, player):
    # Check rows, columns and diagonals for a win
    board = board.board
    for row in range(len(board)):
        for col in range(len(board[row]) - 4 + 1):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    for col in range(len(board[0])):
        for row in range(len(board) - 4 + 1):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(len(board) - 4 + 1):
        for col in range(len(board[row]) - 4 + 1):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                return True

    return False

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

    return count > 0

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

    return count > 0

