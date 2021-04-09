import numpy
import pygame

class hamiltonianCycle(object):

    def __init__(self, screen, board, coloursLibrary, offset, widthOfHexCell):
        # Hamiltonian Cycle
        self.screen = screen
        self.widthOfHexCell = widthOfHexCell
        self.offset = offset
        self.board = board
        self.coloursLibrary = coloursLibrary
        self.totalNumberOfCells = 0
        self.hamiltonianCycleRoot = -1, -1
        self.hamiltonianCycleMap = numpy.zeros_like(board)  # 1 for right hand side, and count in clockwise
        self.hamiltonianCycleStack = []
        self.hamiltonianCycleGeneratedFlag = False


    def searchNeighbourCells(self, cellIn):
        x = cellIn[0]
        y = cellIn[1]
        # obtain the size of the boardMatrix
        maxOfX = len(self.board[0]) - 1
        maxOfY = len(self.board) - 1

        results = []  # (x, y, from, to)
        # search neighbour cells around the cellIn
        # know the neighbour x, y, from but not know where to go(set as default 0)
        if x + 2 <= maxOfX:
            if (self.board[y][x + 2] != 0):  # From Left 1 to right 4
                results.append([x + 2, y, 1, 0])
        if x + 1 <= maxOfX and y + 1 <= maxOfY:
            if (self.board[y + 1][x + 1] != 0):  # from upper left 2 to lower right 5
                results.append([x + 1, y + 1, 2, 0])
        if x - 1 >= 0 and y + 1 <= maxOfY:
            if (self.board[y + 1][x - 1] != 0):  # from upper right 3 to lower left 6
                results.append([x - 1, y + 1, 3, 0])
        if x - 2 >= 0:
            if (self.board[y][x - 2] != 0):  # from right 4 to left 1
                results.append([x - 2, y, 4, 0])
        if x - 1 >= 0 and y - 1 >= 0:
            if (self.board[y - 1][x - 1] != 0):  # from lower right 5 to upper left 2
                results.append([x - 1, y - 1, 5, 0])
        if x + 1 <= maxOfX and y - 1 >= 0:
            if (self.board[y - 1][x + 1] != 0):  # from lower left 6 to upper right 3
                results.append([x + 1, y - 1, 6, 0])

        return results


    def hamiltonianCycleInitialization(self):
        # to generate a root and count the #cells
        #
        global hamiltonianCycleRoot
        global totalNumberOfCells
        totalNumberOfCells = 0

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != 0:
                    totalNumberOfCells = totalNumberOfCells + 1
                    if (self.hamiltonianCycleRoot[0] == -1):
                        self.hamiltonianCycleRoot = x, y
        return


    def hamiltonianCycleGenerator(self):
        # DFS

        if self.hamiltonianCycleGeneratedFlag: return
        self.hamiltonianCycleGeneratedFlag = True

        # initialize
        self.hamiltonianCycleInitialization()

        thisCell = (self.hamiltonianCycleRoot[0], self.hamiltonianCycleRoot[1], -1)
        completeFlag = False
        self.hamiltonianCycleStack.append([thisCell[0], thisCell[1]])

        while (not completeFlag):

            # animation
            # pygame.time.delay(80)
            # redrawTheScreen()
            # search for next step

            neighbourList = self.searchNeighbourCells(thisCell)
            availableNextCellList = []

            # filter
            for neighbour in neighbourList:
                if [neighbour[0], neighbour[1]] not in self.hamiltonianCycleStack:  # not visit yet
                    if neighbour[2] > self.hamiltonianCycleMap[thisCell[1]][thisCell[0]]:  # next.from >= this.to
                        availableNextCellList.append(neighbour)
                if neighbour[0] == self.hamiltonianCycleRoot[0] and neighbour[1] == self.hamiltonianCycleRoot[1]:  # is the root
                    if len(self.hamiltonianCycleStack) == totalNumberOfCells:
                        self.hamiltonianCycleStack.append(self.hamiltonianCycleStack[0])
                        self.hamiltonianCycleMap[thisCell[1]][thisCell[0]] = neighbour[2]
                        completeFlag = True
                        break



            # go to next step
            if not completeFlag:
                lastCell = self.hamiltonianCycleStack[len(self.hamiltonianCycleStack) - 1]
                if len(availableNextCellList) == 0:  # no next step
                    self.hamiltonianCycleStack.pop()
                    self.hamiltonianCycleMap[thisCell[1]][thisCell[0]] = 0
                    thisCell = self.hamiltonianCycleStack[len(self.hamiltonianCycleStack) - 1]

                    # print("go back")

                else:  # there is next step
                    # record the footprint
                    thisCell = availableNextCellList[0]
                    self.hamiltonianCycleStack.append([thisCell[0], thisCell[1]])
                    self.hamiltonianCycleMap[lastCell[1]][lastCell[0]] = thisCell[2]
                    # print("goto: ", thisCell)

        print ("hamiltonianCycleGenerator finished")


    def hamiltonianCycleDrawer(self, buttonStates2):
        if not buttonStates2: return

        if not self.hamiltonianCycleGeneratedFlag:
            self.hamiltonianCycleGenerator()

        for i in range(len(self.hamiltonianCycleStack) - 1):
            pygame.draw.line(self.screen, self.coloursLibrary['backGround'],
                             (int(self.offset + self.hamiltonianCycleStack[i][0] * self.widthOfHexCell),
                              int(self.offset + self.hamiltonianCycleStack[i][1] * self.widthOfHexCell * 1.732)),
                             (int(self.offset + self.hamiltonianCycleStack[i + 1][0] * self.widthOfHexCell),
                              int(self.offset + self.hamiltonianCycleStack[i + 1][1] * self.widthOfHexCell * 1.732)),
                             4)
            pygame.draw.line(self.screen, self.coloursLibrary['hamiltonianCycle'],
                             (int(self.offset + self.hamiltonianCycleStack[i][0] * self.widthOfHexCell),
                              int(self.offset + self.hamiltonianCycleStack[i][1] * self.widthOfHexCell * 1.732)),
                             (int(self.offset + self.hamiltonianCycleStack[i + 1][0] * self.widthOfHexCell),
                              int(self.offset + self.hamiltonianCycleStack[i + 1][1] * self.widthOfHexCell * 1.732)),
                             2)
