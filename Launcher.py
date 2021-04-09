import pygame

from boardConfigsContainer import boardConfig4 as boardConfig
from buttons import buttons
from cellsConstructor import cellsConstructor
from gourdsConstructor import gourdsConstructor
from hamiltonianCycle import hamiltonianCycle
from finalGourdsConfigGenerator import finalGourdsConfig



# set size of the window
xLengthOfTheWindow = int(len(boardConfig.board[0])*50 + 250)
yLengthOfTheWindow = int(len(boardConfig.board)*90 + 50)
sizeOfTheWindow = (xLengthOfTheWindow, yLengthOfTheWindow)
# button size
buttonSize = 200, 30
# widthOfHexCells
widthOfHexCell = -1
# offset
offset = -1
# gourd size
gourdSize = -1


# first run flag
runFirstTimeFlag = True

pygame.init()
# size of the window
screen = pygame.display.set_mode(sizeOfTheWindow)
# caption setting
pygame.display.set_caption('Gourds')


def mouseClicked(pos):
    # search Gourds by the given Coordinate
    indexOfGourd, xGourd, yGourd = myGourdsConstructor.gourdsSearchingByCoordinate(pos)
    if indexOfGourd != -1:
        # print(xGourd, yGourd)
        # search if there is an Empty Cell Around
        xCell, yCell = myGourdsConstructor.emptyCellSearchingAroundAGourd(xGourd, yGourd)
        if xCell != -1:
            # move gourd to the empty cell
            myGourdsConstructor.gourdsMovementController(indexOfGourd, xGourd, yGourd, xCell, yCell)
            # finally refresh the cells and gourds
            redrawTheScreen()
            return 0

        redrawTheScreen()
        return 0

    # search button by the given coordinate
    if myButtons.buttonsClicked(pos) != -1:

        redrawTheScreen()
        return 0

    return -1;


def redrawTheScreen():

    screen.fill(myBoardsConfig.coloursLibrary['backGround'])
    myButtons.buttonConstructor()
    myCellsConstructor.cellsAndAxisConstructor(myButtons.buttonStates[1])
    myGourdsConstructor.gourdsConstructor(myButtons.buttonStates[1])
    myHamiltonianCycle.hamiltonianCycleDrawer(myButtons.buttonStates[2])


    pygame.display.update()


def main():
    # initialization
    global myBoardsConfig
    myBoardsConfig = boardConfig();


    # parameters init
    global widthOfHexCell, offset, gourdSize


    # set width of the hexagonal cell
    if (sizeOfTheWindow[0] - buttonSize[0]) / (len(myBoardsConfig.board[0])) <= sizeOfTheWindow[1] / 1.732 / (len(myBoardsConfig.board)):
        widthOfHexCell = int((sizeOfTheWindow[0] - buttonSize[0]) / (len(myBoardsConfig.board[0]) + 2))
    else:
        widthOfHexCell = int(sizeOfTheWindow[1] / 1.732 / (len(myBoardsConfig.board) + 1))
    offset = widthOfHexCell * 1.5
    # gourd size
    gourdSize = int(widthOfHexCell * 0.35)

    # objects init
    global myButtons
    myButtons = buttons(screen, myBoardsConfig.coloursLibrary, sizeOfTheWindow, buttonSize)

    global myCellsConstructor
    myCellsConstructor = cellsConstructor(screen, myBoardsConfig.board, myBoardsConfig.coloursLibrary, offset, widthOfHexCell)

    global myGourdsConstructor
    myGourdsConstructor = gourdsConstructor(screen, myBoardsConfig.board, myBoardsConfig.gourdsList, myBoardsConfig.coloursLibrary, offset, widthOfHexCell, gourdSize)

    global myHamiltonianCycle
    myHamiltonianCycle = hamiltonianCycle(screen, myBoardsConfig.board, myBoardsConfig.coloursLibrary, offset, widthOfHexCell)

    global myFinalGourdsConfig
    myFinalGourdsConfig = finalGourdsConfig(screen, myBoardsConfig.board, myBoardsConfig.gourdsList, myBoardsConfig.coloursLibrary, offset, widthOfHexCell)
    myFinalGourdsConfig.finalConfigGenerator()

    # flag setting
    global runFirstTimeFlag
    runFirstTimeFlag = False



    redrawTheScreen()
    pygame.display.update()

    # main loop
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pass

            # MOUSE BUTTON DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # MOUSE BUTTON UP
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClicked(event.pos)
                pass
    exit()


if __name__ == '__main__':
    main()
