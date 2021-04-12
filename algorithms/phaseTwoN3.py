import pygame

class phaseTwoN3(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig):
        self.screen = screen
        self.myBoardsConfig = myBoardsConfig
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.HCycleAux = self.myHamiltonianCycle.HCycleAux

    def runPhaseTwoN3(self, buttonState4):
        if buttonState4 != 2: # running
            self.firstRun = True
            return False

        if self.myButtons.buttonStates[3] != 1:
            self.myButtons.buttonStates[4] = 0
            print("Phase 1 should be finished first!")
            self.redrawTheScreen()
            return False
        print("Phase two O(n^3) is running")

        isFinishedFlag = False

        #search type two
        cellIndexInHCycle = self.searchLeafInTypeTwo()
        if cellIndexInHCycle != -1:
            isFinishedFlag = self.typeTwoBubbleSort()


        else:
            # search type one
            cellIndexInHCycle = self.searchLeafInTypeOne()
            if cellIndexInHCycle != -1:
                isFinishedFlag = self.typeOneInsertionSort()


        self.myButtons.buttonStates[4] = 1  # finished
        self.myButtons.buttonStates[5] = 1  # finished
        self.redrawTheScreen()
        if not isFinishedFlag: print("---WARN--- Something went wrong in Phase 2 O(n^3)!")
        return isFinishedFlag

    def searchLeafInTypeOne(self):
        HCycleIndex = -1
        #TODO




        return HCycleIndex

    def searchLeafInTypeTwo(self):
        HCycleIndex = -1
        #TODO
        return HCycleIndex

    def typeOneInsertionSort(self):
        #TODO

        # self.myGourdsConstructor.gourdsClicked([4, 2], 'al')
        return True

    def typeTwoBubbleSort(self):
        #TODO


        return True

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

