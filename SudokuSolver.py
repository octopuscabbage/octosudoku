__author__ = 'octopuscabbage_'


class Cell:
    def __init__(self, value, final):
        self.value = value
        self.final = final
        self.possibilities = {}


class SudokuCells:
    def __init__(self):
        self.sudokulist = [[Cell(0, False) for x in range(9)] for x in range(9)]
        self.universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def isSolved(self):
        for value in self.values():
            if value == 0:
                return False
        return True

    def testPossibilities(self):
        for x, y in self.coordinates():
            self.sudokulist[x][y].value = self.sudokulist[x][y].pop()

    def testChoiceInCells(self, value):
        for x, y in self.coordinates():
            if len(self.sudokulist[x][y].possibilities) == value:
                return True
        return False
    def apply_test_on_all_cells(self, test):
        for x,y in self.coordinates():
            if test(x,y):
                return True
        return False
    def reset_cells(self):
        for x,y in self.coordinates():
            if not self.sudokulist[x][y].final:
                self.sudokulist[x][y].value = 0
        return
    def guess(self):
        for x,y in self.coordinates():
            if not self.sudokulist[x][y].final and self.sudokulist[x][y].value == 0:
                self.sudokulist[x][y].value = self.sudokulist[x][y].possibilities.pop()


    def buildSets(self):
        for x, y in self.coordinates():
            if not self.sudokulist[x][y].final and self.sudokulist[x][y] == 0:
                column_set = self.__get_column(x, y)
                row_set = self.__get_row(x, y)
                square_set = self.__get_square(x, y)
                column_difference = self.universal_set.difference(column_set)
                row_difference = self.universal_set.difference(row_set)
                square_set = self.universal_set.difference(square_set)
                self.sudokulist[x][y].possibilities = square_set.intersection(
                    row_difference.intersection(column_difference))

    def __get_column(self, x, y):
        column_set = set()
        for x in range(0, 10):
            column_set.add(self.sudokulist[x][y])
        return column_set

    def __get_row(self, x, y):
        row_set = set()
        for x in range(0, 10):
            row_set.add(self.sudokulist[x][y])
        return row_set

    def __get_square(self, x, y):
        square_set = set()
        for x_pos, y_pos in self.coordinates():

            if x > 3 and x_pos > 3:
                self.__y_test(y, y_pos, x_pos, square_set)
            elif x > 6 and x_pos > 6:
                self.__y_test(y, y_pos, x_pos, square_set)
            else:
                self.__y_test(y, y_pos, x_pos, square_set)
        return square_set

    def __y_test(self, y, y_pos, x_pos, square_set):
        if y > 3 and y_pos > 3:
            square_set.add(self.sudokulist[x_pos][y_pos])
        elif y > 6 and y_pos > 6:
            square_set.add(self.sudokulist[x_pos][y_pos])
        else:
            square_set.add(self.sudokulist[x_pos][y_pos])

    def getParse(self, parseList):
        for x, y in self.coordinates():
            if parseList[x][y] == "-":
                self.sudokulist[x][y] = Cell(0, False)
        else:
            self.sudokulist[x][y] = Cell(int(parseList[x][y]), True)


    def coordinates(self):
        for x in range(0, 10):
            for y in range(0, 10):
                yield x, y


    def values(self):
        for x, y in self.coordinates():
            yield self.sudokulist[x][y]
