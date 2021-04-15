import pygame


class phaseOne(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig):
        self.screen = screen
        self.myBoardsConfig = myBoardsConfig
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.HCycleAux = self.myHamiltonianCycle.HCycleAux

    def runPhaseOne(self, buttonState3):
        if buttonState3 != 2: # running
            self.firstRun = True
            return
        print("Phase one is running")

        # show the H-Cycle
        self.myButtons.buttonStates[2] = 1
        self.redrawTheScreen()

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

            self.gourdsMovementController(rootIndex)


        print("Phase one finished!")
        self.myButtons.buttonStates[3] = 1 # finished
        self.redrawTheScreen()

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


        gourdsIndex, partIndex  = self.myGourdsConstructor.gourdsClicked(self.HCycleAux[HCycleIndex], 'al')
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
            self.myGourdsConstructor.gourdsClicked(nextPartofGourds, 'al')

    def gourdsMovementController(self, HCycleIndex):
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

            self.myGourdsConstructor.gourdsClicked(theNextPart, 'al')
            self.redrawTheScreen()
            return True


        self.movesAloneTheHCycle(HCycleIndex)

        # print(partIndex)

        self.redrawTheScreen()
        return True

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

