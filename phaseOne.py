import copy

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
        # make a copy of Hamiltonian Cycle and duplicate it
        self.HCycleAux = copy.deepcopy(self.myHamiltonianCycle.hamiltonianCycleStack)
        for i in range(len(self.HCycleAux)):
            self.HCycleAux.append(copy.deepcopy((self.HCycleAux[i])))

    def runPhaseOne(self, buttonState3):
        if buttonState3 != 2: # running
            self.firstRun = True
            return
        print("Phase one is running")



        # find the empty cell
        rootIndex = -1
        for aCell in self.myHamiltonianCycle.hamiltonianCycleStack:
            rootIndex += 1
            isEmpty, indexOfGourds = self.isCellEmpty(aCell)
            if isEmpty: break

        if rootIndex == -1:
            print("---WARN--- No empty cell found")
            return False



        # move the gourds
        for i in range(0, len(self.myHamiltonianCycle.hamiltonianCycleStack), 2):
            # print (self.HCycleAux[rootIndex + i])
            self.gourdsMovement(rootIndex + i)



        self.myButtons.buttonStates[3] = 1 # finished
        self.redrawTheScreen()



    def isCellEmpty(self, aCell):
        isEmpty = True
        gourdsIndex = -1
        for aGourds in self.myBoardsConfig.gourdsList:
            gourdsIndex += 1
            if (aCell[0] == aGourds[0] and aCell[1] == aGourds[1]):
                isEmpty = False
                break
            elif (aCell[0] == aGourds[2] and aCell[1] == aGourds[3]):
                isEmpty = False
                break
        if isEmpty:
            return True, -1
        return False, gourdsIndex

    def gourdsMovement(self, HCycleIndex):
        print(HCycleIndex + 1)
        print(self.HCycleAux[HCycleIndex + 1])



        isEmpty, indexOfGourds = self.isCellEmpty(self.HCycleAux[HCycleIndex])
        if not isEmpty:

            if (self.myBoardsConfig.gourdsList[indexOfGourds][0] == self.HCycleAux[HCycleIndex][0]
                    and self.myBoardsConfig.gourdsList[indexOfGourds][1] == self.HCycleAux[HCycleIndex][1]):
                # is the first part
                # click the second part
                theNextPart = self.myBoardsConfig.gourdsList[indexOfGourds][2], self.myBoardsConfig.gourdsList[indexOfGourds][3]
            else:
                # is the second part
                # click the first part
                theNextPart = self.myBoardsConfig.gourdsList[indexOfGourds][0], self.myBoardsConfig.gourdsList[indexOfGourds][1]

            self.myGourdsConstructor.gourdsClicked(theNextPart, 'al')
            return


        # move first part
        HCycleIndex += 1
        gourdsIndex, partIndex = self.myGourdsConstructor.gourdsClicked(self.HCycleAux[HCycleIndex], 'al')
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


        # print(partIndex)


        return

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

