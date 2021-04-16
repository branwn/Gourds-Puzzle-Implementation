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
















        self.myButtons.buttonStates[6] = 1 # finished
        self.myGourdsConstructor.gourdsClicked([ 4, 2], 'al')
        self.redrawTheScreen()



    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

