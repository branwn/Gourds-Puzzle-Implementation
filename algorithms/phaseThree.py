import copy

import pygame
class phaseThree(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig, myFinalHCycleOrderConfig):
        self.screen = screen
        self.myBoardsConfig = myBoardsConfig
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.myFinalHCycleOrderConfig = myFinalHCycleOrderConfig
        # init
        self.gourdsFinalOrderInHCycle = myFinalHCycleOrderConfig.gourdsFinalOrderInHCycle
        self.HCycleDup = self.myHamiltonianCycle.hamiltonianCycleStack * 2
        self.lenOfACycle = int(len(self.HCycleDup) / 2)

    def runPhaseThree(self, buttonState6):
        if buttonState6 != 2: # running
            self.firstRun = True
            return
        if self.myButtons.buttonStates[4] != 1:
            self.myButtons.buttonStates[6] = 0
            print("Phase 2 should be finished first!")
            self.redrawTheScreen()
            return False

        print("Phase three is running")

        #TODO

        isTheFinalOrder = self.gourdsFinalOrderInHCycleGetter() == self.gourdsPresentOrderInHCycleGetter()
        emptyCellAtAProperPlace = self.isCellEmpty(self.HCycleDup[self.myFinalHCycleOrderConfig.emptyCellIndex])[0]


        # ensure the empty cell is at a proper place, if not true, then move gourds counter-clock-wise
        while not (emptyCellAtAProperPlace and isTheFinalOrder):

            self.movesAllGourdsCClockwiseAlongACycle(self.HCycleDup)

            isTheFinalOrder = self.gourdsFinalOrderInHCycleGetter() == self.gourdsPresentOrderInHCycleGetter()
            emptyCellAtAProperPlace = self.isCellEmpty(self.HCycleDup[self.myFinalHCycleOrderConfig.emptyCellIndex])[0]



        # go back-ward
        footPrintAux = copy.deepcopy(self.myFinalHCycleOrderConfig.stackOfFootPrint)
        while len(footPrintAux) > 0 :
            self.myGourdsConstructor.gourdsClicked(footPrintAux.pop(), 'al')


        # print(footPrintAux)


        self.myButtons.buttonStates[6] = 1  # finished
        self.myButtons.buttonStates[2] = 0  # hidden the H-Cycle
        self.redrawTheScreen()


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

    def movesAllGourdsCClockwiseAlongACycle(self, aCycleDup):
        lenOfACycle = int(len(aCycleDup) / 2)

        for i in range(lenOfACycle):
            if self.isCellEmpty(aCycleDup[i])[0]:
                self.movesAGourdAloneTheACycle(aCycleDup, i)
                break

    def movesAGourdAloneTheACycle(self, aCycleDup, cycleIndex):

        # move first part
        cycleIndex += 1
        gourdsIndex, partIndex = self.myGourdsConstructor.gourdsClicked(aCycleDup[cycleIndex], 'al')
        if gourdsIndex == -1:
            print ("---WARN--- No these gourds found!")
            return False

        # check if the next part is along the HCycle
        if (self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex] == aCycleDup[cycleIndex][0]
                and self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex+1] == aCycleDup[cycleIndex][1]):
            # is along the HCycle
            pass
        else:
            # is not along the HCycle
            nextPartofGourds = self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex], self.myBoardsConfig.gourdsList[gourdsIndex][2-partIndex+1]
            # move the next part
            self.myGourdsConstructor.gourdsClicked(nextPartofGourds, 'al')

        self.redrawTheScreen()

    def gourdsFinalOrderInHCycleGetter(self):
        return self.gourdsFinalOrderInHCycle

    def gourdsPresentOrderInHCycleGetter(self):
        order = []
        for cell in self.myHamiltonianCycle.hamiltonianCycleStack:
            for i in range(self.myFinalGourdsConfig.totalNumberOfGourds):
                if i not in order:
                    gourd = self.myBoardsConfig.gourdsList[i]
                    if gourd[0] == cell[0] and gourd[1] == cell[1]:
                        order.append(i)
                        break
                    elif gourd[2] == cell[0] and gourd[3] == cell[1]:
                        order.append(i)
                        break

        return order

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

