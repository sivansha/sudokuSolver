numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku1 = [[0, 0, 0, 0, 2, 0, 4, 0, 0],
           [9, 0, 6, 0, 8, 0, 0, 0 ,0],
           [0, 0, 0, 0, 0, 3, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 7, 5, 4],
           [3, 8, 0, 0, 0, 0, 0, 2, 0],
           [1, 0, 0, 0, 0, 0, 0, 3, 0],
           [0, 5, 0, 4, 0, 0, 0, 0, 2],
           [0, 7, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 3, 5, 0, 7, 0, 0, 0]]

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
input: input: a sudoku and a tuple indicating a cell
output: the region of the cell
"""
def getRegion(sudoku, col):
    nums = []

    return nums

"""
input: a sudoku and a tuple indicating a cell (row, col)
output: a list that with all the numbers that currently are not on the same row, column or 3*3 region.
"""
def findAllPossibilities(sudoku, cell):
    rowNum = list(filter(lambda a: a != 0, getRow(cell[0])))
    possibleRowNum = numbers
    for num in rowNum:
        possibleRowNum = list(filter(lambda a: a != num, possibleRowNum))
    # get all numbers on same col that are not 0
    colNum = list(filter(lambda a: a != 0, getCol[cell[1]]))
    possibleColNum = numbers
    for num in colNum:
        possibleColNum = list(filter(lambda a: a != num, possibleColNum))


