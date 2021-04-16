import pygame
class phaseTwoN2(object):

    def __init__(self, screen, myBoardsConfig, myButtons, myCellsConstructor, myGourdsConstructor, myHamiltonianCycle, myFinalGourdsConfig, myFinalHCycleOrderConfig):
        self.screen = screen
        self.myBoardsConfig = myBoardsConfig
        self.myButtons = myButtons
        self.myCellsConstructor = myCellsConstructor
        self.myGourdsConstructor = myGourdsConstructor
        self.myHamiltonianCycle = myHamiltonianCycle
        self.myFinalGourdsConfig = myFinalGourdsConfig
        self.myFinalHCycleOrderConfig = myFinalHCycleOrderConfig


    def runPhaseTwoN2(self, buttonState5):
        if buttonState5 != 2: # running
            self.firstRun = True
            return

        if self.myButtons.buttonStates[3] != 1:
            self.myButtons.buttonStates[5] = 0
            print("Phase 1 should be finished first!")
            self.redrawTheScreen()
            return False

        print("Phase two O(n^2) is running")

        #TODO

        self.myButtons.buttonStates[4] = 1  # finished
        self.myButtons.buttonStates[5] = 1  # finished
        self.myGourdsConstructor.gourdsClicked([ 4, 2], 'al')
        self.redrawTheScreen()



    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

