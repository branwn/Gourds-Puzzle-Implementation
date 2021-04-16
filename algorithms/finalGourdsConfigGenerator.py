

class finalGourdsConfig(object):

    def __init__(self, screen, board, gourdsList, coloursLibrary, offset, widthOfHexCell):
        # Hamiltonian Cycle
        self.screen = screen
        self.widthOfHexCell = widthOfHexCell
        self.offset = offset
        self.board = board
        self.gourdsList = gourdsList
        self.coloursLibrary = coloursLibrary
        self.gourdsPossibleLocations = {}
        self.gourdsAssignedDict = {}
        self.gourdsFootprint = {}
        self.totalNumberOfGourds = len(gourdsList)
        self.finishedFlag = False

    def isAllGourdsAssigned(self):
        # print(self.gourdsAssignedDict)

        if len(self.gourdsAssignedDict) == self.totalNumberOfGourds:
            self.gourdsFootprint = {}
            self.gourdsPossibleLocations = {}
            return True

        return False

    def listAllPossibleAssignment(self):
        boardTemp = self.board.copy()
        possibleLocationsStack = []
        maxOfX = len(boardTemp[0]) - 1
        maxOfY = len(boardTemp) - 1

        # set the assigned locations as 0 (unavailable)
        for i in range(self.totalNumberOfGourds):
            location = self.gourdsAssignedDict.get(i)
            if location is not None and location != []:
                boardTemp[location[2]][location[1]] = 0
                boardTemp[location[4]][location[3]] = 0
        # print(boardTemp)

        # search for available locations
        for y in range(len(boardTemp)):
            for x in range(len(boardTemp[0])):
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


        # stack to dict
        for i in range(self.totalNumberOfGourds):
            self.gourdsPossibleLocations[i] = []

            # add the possibles location to the gourdsPossibleLocations

            for stack in possibleLocationsStack:
                if stack[0] == i:
                    if self.gourdsFootprint.get(i) is None:
                        self.gourdsPossibleLocations[i].append(stack)
                    else:
                        # filter out the visited stack
                        if stack not in self.gourdsFootprint.get(i):
                            self.gourdsPossibleLocations[i].append(stack)


        return

    def allGourdsHavePossibleLocation(self):
        for i in range(self.totalNumberOfGourds):




            if self.gourdsAssignedDict.get(i) is None or self.gourdsAssignedDict.get(i) == []:
                if self.gourdsPossibleLocations.get(i) == []:
                    return False



        return True

    def assignGourds(self):

        listOfLocations = []

        # go next step
        isAssigned = False
        for i in range(self.totalNumberOfGourds):
            # clear the footprints of latest gourds
            if not isAssigned:
                listOfLocations = self.gourdsPossibleLocations[i]
                if self.gourdsAssignedDict.get(i) is None:

                    isAssigned = True
                    self.gourdsAssignedDict[i] = listOfLocations[0]
                    # record this footprint
                    if self.gourdsFootprint.get(i) is None:
                        self.gourdsFootprint[i] = []
                    self.gourdsFootprint[i].append(listOfLocations[0])
                    continue
            else:
                self.gourdsFootprint[i] = []

    def returnToLastStep(self):
        for i in range(self.totalNumberOfGourds):
            if self.gourdsAssignedDict.get(i) is None and i >= 1:
                self.gourdsAssignedDict[i-1] = []
                break

    def finalConfigGenerator(self):


        if self.finishedFlag: return

        # DFS
        while(not self.finishedFlag):


            # pygame.time.delay(1000)
            # print("possible :", self.gourdsPossibleLocations)
            # print('')
            # print("footprint:", self.gourdsFootprint)
            # print("dict     :", self.gourdsAssignedDict)

            # all gourds have been assigned?
            if self.isAllGourdsAssigned():
                self.finishedFlag = True

                print("The final configuration: ", self.gourdsAssignedDict)

                return True

            # list all possible location
            self.listAllPossibleAssignment()

            # If there are gourds have no possible location?
            if self.allGourdsHavePossibleLocation():
                # go to next step
                self.assignGourds()


            else:
                # return to last step
                self.returnToLastStep()





