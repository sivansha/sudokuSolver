import misc

"""
input: a 9*9 matrix, indicating a sudoku
do: prints the sudoku
"""
def printSudoku(sudoku):
    for row in sudoku:
        for number in row:
            print(number, end=" ")
        print()

"""
though getRow is not necessary because getting a row is simple, it is defined in order to keep uniformity with getCol.
input: input: a sudoku and a tuple indicating row
output: the row
"""
def getRow(sudoku, row):
    return sudoku[row]

"""
input: input: a sudoku and a tuple indicating column
output: the column
"""
def getCol(sudoku, col):
    nums = []
    for row in sudoku:
        nums.append(row[col])
    return nums

"""
input: a tuple indicating a cell
output: in which region the cell is
"""
def whichRegion(cell):
    if cell[0] == 0 or cell[0] == 1 or cell[0] == 2:
        if cell[1] == 0 or cell[1] == 1 or cell[1] == 2:
            return 1
        if cell[1] == 3 or cell[1] == 4 or cell[1] == 5:
            return 2
        if cell[1] == 6 or cell[1] == 7 or cell[1] == 8:
            return 3
    if cell[0] == 3 or cell[0] == 4 or cell[0] == 5:
        if cell[1] == 0 or cell[1] == 1 or cell[1] == 2:
            return 4
        if cell[1] == 3 or cell[1] == 4 or cell[1] == 5:
            return 5
        if cell[1] == 6 or cell[1] == 7 or cell[1] == 8:
            return 6
    if cell[0] == 6 or cell[0] == 7 or cell[0] == 8:
        if cell[1] == 0 or cell[1] == 1 or cell[1] == 2:
            return 7
        if cell[1] == 3 or cell[1] == 4 or cell[1] == 5:
            return 8
        if cell[1] == 6 or cell[1] == 7 or cell[1] == 8:
            return 9

"""
input: input: a sudoku and a tuple indicating a cell
output: the region of the cell
"""
def getRegion(sudoku, col):
    nums = []
    region = whichRegion(col)
    if 1 == region:
        nums = nums + sudoku[0][:3]
        nums = nums + sudoku[1][:3]
        nums = nums + sudoku[2][:3]
    if 2 == region:
        nums = nums + sudoku[0][3:6]
        nums = nums + sudoku[1][3:6]
        nums = nums + sudoku[2][3:6]
    if 3 == region:
        nums = nums + sudoku[0][6:]
        nums = nums + sudoku[1][6:]
        nums = nums + sudoku[2][6:]
    if 4 == region:
        nums = nums + sudoku[3][:3]
        nums = nums + sudoku[4][:3]
        nums = nums + sudoku[5][:3]
    if 5 == region:
        nums = nums + sudoku[3][3:6]
        nums = nums + sudoku[4][3:6]
        nums = nums + sudoku[5][3:6]
    if 6 == region:
        nums = nums + sudoku[3][6:]
        nums = nums + sudoku[4][6:]
        nums = nums + sudoku[5][6:]
    if 7 == region:
        nums = nums + sudoku[6][:3]
        nums = nums + sudoku[7][:3]
        nums = nums + sudoku[8][:3]
    if 8 == region:
        nums = nums + sudoku[6][3:6]
        nums = nums + sudoku[7][3:6]
        nums = nums + sudoku[8][3:6]
    if 9 == region:
        nums = nums + sudoku[6][6:]
        nums = nums + sudoku[7][6:]
        nums = nums + sudoku[8][6:]
    return nums

"""
input: a sudoku and a tuple indicating a cell (row, col)
output: a list that with all the numbers that currently are not on the same row, column or 3*3 region.
"""
def findAllPossibleNumbers(sudoku, cell):
    possibleNum = misc.numbers
    rowNum = list(filter(lambda a: a != 0, getRow(sudoku, cell[0])))
    colNum = list(filter(lambda a: a != 0, getCol(sudoku, cell[1])))
    regNum = list(filter(lambda a: a != 0, getRegion(sudoku, (cell[0], cell[1]))))

    possibleNum = [item for item in possibleNum if item not in rowNum and item not in colNum and item not in regNum]

    return possibleNum
