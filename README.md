# adversarial-search-algorithms

Summary:


boardprint(): prints the board in a readable format
winner(board,player): checks if a player has won
draw(board): checks if the board is fully drawn
minimax(board, depth, maximizing): AI decision-making algorithm
alphaBeta(board, depth, alpha beta, maximizing): Ai decision-making using alpha-beta pruning
bestMove(): finds best move for AI
playGame(): main game loop handling turns

Minimax code explanation:



def boardPrint():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

This function prints the board in a readable format
It splits the 1D list into three rows (boards[i:i+3]
Example output
| O | X | O |
| X | O | X |
| O | X | O |


def winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


This function checks if a player has won
Win_conditions lists all possible winning combinations
any(all(...)) ensures that if any condition is met, the function returns true

Example:
board = ['X', 'X', 'X', ' ', 'O', 'O', ' ', ' ', ' ']
winner(board, 'X')  # Returns True (Row win)



def draw(board):
    return ' ' not in board

Checks if the game is a draw by checking for empty spaces
If no  ‘  ’ are available then the game is a draw

Example:
board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X']
draw(board)  # Returns True (No spaces left)


def minimax(board, depth, maximizing):
    if winner(board, ai):
        return 10 - depth
    if winner(board, player):
        return depth - 10
    if draw(board):
        return 0

This is the core AI function
It recursively evaluates all possible moves
If AI wins-> positive score (10 - depth)
If player wins-> negative score(depth - 10)
If draw-> 0


if maximizing:
    maxEval = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            maxEval = minimax(board, depth + 1, False)
            board[i] = ' '
            maxEval = max(maxEval, maxEval)
    return maxEval


Minimax for AI maximizing
AI wants to maximize its score
It places ‘x’ in an empty spot, calls minimax() for the player’s move, undoes the move, and finds the maximum possible score



else:
    minEval = math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            maxEval = minimax(board, depth + 1, True)
            board[i] = ' '
            minEval = min(minEval, maxEval)
    return minEval


Minimax for player (minimizing)
The player tries to minimize AI’s score
Places ‘o’, calls minimax() for ai’s move, undoes the move then finds the minimum score


def bestMove():
    bestValue = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            moveValue = minimax(board, 0, False)
            board[i] = ' '
            if moveValue > bestValue:
                bestValue = moveValue
                move = i
    return move

Ai selects the best move by running minimax() on all available spots
The best move is stored in move

Example:
board = ['X', 'O', 'X', 'O', 'X', ' ', ' ', 'O', ' ']
print(bestMove())  # AI picks the best move

def playGame():
    while True:
        boardPrint()
        if winner(board, ai):
            print("AI wins!")
            break
        if winner(board, player):
            print("Player wins!")
            break
        if draw(board):
            print("It's a draw!")
            break

Main game loop
Prints board
Ensures move is valid


Alpha beta pruning:

def alphaBeta(board, depth, alpha, beta, maximizing):
    if winner(board, ai):
        return 10 - depth
    if winner(board, player):
        return depth - 10
    if draw(board):
        return 0

Same as minimax
Checks if ai wins or if player wins or if game is a draw

if maximizing:
    maxEval = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            eval = alphaBeta(board, depth + 1, alpha, beta, False)
            board[i] = ' '
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
    return maxEval

Same as minimax
Places ‘x’ in an empty position and calls alphaBeta() recursivly
Updates alpha (best value AI can guarantee)
Breaks early if beta<=alpha i.e. pruning, opponent will not allow this move




else:
    minEval = math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            eval = alphaBeta(board, depth + 1, alpha, beta, True)
            board[i] = ' '
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
    return minEval

Player tries to minimize the score
Places ’o’, calls alphaBeta() recursivly
Updates beta (best value the player can gaurantee)
Breaks early if beta<= alpha i.e. pruning

def bestMove():
    bestValue = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            moveValue = alphaBeta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if moveValue > bestValue:
                bestValue = moveValue
                move = i
    return move

Same as minimax
Tries all empty positions uses alphaBeta() to calculate the best move
Picks the move with the highest score

Key improvements over minimax:

Alpha-beta pruning means faster by eliminating unnecessary moves
Ai will always pick the best move meaning unbeatable AI
Depth factor meaning AI prioritizes faster wins and delayed losses
