import copy

import pygame

class phaseTwoN3(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig, myFinalHCycleOrderConfig):
        self.screen = screen
        self.myBoardsConfig = myBoardsConfig
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.myFinalHCycleOrderConfig = myFinalHCycleOrderConfig

        self.HCycleAux = self.myHamiltonianCycle.HCycleAux
        self.firstRunFlag = True
        self.gourdsFinalOrderInHCycle = myFinalHCycleOrderConfig.gourdsFinalOrderInHCycle
        self.leafType = -1
        self.leafIndex = -1

    def runPhaseTwoN3(self, buttonState4):
        if buttonState4 != 2: # running
            return False

        if self.myButtons.buttonStates[3] != 1:
            self.myButtons.buttonStates[4] = 0
            print("Phase 1 should be finished first!")
            self.redrawTheScreen()
            return False


        print("Phase two O(n^3) is running")

        result = False


        # gourdsOrderInHCycleGenerator
        if len(self.gourdsFinalOrderInHCycle) <= 0:
            self.gourdsFinalOrderInHCycleGetter()


        # search type two
        cellIndexInHCycle = self.searchLeafInTypeTwo()
        if cellIndexInHCycle != -1:
            self.leafType = 2
            result = self.typeTwoBubbleSort(cellIndexInHCycle)


        else:
            # search type one
            cellIndexInHCycle = self.searchLeafInTypeOne()
            if cellIndexInHCycle != -1:
                self.leafType = 2
                print("\t", self.HCycleAux[cellIndexInHCycle], "is the x of leaf type one")
                result = self.typeOneInsertionSort(cellIndexInHCycle)



        self.myButtons.buttonStates[4] = 1  # finished
        self.myButtons.buttonStates[5] = 1  # finished
        self.redrawTheScreen()
        if not result: print("---WARN--- Something went wrong in Phase 2 O(n^3)!")
        return result

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

    def gourdsOrderedWithOffset(self):
        # measure the offset
        presentGourdsOrder = self.gourdsPresentOrderInHCycleGetter()
        offset = 0
        for i in range(len(presentGourdsOrder)):
            if presentGourdsOrder[i] == self.gourdsFinalOrderInHCycle[0]:
                offset = i
                break
        # check if the offset valid
        duplicatePresentGourdsOrder = presentGourdsOrder * 2
        result = True
        for i in range(len(presentGourdsOrder)):
            if not duplicatePresentGourdsOrder[i + offset] == self.gourdsFinalOrderInHCycle[i]:
                result = False

                break
        return result

    def searchLeafInTypeOne(self):
        HCycleIndex = -1

        # calculate the distance between i+0 and i+3
        for i in range(self.myHamiltonianCycle.lengthOfHCycle):
            diffInX = self.HCycleAux[i][0] - self.HCycleAux[i+3][0]
            diffInY = self.HCycleAux[i][1] - self.HCycleAux[i+3][1]
            squaredDistance = diffInX * diffInX + diffInY * diffInY * 1.732 * 1.732
            if squaredDistance <= 4:
                return i

        return HCycleIndex

    def searchLeafInTypeTwo(self):
        HCycleIndex = -1


        for i in range(self.myHamiltonianCycle.lengthOfHCycle):
            # calculate the distance between i+0 and i+2
            diffInX = self.HCycleAux[i][0] - self.HCycleAux[i + 2][0]
            diffInY = self.HCycleAux[i][1] - self.HCycleAux[i + 2][1]
            squaredDistance = diffInX * diffInX + diffInY * diffInY * 1.732 * 1.732
            if squaredDistance <= 4:
                # calculate the distance between i+0 and i+4
                diffInX = self.HCycleAux[i][0] - self.HCycleAux[i + 4][0]
                diffInY = self.HCycleAux[i][1] - self.HCycleAux[i + 4][1]
                squaredDistance = diffInX * diffInX + diffInY * diffInY * 1.732 * 1.732
                if squaredDistance <= 4:
                    # calculate the distance between i+2 and i+4
                    diffInX = self.HCycleAux[i + 2][0] - self.HCycleAux[i + 4][0]
                    diffInY = self.HCycleAux[i + 2][1] - self.HCycleAux[i + 4][1]
                    squaredDistance = diffInX * diffInX + diffInY * diffInY * 1.732 * 1.732
                    if squaredDistance <= 4:
                        return i

        return HCycleIndex

    def typeOneInsertionSort(self, cellIndexInHCycle):
        # this is not really an Insertion Sort, it just an Insertion Sort-like algorithms
        #TODO
        # init
        HCycleDup = self.myHamiltonianCycle.hamiltonianCycleStack * 2
        HPrimeCycleDup = copy.copy(self.myHamiltonianCycle.hamiltonianCycleStack)
        HPrimeCycleDup.pop(cellIndexInHCycle + 2)
        HPrimeCycleDup.pop(cellIndexInHCycle + 1)
        HPrimeCycleDup = HPrimeCycleDup * 2
        print("\tThe order of gourds now: ", self.gourdsPresentOrderInHCycleGetter())



        while(True):
            presentGourdsOrder = self.gourdsPresentOrderInHCycleGetter()
            # already done?
            if(self.gourdsFinalOrderInHCycle == presentGourdsOrder):
                print("\tThe order of gourds now: ", self.gourdsPresentOrderInHCycleGetter())

                return True
            lenOfACycle = int(len(HCycleDup) / 2)


            # check if there's an offset, if true, then move gourds counter-clock-wise
            if self.gourdsOrderedWithOffset():

                for counter in range(lenOfACycle):
                    self.movesAllGourdsCClockwiseAlongACycle(HCycleDup)


            # insertion
            # Ensure Gourds In Proper Places
            self.typeOneEnsureGourdsInProperPlaces(HCycleDup, cellIndexInHCycle, HPrimeCycleDup)


            gourdsIndexAtXPlusOne = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 1][0], HCycleDup[cellIndexInHCycle + 1][1])[0]
            gourdsIndexAtXPlusZero = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 0][0], HCycleDup[cellIndexInHCycle + 0][1])[0]

            gourdsIndexShouldNextToXPlusOne = -1
            for i in range(lenOfACycle):
                if gourdsIndexAtXPlusOne == self.gourdsFinalOrderInHCycle[i]:
                    gourdsIndexShouldNextToXPlusOne = self.gourdsFinalOrderInHCycle[i-1]
                    break

            while not (gourdsIndexAtXPlusZero == gourdsIndexShouldNextToXPlusOne):
                self.movesAllGourdsCClockwiseAlongACycle(HPrimeCycleDup)
                gourdsIndexAtXPlusZero = \
                self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 0][0],
                                                                HCycleDup[cellIndexInHCycle + 0][1])[0]

            self.typeOneEnsureGourdsInProperPlaces(HCycleDup, cellIndexInHCycle, HPrimeCycleDup)
            for i in range(lenOfACycle):
                self.movesAllGourdsCClockwiseAlongACycle(HCycleDup)

            print("\tThe order of gourds now: ", self.gourdsPresentOrderInHCycleGetter())

        return True

    def typeTwoBubbleSort(self, cellIndexInHCycle):
        # this is also not really a Bubble Sort, it just a Bubble Sort-like algorithm.
        #TODO


        return True

    def typeOneEnsureGourdsInProperPlaces(self, HCycleDup, cellIndexInHCycle, HPrimeCycleDup):
        # moves a pair of gourds into the leaf (x+1) and (x+2)
        tempOne = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 1][0],
                                                                  HCycleDup[cellIndexInHCycle + 1][1])
        tempTwo = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 2][0],
                                                                  HCycleDup[cellIndexInHCycle + 2][1])
        while not (tempOne[0] == tempTwo[0]):
            self.movesAllGourdsCClockwiseAlongACycle(HCycleDup)

            tempOne = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 1][0],
                                                                      HCycleDup[cellIndexInHCycle + 1][1])
            tempTwo = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 2][0],
                                                                      HCycleDup[cellIndexInHCycle + 2][1])

        # make sure not a pair of gourds outside the leaf (x+1) and (x+2)
        tempOne = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 0][0],
                                                                  HCycleDup[cellIndexInHCycle + 0][1])
        tempTwo = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 3][0],
                                                                  HCycleDup[cellIndexInHCycle + 3][1])
        while (tempOne[0] == tempTwo[0]):
            self.movesAllGourdsCClockwiseAlongACycle(HPrimeCycleDup)

            tempOne = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 0][0],
                                                                      HCycleDup[cellIndexInHCycle + 0][1])
            tempTwo = self.myGourdsConstructor.gourdsSearchingByIndex(HCycleDup[cellIndexInHCycle + 3][0],
                                                                      HCycleDup[cellIndexInHCycle + 3][1])

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

