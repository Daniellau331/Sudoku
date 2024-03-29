# program for solving Sudoku problems by using backtracking algorithm
# solver.py


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# solver function
def solver(bo):
    find = find_empty(bo)
    # no more empty spot
    if not find:
        return True
    # still have empty spot
    else:
        # find returns the row and the col of the empty spot
        row , col = find

    for guess in range(1,10):
        if(checker(bo,guess,row,col)):
            bo[row][col]=guess

            if solver(bo):
                return True

            bo[row][col]=0

    return False



# function that to checker whether a number is a good guess
def checker(bo,guess,row,col):

    # check row
    for i in range(len(bo)):
        if bo[row][i] ==guess and i != col:
            return False

    # check col
    for i in range(len(bo)):
        if bo[i][col] == guess and i != row:
            return False

    # check box
    # we want to know which box the current guess is in
    # True -  good guess     False - bad guess
    box_x = col //3
    box_y = row //3

    for i in range(box_x*3,box_x+3):
        for j in range(box_y*3,box_y+3):
            if bo[j][i]==guess and j!=row and i !=col:
                return False

    return True




# function that prints the Sudoku board , 0 means empty spot
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")




def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None



print("Problem:")
print_board(board)
solver(board)
print("+++++++++++", end="\n\n")
print("Ans:")
print_board(board)
