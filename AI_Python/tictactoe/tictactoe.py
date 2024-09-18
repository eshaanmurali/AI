"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    
    if even number of empties it is O turn
    
    else x turn
    """
    countEmpty = 0
    
    for row in board:
        for col in row:
            if col == EMPTY:
                countEmpty += 1
    if countEmpty % 2 == 0:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    empty spots are possible positions
    create a list
    when we reach an empty spot add the tuple to the list
    """
    actionsList = set()
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                actionsList.add((row, col))
    
    return actionsList




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    boardCopy = copy.deepcopy(board)
    row, col = action
    
    boardCopy[row][col] = player(board)
    return boardCopy
    

def rowWinner(board, player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
           return True
    
    return False
       

def colWinner(board, player):
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
              
    return False


def diagWinner(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if rowWinner(board, X) or colWinner(board, X) or diagWinner(board, X):
        return X
    
    if rowWinner(board, O) or colWinner(board, O) or diagWinner(board, O):
        return O
    
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    game is over when winner returns x or o
    game is over when there are no more spots
    """
    
    if winner(board) == X or winner(board) == O:
        return True
    
    if any(EMPTY in sublist for sublist in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0
    

def MAXVALUE(state):
    '''
    function MAX-VALUE(state):
        if TERMINAL(state):
            return UTILITY(state)
        v = -1000000 (-infinity)
        for action in ACTIONS(state)
            v = MAX(v, MIN-VALUE(RESULT(state, action)))
        return v
    '''
    
    if terminal(state):
        return utility(state)

    v = -1000000000
    for action in actions(state):
        v = max(v, MINVALUE(result(state, action)))
    return v

def MINVALUE(state):
    '''
    function MAX-VALUE(state):
        if TERMINAL(state):
            return UTILITY(state)
        v = 1000000 (infinity)
        for action in ACTIONS(state)
            v = MIN(v, MAX-VALUE(RESULT(state, action)))
        return v
    '''
     
    if terminal(state):
        return utility(state)

    v = 1000000000
    for action in actions(state):
        v = min(v, MAXVALUE(result(state, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    Minimax
    Given a state s:
        MAX (X) picks action a in ACTIONS(s) that produces higest value of MIN-VALUE(RESEULT(s, a))
        MIN (O) picks action a in ACTIONS(s) that produces smallest value of MAX-VALUE(RESEULT(s, a))   
    """
    
    if terminal(board):
        return None
    
    #Player X turn  
    if player(board) == X:
        for a in actions(board):
            if MAXVALUE(board) == MINVALUE(result(board, a)):
                return a
        
    #Player O turn
    else:
        for a in actions(board):
            if MINVALUE(board) == MAXVALUE(result(board, a)):
                return a
    
    
    
        
    