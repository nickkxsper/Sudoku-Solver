import time
counter = 0

def print_board(board):
    '''
    Prints board in traditional format seperated by spaces
    
    Params:
        board: 2d Array (Sudoku Board) 
    

    '''
    for row in board:
        row_print = ''
        for value in row:
            row_print += str(value) + ' '
        print(row_print, flush = True)

## Helper Functions

def find_zero(board):
    '''
    Finds first zero in board starting at top left and navigating left to right by row
    
    params:
        board (2D Array): Sudoku Board
        
    returns:
        list of indices where the first 0 was found
        
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i,j]

def column(matrix, i):
    '''
    params:
        matrix (2D Array) 
        i (int): Column Number
        
    returns:
        list of column i of the matrix
    
    '''
    return [row[i] for row in matrix]

def valid(board, row, col, value):
    '''
    Checks 3x3 Region, Rows, and Columns for Duplicate Elements
    
    params:
        board (2D Array): Sudoku Board
        row(int): Row Index to Check
        col(int): Column Index to Check
        value(int): Value to check at board[row][col]
    returns:
        bool
    
    '''
    
    # Check 3x3 Box
    #Get box coords

    x_box = col // 3
    y_box = row // 3
    
    # check if element at box equals the value and the index is the same

    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box * 3, x_box*3 + 3):
            if board[i][j] == value and [i,j] != [row,col]:
                return False

    # check if value is in row or column of the checked cell
    
    if value in board[row] or value in column(board, col):
        return False
    else:
        return True

def solve(board):
    '''
    Uses recursive backtracking with helper functions defined above
    to solve a 9x9 Sudoku Board
    
    params:
        board(2D Array) : Sudoku Board
    
    '''
    # Base Case: If there are no more zeroes, we are done, return the board
    # Otherwise, check first empty using integers between 1 and 9
    # If none work, set cell equal to 0 and return False to continue backtracking
    global counter
    
    first_empty = find_zero(board)

    if not first_empty:
        return board
        print(f'Solved in {count} counts')
    else:
        row, column = first_empty
        non_valids = 0
        for i in range(1,10):
            counter +=1
            if valid(board, row, column, i):
                board[row][column] = i
                if solve(board):
                    return board
                board[row][column] = 0
        return False
        
def Soduku_Prompt():
    '''
    Takes in a User Inputted Sudoku Board
    and Prints the Solved Verson
    
    
    '''
    print('Welcome to Sudoku Solver! \n')

    board = []
    for i in range(1, 10):
        row = input(f'Enter Row {i} Seperated By Spaces: ')
        temp = list(row.strip().split(' '))
        board.append([int(i) for i in temp])
    print('')
    print('Solving Board...')
    print_board(board)
    time.sleep(1)
    try:
        print('\n')
        
        print_board(solve(board))
        print(f'Solved in {counter} iterations. Congrats!')
    except:
        print('Board Error! Please Try Again!\n')
        Soduku_Prompt()
        
        




if __name__ == '__main__': 
    Soduku_Prompt()
    '''

    # Example board
    board =[[0, 0, 3, 0, 0, 4, 0, 5, 8],
        [6, 0, 0, 1, 0, 0, 0, 0, 2],
        [2, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 7, 9, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 8, 0, 3, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 8, 0, 9, 0],
        [0, 2, 0, 0, 9, 0, 0, 0, 1],
        [8, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
   
