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

        if self.hamiltonianCycleGeneratedFlag: return
        self.hamiltonianCycleGeneratedFlag = True

        # initialize
        self.hamiltonianCycleInitialization()

        thisCell = (self.hamiltonianCycleRoot[0], self.hamiltonianCycleRoot[1], -1)
        completeFlag = False
        self.gourdsAssignedPositions.append([thisCell[0], thisCell[1]])

        while (not completeFlag):

            # animation
            # pygame.time.delay(80)
            # redrawTheScreen()
            # search for next step

            neighbourList = self.searchAllPossibleAssignment(thisCell)
            availableNextCellList = []

            # filter
            for neighbour in neighbourList:
                if [neighbour[0], neighbour[1]] not in self.gourdsAssignedPositions:  # not visit yet
                    if neighbour[2] > self.hamiltonianCycleMap[thisCell[1]][thisCell[0]]:  # next.from >= this.to
                        availableNextCellList.append(neighbour)
                if neighbour[0] == self.hamiltonianCycleRoot[0] and neighbour[1] == self.hamiltonianCycleRoot[1]:  # is the root
                    pass
                    # if len(self.gourdsAssignedPositions) == totalNumberOfCells:
                    #     self.gourdsAssignedPositions.append(self.gourdsAssignedPositions[0])
                    #     self.hamiltonianCycleMap[thisCell[1]][thisCell[0]] = neighbour[2]
                    #     completeFlag = True
                    #     break



            # go to next step
            if not completeFlag:
                lastCell = self.gourdsAssignedPositions[len(self.gourdsAssignedPositions) - 1]
                if len(availableNextCellList) == 0:  # no next step
                    self.gourdsAssignedPositions.pop()
                    self.hamiltonianCycleMap[thisCell[1]][thisCell[0]] = 0
                    thisCell = self.gourdsAssignedPositions[len(self.gourdsAssignedPositions) - 1]

                    # print("go back")

                else:  # there is next step
                    # record the footprint
                    thisCell = availableNextCellList[0]
                    self.gourdsAssignedPositions.append([thisCell[0], thisCell[1]])
                    self.hamiltonianCycleMap[lastCell[1]][lastCell[0]] = thisCell[2]
                    # print("goto: ", thisCell)

