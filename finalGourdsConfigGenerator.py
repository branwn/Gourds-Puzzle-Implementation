

class finalGourdsConfig(object):

    def __init__(self, screen, board, gourdsList, coloursLibrary, offset, widthOfHexCell):
        # Hamiltonian Cycle
        self.screen = screen
        self.widthOfHexCell = widthOfHexCell
        self.offset = offset
        self.board = board
        self.gourdsList = gourdsList
        self.coloursLibrary = coloursLibrary
        self.gourdsPossibleLocations = []
        self.gourdsAssignedDict = {}
        self.gourdsAssignedFootprintStack = []
        self.totalNumberOfGourds = len(gourdsList)



    def isAllGourdsAssigned(self):
        # print(self.gourdsAssignedDict)

        if len(self.gourdsAssignedDict) == self.totalNumberOfGourds:
            return True

        return False

    def listAllPossibleAssignment(self):
        boardTemp = self.board.copy()
        possibleLocationsStack = []
        maxOfX = len(boardTemp[0]) - 1
        maxOfY = len(boardTemp) - 1

        # set the assigned locations as 0
        for i in range(self.totalNumberOfGourds):
            location = self.gourdsAssignedDict.get(i)
            if location is not None:
                boardTemp[location[2]][location[1]] = 0
                boardTemp[location[4]][location[3]] = 0
        print(boardTemp)

        # search for available locations
        for y in range(maxOfY):
            for x in range(maxOfX):
                if boardTemp[y][x] != 0:
                    for gourdIndex in range(len(self.gourdsList)):
                        if x + 2 <= maxOfX:# From Left 1 to right 4
                            if (boardTemp[y][x] == self.gourdsList[gourdIndex][4] and
                                    boardTemp[y][x + 2] == self.gourdsList[gourdIndex][5]):
                                possibleLocationsStack.append([gourdIndex, x, y, x + 2, y])
                            elif (boardTemp[y][x] == self.gourdsList[gourdIndex][5] and
                                    boardTemp[y][x + 2] == self.gourdsList[gourdIndex][4]):
                                possibleLocationsStack.append([gourdIndex, x + 2, y, x, y])
                        if x + 1 <= maxOfX and y + 1 <= maxOfY:# from upper left 2 to lower right 5
                            if (boardTemp[y][x] == self.gourdsList[gourdIndex][4] and
                                    boardTemp[y + 1][x + 1] == self.gourdsList[gourdIndex][5]):
                                possibleLocationsStack.append([gourdIndex, x, y, x + 1, y + 1])
                            elif (boardTemp[y][x] == self.gourdsList[gourdIndex][5] and
                                  boardTemp[y + 1][x + 1] == self.gourdsList[gourdIndex][4]):
                                possibleLocationsStack.append([gourdIndex, x + 1, y + 1, x, y])
                        if x - 1 >= 0 and y + 1 <= maxOfY:# from upper right 3 to lower left 6
                            if (boardTemp[y][x] == self.gourdsList[gourdIndex][4] and
                                    boardTemp[y + 1][x - 1] == self.gourdsList[gourdIndex][5]):
                                possibleLocationsStack.append([gourdIndex, x, y, x - 1, y + 1])
                            elif (boardTemp[y][x] == self.gourdsList[gourdIndex][5] and
                                  boardTemp[y + 1][x - 1] == self.gourdsList[gourdIndex][4]):
                                possibleLocationsStack.append([gourdIndex, x - 1, y + 1, x, y])

        # stack to list
        self.gourdsPossibleLocations.clear()
        for i in range(self.totalNumberOfGourds):
            self.gourdsPossibleLocations.append([i])

            for stack in possibleLocationsStack:
                if stack[0] == i:
                   self.gourdsPossibleLocations[i].append(stack)


        print(self.gourdsPossibleLocations)
        return

    def allGourdsHavePossibleLocation(self):
        for i in range(self.totalNumberOfGourds):

            # print (self.gourdsAssignedLocations.get(i))
            # print (len(self.gourdsPossibleLocations[i]))

            if self.gourdsAssignedDict.get(i) is None:
                if len(self.gourdsPossibleLocations[i]) <= 1:

                    return False

        return True

    def returnToLastStep(self):


        pass

    def assignGourds(self):
        for aLine in self.gourdsPossibleLocations:
            if len(aLine) >= 2:
                self.gourdsAssignedDict[aLine[0]] = aLine[1]
                return

        self.gourdsAssignedFootprintStack.append(aLine[1])
        pass

    def finalConfigGenerator(self, buttonState):
        # DFS
        if not buttonState: return

        finishedFlag = False
        while(not finishedFlag):
            # all gourds have been assigned?
            if self.isAllGourdsAssigned():
                return True

            # list all possible location
            self.listAllPossibleAssignment()

            # If there are gourds have no possible location?
            if not self.allGourdsHavePossibleLocation():
                # return to last step
                self.returnToLastStep()

            else:
                # assign next step
                self.assignGourds()


            finishedFlag = True


