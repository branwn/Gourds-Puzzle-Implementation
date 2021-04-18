import pygame

from algorithms.finalHCycleOrderGenerator import finalHCycleOrderGenerator
from boardConfigsContainer import boardsContainer
from boardConstructor.buttonsForBoard import buttons
from boardConstructor.cellsConstructor import cellsConstructor
from boardConstructor.gourdsConstructor import gourdsConstructor
from algorithms.hamiltonianCycle import hamiltonianCycle
from algorithms.finalGourdsConfigGenerator import finalGourdsConfig



# set size of the window
from algorithms.phaseOne import phaseOne
from algorithms.phaseThree import phaseThree
from algorithms.phaseTwoN2 import phaseTwoN2
from algorithms.phaseTwoN3 import phaseTwoN3


class board(object):
    def __init__(self):
        pass



    def mouseClicked(self, pos):
        if self.myGourdsConstructor.gourdsClicked(pos, 'm')[0] != -1:
            # reset the algorithms states
            self.myButtons.buttonStates[3] = 0
            self.myButtons.buttonStates[4] = 0
            self.myButtons.buttonStates[5] = 0
            self.myButtons.buttonStates[6] = 0

            self.redrawTheScreen()
            return 0

        # search button by the given coordinate
        if self.myButtons.buttonsClicked(pos) != -1:

            self.redrawTheScreen()
            return 0

        return -1;


    def redrawTheScreen(self):
        if not self.myButtons.buttonStates[8] == 0: return

        self.boardScreen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(self.myButtons.buttonStates[1])
        self.myGourdsConstructor.gourdsConstructor(self.myButtons.buttonStates[1])
        self.myHamiltonianCycle.hamiltonianCycleDrawer(self.myButtons.buttonStates[2])
        self.myPhaseOne.runPhaseOne(self.myButtons.buttonStates[3])
        self.myPhaseTwoN3.runPhaseTwoN3(self.myButtons.buttonStates[4])
        self.myPhaseTwoN2.runPhaseTwoN2(self.myButtons.buttonStates[5])
        self.myPhaseThree.runPhaseThree(self.myButtons.buttonStates[6])


        pygame.display.update()


    def main(self, indexOfBoard):
        # initialization
        self.myBoardContainer = boardsContainer()
        self.boardConfig = self.myBoardContainer.container[indexOfBoard]

        xLengthOfTheWindow = int(len(self.boardConfig.board[0]) * 50 + 250)
        yLengthOfTheWindow = int(len(self.boardConfig.board) * 90 + 60)
        self.sizeOfTheWindow = (xLengthOfTheWindow, yLengthOfTheWindow)
        # button size
        self.buttonSize = 200, 30
        # widthOfHexCells
        self.widthOfHexCell = -1
        # offset
        self.offset = -1
        # gourd size
        self.gourdSize = -1

        # first run flag
        self.runFirstTimeFlag = True

        pygame.init()
        # size of the window
        self.boardScreen = pygame.display.set_mode(self.sizeOfTheWindow)
        # caption setting
        pygame.display.set_caption('Board')


        self.myBoardsConfig = self.boardConfig();


        # parameters init
        self.widthOfHexCell, self.offset, self.gourdSize


        # set width of the hexagonal cell
        if (self.sizeOfTheWindow[0] - self.buttonSize[0]) / (len(self.myBoardsConfig.board[0])) <= self.sizeOfTheWindow[1] / 1.732 / (len(self.myBoardsConfig.board)):
            self.widthOfHexCell = int((self.sizeOfTheWindow[0] - self.buttonSize[0]) / (len(self.myBoardsConfig.board[0]) + 2))
        else:
            self.widthOfHexCell = int(self.sizeOfTheWindow[1] / 1.732 / (len(self.myBoardsConfig.board) + 1))
        self.offset = self.widthOfHexCell * 1.5
        # gourd size
        self.gourdSize = int(self.widthOfHexCell * 0.35)

        # objects init

        self.myButtons = buttons(self.boardScreen, self.myBoardsConfig.coloursLibrary, self.sizeOfTheWindow, self.buttonSize)


        self.myCellsConstructor = cellsConstructor(self.boardScreen, self.myBoardsConfig.board, self.myBoardsConfig.coloursLibrary, self.offset, self.widthOfHexCell)


        self.myGourdsConstructor = gourdsConstructor(self.boardScreen, self.myBoardsConfig.board, self.myBoardsConfig.gourdsList, self.myBoardsConfig.coloursLibrary, self.offset, self.widthOfHexCell, self.gourdSize)

        self.myHamiltonianCycle = hamiltonianCycle(self.boardScreen, self.myBoardsConfig.board, self.myBoardsConfig.coloursLibrary, self.offset, self.widthOfHexCell)
        self.myHamiltonianCycle.hamiltonianCycleGenerator()

        self.myFinalGourdsConfig = finalGourdsConfig(self.boardScreen, self.myBoardsConfig.board, self.myBoardsConfig.gourdsList, self.myBoardsConfig.coloursLibrary, self.offset, self.widthOfHexCell)
        self.myFinalGourdsConfig.finalConfigGenerator()

        self.myFinalHCycleOrderConfig = finalHCycleOrderGenerator(self.boardScreen, self.myBoardsConfig, self.myButtons, self.myCellsConstructor, self.myGourdsConstructor, self.myHamiltonianCycle, self.myFinalGourdsConfig)
        self.myFinalHCycleOrderConfig.runFinalHCycleOrderGenerator()

        self.myPhaseOne = phaseOne(self.boardScreen, self.myBoardsConfig, self.myButtons, self.myCellsConstructor, self.myGourdsConstructor, self.myHamiltonianCycle, self.myFinalGourdsConfig)

        self.myPhaseTwoN3 = phaseTwoN3(self.boardScreen, self.myBoardsConfig, self.myButtons, self.myCellsConstructor, self.myGourdsConstructor, self.myHamiltonianCycle, self.myFinalGourdsConfig, self.myFinalHCycleOrderConfig)

        self.myPhaseTwoN2 = phaseTwoN2(self.boardScreen, self.myBoardsConfig, self.myButtons, self.myCellsConstructor, self.myGourdsConstructor, self.myHamiltonianCycle, self.myFinalGourdsConfig, self.myFinalHCycleOrderConfig)

        self.myPhaseThree = phaseThree(self.boardScreen, self.myBoardsConfig, self.myButtons, self.myCellsConstructor, self.myGourdsConstructor, self.myHamiltonianCycle, self.myFinalGourdsConfig, self.myFinalHCycleOrderConfig)


        # flag setting

        self.runFirstTimeFlag = False



        self.redrawTheScreen()
        pygame.display.update()

        # main loop
        running = True
        while running:

            if not self.myButtons.buttonStates[8] == 0: return


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pass

                # MOUSE BUTTON DOWN
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # MOUSE BUTTON UP
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouseClicked(event.pos)
                    pass
        exit()



