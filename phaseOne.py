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
            self.HCycleAux.append(self.HCycleAux[i])

    def runPhaseOne(self, buttonState3):
        if buttonState3 != 2: # running
            self.firstRun = True
            return
        print("Phase one is running")

        #TODO


        i = 0

        # for i in range(len(self.myHamiltonianCycle.hamiltonianCycleStack)):

        # find a root in h-cycle
        rootIndex = self.theEmptyCellSearching()
        if (rootIndex == False):
            print("---WARN--- No empty cell found")
            return False

        # move the gourds
        self.gourdsMovement(rootIndex + i)



        self.myButtons.buttonStates[3] = 1 # finished
        self.redrawTheScreen()



    def theEmptyCellSearching(self):
        cellIndex = -1
        for aCell in self.myHamiltonianCycle.hamiltonianCycleStack:
            cellIndex +=1
            isEmpty = True
            for aGourds in self.myBoardsConfig.gourdsList:
                if (aCell[0] == aGourds[0] and aCell[1] == aGourds[1]):
                    isEmpty = False
                    break
                elif (aCell[0] == aGourds[2] and aCell[1] == aGourds[3]):
                    isEmpty = False
                    break
            if isEmpty:
                return cellIndex
        return False

    def gourdsMovement(self, index):
        index += 1
        # move first part
        gourdsIndex, partIndex = self.myGourdsConstructor.gourdsClicked(self.HCycleAux[index], 'al')
        if gourdsIndex is None:
            print ("---WARN--- No these gourds found!")
            return False
        # if the second part should be moved?




        print(partIndex)


        return

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

