import pygame

from boardConfigsContainer import boardsContainer
from boardConstructor.buttonsForSwitcher import buttons
from boardConstructor.cellsConstructor import cellsConstructor
from boardConstructor.Board import board




class boardsSwitcher(object):
    def __init__(self):


        self.indexOfBoard = 0

    def mouseClicked(self, pos):

        # search button by the given coordinate
        if self.myButtons.buttonsClicked(pos) != -1:

            self.redrawTheScreen()
            return 0

        return -1;

    def redrawTheScreen(self):
        self.runBoard()
        self.boardChanging()
        self.boardScreen.fill(self.myBoardsConfig.coloursLibrary['backGround'])
        self.myButtons.buttonConstructor()
        self.myCellsConstructor.cellsAndAxisConstructor(1)

        pygame.display.update()

    def boardChanging(self):
        if self.myButtons.buttonStates[1] == 2:
            if self.indexOfBoard - 1 >= 0:
                self.indexOfBoard -= 1


        if self.myButtons.buttonStates[2] == 2:
            if self.indexOfBoard + 1 < len(self.myBoardContainer.container) :
                self.indexOfBoard += 1

        self.myButtons.buttonStates[1] = 0
        self.myButtons.buttonStates[2] = 0

    def runBoard(self):
        if not self.myButtons.buttonStates[8] == 0:
            self.myButtons.buttonStates[8] = 2
            myBoard = board()
            myBoard.main(self.indexOfBoard)
            del myBoard
        self.myButtons.buttonStates[8] = 0

    def main(self):
        # main loop
        running = True
        while running:

            # initialization
            self.myBoardContainer = boardsContainer()
            self.boardConfig = self.myBoardContainer.container[self.indexOfBoard]


            self.sizeOfTheWindow = (600, 330)
            # button size
            self.buttonSize = 100, 30
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
            caption = "Board Switcher    ( Index = "+ str(self.indexOfBoard) + " )"
            pygame.display.set_caption(caption)


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


            # flag setting

            self.runFirstTimeFlag = False



            self.redrawTheScreen()
            pygame.display.update()


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



