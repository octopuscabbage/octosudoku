__author__ = 'octopuscabbage_'

from SudokuSolver import SudokuCells


def main():
    # //load file
    # while not solved:
    # build set of row, column, square numbers
    # for each open cell:
    #      update set of available choices
    # if any nodes have 1 choice:
    #      put that choice down
    # else any nodes have no choices:
    #      reset unfinal cells
    # else:
    #      guess an avilable choice in a cell


    #load file
    sudokuCells = SudokuCells()
    sudokuCells.getParse((parse("sudoku.txt")))
    while not sudokuCells.isSolved():
        sudokuCells.buildSets()
        if sudokuCells.testChoiceInCells( lambda x,y: len(sudokuCells.sudokulist[x][y].possibilities)==1):
            sudokuCells.testPossibilities()
        elif sudokuCells.apply_test_on_all_cells(lambda x,y: len(sudokuCells.sudokulist[x][y].possibilities)==0 ):
            sudokuCells.reset_cells()
        else:
            sudokuCells.guess()




def parse(file):
    sudokulist = [[0 for x in range(9)] for x in range(9)]
    column, row = 0, 0

    with open(file) as fileobj:
        for word in fileobj:
            for ch in word:
                if ch != " " and ch != "\n" and row < 9:
                    sudokulist[row][column] = ch
                    column += 1
                    if (column >= 9):
                        row += 1
                        column = 0
    return sudokulist


main()