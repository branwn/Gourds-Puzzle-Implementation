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
        self.firstRun = True

    def runPhaseOne(self, buttonState3):
        if buttonState3 != 2: # running
            self.firstRun = True
            return
        if not self.firstRun: return
        self.firstRun = False
        self.myButtons.buttonStates[3] = 1 # finished


        self.myGourdsConstructor.gourdsClicked([ 4, 2], 'a')
        self.redrawTheScreen()

        print("run phase one")

    def redrawTheScreen(self):

        self.screen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])

        pygame.display.update()

