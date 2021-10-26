

import random

from player import Player


def heuristic(board):
    # 0 is empty
    # 1 is player 1
    # 2 is player 2
    
    ...


def max_value(game, alpha, beta, d) -> tuple:
    if game.terminal() or d == 0:
        return (game.utility(game.player()), None)

    v = float("-inf")
    move = None
    for action in game.actions():
        v2, _ = min_value(game.result(action), alpha, beta, d - 1)
        v2 += heuristic(game)
        if v2 > v:
            v, move = v2, action
            alpha = max(alpha, v)
        if v >= beta:
            return (v, move)
    return (v, move)  # best move


def min_value(game, alpha, beta, d) -> tuple:  # (utility, move)
    if game.terminal() or d == 0:
        return (game.utility(game.otherplayer()), None)

    v = float("+inf")
    move = None
    for action in game.actions():
        v2, _ = max_value(game.result(action), alpha, beta, d - 1)
        v2 += heuristic(game.data)
        if v2 < v:
            v, move = v2, action
            beta = min(beta, v)
        if v <= alpha:
            return (v, move)
    return (v, move)  # worst move


def alpha_beta(game):
    _, move = max_value(game, float("-inf"), float("+inf"), d=5)
    return move
    

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        board.print()
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py

        return alpha_beta(board)
        # return random.sample(board.actions(),1)[0]
    def player(self):
        return self.playerN

    
    
