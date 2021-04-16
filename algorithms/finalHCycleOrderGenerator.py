import copy

import pygame


class finalHCycleOrderGenerator(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig):
        self.screen = screen
        self.myBoardsConfig = copy.deepcopy(myBoardsConfig)
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        # self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.HCycleAux = self.myHamiltonianCycle.HCycleAux
        self.gourdsFinalOrderInHCycle = []
        self.stackOfFootPrint = []
        self.emptyCellIndex = -1

        # build up final gourds config
        finalGourdsList = copy.deepcopy(self.myBoardsConfig.gourdsList)
        for i in range(len(finalGourdsList)):
            finalGourdsList[i][0] = self.myFinalGourdsConfig.gourdsAssignedDict.get(i)[1]
            finalGourdsList[i][1] = self.myFinalGourdsConfig.gourdsAssignedDict.get(i)[2]
            finalGourdsList[i][2] = self.myFinalGourdsConfig.gourdsAssignedDict.get(i)[3]
            finalGourdsList[i][3] = self.myFinalGourdsConfig.gourdsAssignedDict.get(i)[4]

        # set values
        self.myBoardsConfig.gourdsList = finalGourdsList
        self.gourdsList = self.myBoardsConfig.gourdsList
        self.board = self.myBoardsConfig.board

    def runFinalHCycleOrderGenerator(self):


        # move the gourds
        while(self.ifThereIsGourdsNotAligned()):
            # print (self.HCycleAux[rootIndex + i])
            # find the empty cell
            rootIndex = -1
            for aCell in self.myHamiltonianCycle.hamiltonianCycleStack:
                rootIndex += 1
                isEmpty, indexOfGourds = self.isCellEmpty(aCell)
                if isEmpty: break

            if rootIndex == -1:
                print("---WARN--- No empty cell found")
                return False

            self.gourdsMovementControllerInOrderGenerator(rootIndex)



        # record the empty cell
        for i in range(len(self.myHamiltonianCycle.HCycleAux)):
            isEmpty, indexOfGourds = self.isCellEmpty(self.myHamiltonianCycle.HCycleAux[i])
            if isEmpty:
                self.emptyCellIndex = i
                break

        self.gourdsFinalOrderInHCycleGenerator()

        print(self.stackOfFootPrint)
        print(self.gourdsFinalOrderInHCycle)
        print(self.emptyCellIndex)

    def gourdsFinalOrderInHCycleGenerator(self):
        orderlist = []

        for cell in self.myHamiltonianCycle.hamiltonianCycleStack:
            for i in range(self.myFinalGourdsConfig.totalNumberOfGourds):
                if i not in orderlist:
                    gourd = self.myFinalGourdsConfig.gourdsAssignedDict.get(i)
                    if gourd[1] == cell[0] and gourd[2] == cell[1]:
                        orderlist.append(i)
                        break
                    elif gourd[3] == cell[0] and gourd[4] == cell[1]:
                        orderlist.append(i)
                        break

        print("\tThe order of gourds should be reached in phase 2: ",orderlist)
        self.gourdsFinalOrderInHCycle = orderlist
        return self.gourdsFinalOrderInHCycle

    def ifThereIsGourdsNotAligned(self):
        for gourds in self.myBoardsConfig.gourdsList:
            for HCycleCellIndex in range(1, len(self.HCycleAux)):
                if (gourds[0] == self.HCycleAux[HCycleCellIndex][0] and gourds[1] == self.HCycleAux[HCycleCellIndex][1]):
                    if (gourds[2] == self.HCycleAux[HCycleCellIndex+1][0] and gourds[3] == self.HCycleAux[HCycleCellIndex+1][1]):
                        break
                    elif (gourds[2] == self.HCycleAux[HCycleCellIndex-1][0] and gourds[3] == self.HCycleAux[HCycleCellIndex-1][1]):
                        break
                    return True
        return False

    def isCellEmpty(self, aCell):
        isEmpty = True
        gourdsIndexInHCycle = -1
        for aGourds in self.myBoardsConfig.gourdsList:
            gourdsIndexInHCycle += 1
            if (aCell[0] == aGourds[0] and aCell[1] == aGourds[1]):
                isEmpty = False
                break
            elif (aCell[0] == aGourds[2] and aCell[1] == aGourds[3]):
                isEmpty = False
                break
        if isEmpty:
            return True, -1
        return False, gourdsIndexInHCycle

    def movesAloneTheHCycle(self, HCycleIndex):
        # move first part
        HCycleIndex += 1


        gourdsIndex, partIndex  = self.gourdsClicked(self.HCycleAux[HCycleIndex], 'al')
        if gourdsIndex == -1:
            print ("---WARN--- No these gourds found!")
            return False



        # check if the next part is along the HCycle
        if (self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex] == self.HCycleAux[HCycleIndex][0]
                and self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex+1] == self.HCycleAux[HCycleIndex][1]):
            # is along the HCycle
            pass
        else:
            # is not along the HCycle
            nextPartofGourds = self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex], self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex+1]
            # move the next part
            self.gourdsClicked(nextPartofGourds, 'al')

    def gourdsMovementControllerInOrderGenerator(self, HCycleIndex):
        isEmpty, indexOfGourds = self.isCellEmpty(self.HCycleAux[HCycleIndex])
        if not isEmpty:
            if (self.myBoardsConfig.gourdsList[indexOfGourds][0] == self.HCycleAux[HCycleIndex][0]
                    and self.myBoardsConfig.gourdsList[indexOfGourds][1] == self.HCycleAux[HCycleIndex][1]):
                # is the first part
                if (self.myBoardsConfig.gourdsList[indexOfGourds][2] == self.HCycleAux[HCycleIndex+1][0]
                    and self.myBoardsConfig.gourdsList[indexOfGourds][3] == self.HCycleAux[HCycleIndex+1][1]):
                    return True
                elif(self.myBoardsConfig.gourdsList[indexOfGourds][2] == self.HCycleAux[HCycleIndex-1][0]
                    and self.myBoardsConfig.gourdsList[indexOfGourds][3] == self.HCycleAux[HCycleIndex-1][1]):
                    return True
                # click the second part
                theNextPart = self.myBoardsConfig.gourdsList[indexOfGourds][2], self.myBoardsConfig.gourdsList[indexOfGourds][3]

            else:
                # is the second part
                if (self.myBoardsConfig.gourdsList[indexOfGourds][0] == self.HCycleAux[HCycleIndex+1][0]
                    and self.myBoardsConfig.gourdsList[indexOfGourds][1] == self.HCycleAux[HCycleIndex+1][1]):
                    return True
                elif (self.myBoardsConfig.gourdsList[indexOfGourds][0] == self.HCycleAux[HCycleIndex - 1][0]
                      and self.myBoardsConfig.gourdsList[indexOfGourds][1] == self.HCycleAux[HCycleIndex - 1][1]):
                    return True
                # click the first part
                theNextPart = self.myBoardsConfig.gourdsList[indexOfGourds][0], self.myBoardsConfig.gourdsList[indexOfGourds][1]

            self.gourdsClicked(theNextPart, 'al')
            return True


        self.movesAloneTheHCycle(HCycleIndex)

        # print(partIndex)

        return True

    # copied from gourds constructor
    def gourdsClicked(self, pos, mode):
        # search Gourds by the given Coordinate

        indexOfGourd, xGourd, yGourd = self.gourdsSearchingByIndex(pos[0], pos[1])

        if indexOfGourd != -1:
            # print(xGourd, yGourd)
            # search if there is an Empty Cell Around
            xCell, yCell = self.emptyCellSearchingAroundAGourd(xGourd, yGourd)
            if xCell != -1:
                # move gourd to the empty cell

                return self.gourdsMovementController(indexOfGourd, xGourd, yGourd, xCell, yCell)



            return -1, -1
        return -1, -1

    def gourdsSearchingByIndex(self, x, y):
        # search if there is a pair of gourds on (x, y)
        for i in range(len(self.gourdsList)):
            if (x == self.gourdsList[i][0] and y == self.gourdsList[i][1]):
                return i, x, y
            if (x == self.gourdsList[i][2] and y == self.gourdsList[i][3]):
                return i, x, y
        return -1, -1, -1

    def emptyCellSearchingAroundAGourd(self, x, y):
        # obtain the size of the self.boardMatrix
        maxOfX = len(self.board[0]) - 1
        maxOfY = len(self.board) - 1

        # search an empty cell around x, y
        if x - 1 >= 0 and y - 1 >= 0:
            if (self.board[y - 1][x - 1] != 0) and (self.gourdsSearchingByIndex(x - 1, y - 1)[0] == -1):  # upper left
                return x - 1, y - 1
        if x - 1 >= 0 and y + 1 <= maxOfY:
            if (self.board[y + 1][x - 1] != 0) and (self.gourdsSearchingByIndex(x - 1, y + 1)[0] == -1):  # lower left
                return x - 1, y + 1
        if x + 1 <= maxOfX and y + 1 <= maxOfY:
            if (self.board[y + 1][x + 1] != 0) and (self.gourdsSearchingByIndex(x + 1, y + 1)[0] == -1):  # lower right
                return x + 1, y + 1
        if x + 1 <= maxOfX and y - 1 >= 0:
            if (self.board[y - 1][x + 1] != 0) and (self.gourdsSearchingByIndex(x + 1, y - 1)[0] == -1):  # upper right
                return x + 1, y - 1
        if x - 2 >= 0:
            if (self.board[y][x - 2] != 0) and (self.gourdsSearchingByIndex(x - 2, y)[0] == -1):  # left
                return x - 2, y
        if x + 2 <= maxOfX:
            if (self.board[y][x + 2] != 0) and (self.gourdsSearchingByIndex(x + 2, y)[0] == -1):  # right
                return x + 2, y
        return -1, -1

    def gourdsMovementController(self, indexOfGourd, xGourdClicked, yGourdClicked, xCell, yCell):

        # identify the clicked and linked parts of gourd
        if self.gourdsList[indexOfGourd][0] == xGourdClicked and self.gourdsList[indexOfGourd][1] == yGourdClicked:
            partIndex = 0
            firstPartClicked = True
            xGourdLinked = self.gourdsList[indexOfGourd][2]
            yGourdLinked = self.gourdsList[indexOfGourd][3]
        elif self.gourdsList[indexOfGourd][2] == xGourdClicked and self.gourdsList[indexOfGourd][3] == yGourdClicked:
            partIndex = 2
            firstPartClicked = False
            xGourdLinked = self.gourdsList[indexOfGourd][0]
            yGourdLinked = self.gourdsList[indexOfGourd][1]
        else:

            print("---WARN--- Something went wrong in gourdsMovement()")
            return -1, -1
        # move gourd
        print(1111)
        distanceSquare = ((xGourdLinked - xCell) ** 2) + (((yGourdLinked - yCell) * 1.732) ** 2)
        if distanceSquare < 4.3:  # pivot
            xGourdClicked = xCell
            yGourdClicked = yCell
            #record
            self.stackOfFootPrint.append([xCell, yCell])
        else:  # slide or turn
            xGourdLinked = xGourdClicked
            yGourdLinked = yGourdClicked
            xGourdClicked = xCell
            yGourdClicked = yCell
            # record
            self.stackOfFootPrint.append([xGourdLinked, yGourdLinked])

        # identify the clicked and linked parts and save
        if firstPartClicked:

            self.gourdsList[indexOfGourd][0] = xGourdClicked
            self.gourdsList[indexOfGourd][1] = yGourdClicked
            self.gourdsList[indexOfGourd][2] = xGourdLinked
            self.gourdsList[indexOfGourd][3] = yGourdLinked

        else:
            self.gourdsList[indexOfGourd][0] = xGourdLinked
            self.gourdsList[indexOfGourd][1] = yGourdLinked
            self.gourdsList[indexOfGourd][2] = xGourdClicked
            self.gourdsList[indexOfGourd][3] = yGourdClicked

        # finally refresh the whole self.board
        # cellsAndAxisConstructor()
        # gourdsConstructor()


        return indexOfGourd, partIndex # partIndex is 0 or 2

