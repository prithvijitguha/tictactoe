"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    """
    xcount = 0 
    ocount = 0

    #total x's and o's on board
    for i in board: 
        for j in i: 
            if j == X:
                xcount += 1 
            elif j == O:
                ocount += 1
        

  
    if xcount > ocount:
        return O
    elif ocount > xcount: 
        return X 
    #default x goes first
    elif xcount == ocount: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
   
    actionlist = set() 

    for i in range(3):
        for j in range(3): 
            if board[i][j] == EMPTY:
                actionlist.add((i,j))      
    return actionlist

   

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    """

    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    else:
        copyboard = copy.deepcopy(board)
        copyboard[action[0]][action[1]] = player(board)


    return copyboard
    
    """
    if board[i][j] == EMPTY:
        copyboard = copy.deepcopy(board)
        copyboard[i][j] = player(board)
    

    else: 
        raise Exception
    return copyboard
    """
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        for j in range(3):
            #diagonal winner
            if board[0][0] == board[1][1] == board[2][2] != EMPTY:
                return board[0][0]
            elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
                return board[0][2]
            #vertical winner 
            elif board[0][j] == board[1][j] == board[2][j] != EMPTY:
                return board[i][j]
            #horizontal winner
            elif board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return board[i][0]



    
 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #winner is present return true 
    if winner(board) != EMPTY: 
        return True
    #if no winner and no actions left, game over
    elif winner(board) == None and actions(board) == set():
        return True
    
    else: 
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1 
        elif winner(board) == "O":
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if computer is X
    if player(board) == X:
        #Take center of board
        if len(actions(board)) == 9:
            bestmoves = [(1,1), (0,0), (0,2), (2,0), (2,2)]
            return random.choice(bestmoves)
        else: 
            #goal is to maximize own score 
            v = -math.inf
            for action in actions(board):
                k = minvalue(result(board, action))
                if k > v: 
                    v = k 
                    best = action
  
            return best
    
    #if computer is O
    else: 
        #Take Center of board if empty
        if len(actions(board)) == 8 and board[1][1] == EMPTY:
            return (1,1)
        else:
            v = math.inf
            for action in actions(board):
                k = maxvalue(result(board, action))
                if k < v:
                    v = k
                    best = action
                    
            return best
            




def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v 

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
        
    return v   
    