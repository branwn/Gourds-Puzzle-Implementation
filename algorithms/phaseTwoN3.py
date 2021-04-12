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


        #TODO
        leafType, HCycleIndex = self.findTheLeaves()
        if leafType == -1:
            print("---WARN--- Cannot find a leaf!")
            return False

        if leafType == 1:
            self.typeOneInsertionSort()

        elif leafType == 2:
            self.typeTwoBubbleSort()



        self.myButtons.buttonStates[4] = 1  # finished
        self.myButtons.buttonStates[5] = 1  # finished
        self.redrawTheScreen()
        return True

    def findTheLeaves(self):
        type = -1
        HCycleIndex = -1


        return type, HCycleIndex



    def typeOneInsertionSort(self):
        #TODO

        self.myGourdsConstructor.gourdsClicked([4, 2], 'a')
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

