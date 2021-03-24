import numpy
import pygame

class finalGourdsConfig(object):

    def __init__(self, screen, board, gourdsList, coloursLibrary, offset, widthOfHexCell):
        # Hamiltonian Cycle
        self.screen = screen
        self.widthOfHexCell = widthOfHexCell
        self.offset = offset
        self.board = board
        self.gourdsList = gourdsList
        self.coloursLibrary = coloursLibrary
        self.totalNumberOfCells = 0
        self.gourdsPossiblePositions = []
        self.gourdsAssignedPositions = []
        self.gourdsAssignedFootprintStack = []


    def searchAllPossibleAssignment(self):
        self.gourdsPossiblePositions.clear()
        maxOfX = len(self.board[0]) - 1
        maxOfY = len(self.board) - 1
        for y in range(maxOfY):
            for x in range(maxOfX):

                if self.board[y][x] != 0:
                    for gourdIndex in range(len(self.gourdsList)):
                        if x + 2 <= maxOfX:# From Left 1 to right 4
                            if (self.board[y][x] == self.gourdsList[gourdIndex][4] and
                                    self.board[y][x + 2] == self.gourdsList[gourdIndex][5]):
                                self.gourdsPossiblePositions.append([gourdIndex, x, y, x + 2, y])
                            elif (self.board[y][x] == self.gourdsList[gourdIndex][5] and
                                    self.board[y][x + 2] == self.gourdsList[gourdIndex][4]):
                                self.gourdsPossiblePositions.append([gourdIndex, x + 2, y, x, y])
                        if x + 1 <= maxOfX and y + 1 <= maxOfY:# from upper left 2 to lower right 5
                            if (self.board[y][x] == self.gourdsList[gourdIndex][4] and
                                    self.board[y + 1][x + 1] == self.gourdsList[gourdIndex][5]):
                                self.gourdsPossiblePositions.append([gourdIndex, x, y, x + 1, y + 1])
                            elif (self.board[y][x] == self.gourdsList[gourdIndex][5] and
                                  self.board[y + 1][x + 1] == self.gourdsList[gourdIndex][4]):
                                self.gourdsPossiblePositions.append([gourdIndex, x + 1, y + 1, x, y])
                        if x - 1 >= 0 and y + 1 <= maxOfY:# from upper right 3 to lower left 6
                            if (self.board[y][x] == self.gourdsList[gourdIndex][4] and
                                    self.board[y + 1][x - 1] == self.gourdsList[gourdIndex][5]):
                                self.gourdsPossiblePositions.append([gourdIndex, x, y, x - 1, y + 1])
                            elif (self.board[y][x] == self.gourdsList[gourdIndex][5] and
                                  self.board[y + 1][x - 1] == self.gourdsList[gourdIndex][4]):
                                self.gourdsPossiblePositions.append([gourdIndex, x - 1, y + 1, x, y])

        print(self.gourdsPossiblePositions)
        return


    def finalConfigGenerator(self):
        # DFS
        pass
