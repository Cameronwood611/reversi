

import random

from player import Player


def max_value(game, alpha, beta) -> tuple:
    if game.terminal():
        return (game.utility(), None)

    v = float("-inf")
    move = None
    for action in game.actions():
        v2, _ = min_value(game.place_move(game.player(), action), alpha, beta)
        if v2 > v:
            v, move = v2, action
            alpha = max(alpha, v)
        if v >= beta:
            return (v, move)
    return (v, move)  # best move


def min_value(game, alpha, beta) -> tuple:  # (utility, move)
    if game.terminal():
        return (game.utility(), None)

    v = float("+inf")
    move = None
    for action in game.actions():
        v2, _ = max_value(game.place_move(game.otherplayer(), action), alpha, beta)
        if v2 < v:
            v = v2
            move = action
            beta = min(beta, v)
        if v <= alpha:
            return (v, move)
    return (v, move)  # worst move


def alpha_beta(game):
    _, move = max_value(game, float("-inf"), float("+inf"))
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

        alpha_beta(board)
        return random.sample(board.actions(),1)[0]
    def player(self):
        return self.playerN

    
    
