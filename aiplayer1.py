

import random

from player import Player

def coin_diff(game, player, opponent):
    """Measures the difference in the number of pieces on board."""
    board = game.data

    coinsPlayer = 0
    coinsOpponent = 0
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                coinsPlayer += 1
            elif board[i][j] == opponent:
                coinsOpponent += 1

    if (coinsPlayer+coinsOpponent) != 0:
        return ((coinsPlayer-coinsOpponent)/(coinsPlayer+coinsOpponent))*100
    else:
        return 0

def choice_diff(game, player, opponent):
    """Measures the difference in the choice_diff in terms of available choices."""
    return 0

def corner_diff(game, player, opponent):
    """Measures the difference in the number of corners captured."""
    board = game.data

    cornersPlayer = 0
    cornersOpponent = 0

    for corner in [(0,0), (0,7), (7,0), (7,7)]:
        r,c = corner
        if board[r][c] == player:
            cornersPlayer += 1
        elif board[r][c] == opponent:
            cornersOpponent += 1

    if (cornersPlayer+cornersOpponent) != 0:
        return ((cornersPlayer-cornersOpponent)/(cornersPlayer+cornersOpponent))*100
    else:
        return 0

def heuristic(game, player, opponent):
    return 0.15 * coin_diff(game, player, opponent) + 0.15 * choice_diff(game, player, opponent) + 0.7 * corner_diff(game, player, opponent)


def max_value(game, alpha, beta, d) -> tuple:
    if game.terminal():
        return (game.utility(game.player()), None)
    if d == 0:
        score = heuristic(game, game.player(), game.otherplayer())
        return (score, None)

    v = float("-inf")
    move = None
    for action in game.actions():
        v2, _ = min_value(game.result(action), alpha, beta, d - 1)
        if v2 > v:
            v, move = v2, action
            alpha = max(alpha, v)
        if v >= beta:
            return (v, move)
    return (v, move)  # best move


def min_value(game, alpha, beta, d) -> tuple:  # (utility, move)
    if game.terminal():
        return (game.utility(game.otherplayer()), None)
    if d == 0:
        score = heuristic(game, game.otherplayer(), game.player())
        return (score, None)
    
    v = float("+inf")
    move = None
    for action in game.actions():
        v2, _ = max_value(game.result(action), alpha, beta, d - 1)
        if v2 < v:
            v, move = v2, action
            beta = min(beta, v)
        if v <= alpha:
            return (v, move)
    return (v, move)  # worst move


def alpha_beta(game):
    _, move = max_value(game, float("-inf"), float("+inf"), d=5)
    return move
    

class AIPlayer1(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        board.print()
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py

        return alpha_beta(board)
    def player(self):
        return self.playerN

    
    
