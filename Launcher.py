import pygame
import numpy

from boardConfig import boardsConfig
from buttons import buttons
from cells import cells
from gourds import gourds
from hamiltonianCycle import hamiltonianCycle




# colour library
coloursLibrary = {
    'backGround': (242, 242, 242),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'hamiltonianCycle': (39, 98, 184),
    1: (190, 127, 73),
    2: (80, 193, 233),
    3: (122, 87, 209),
    4: (237, 84, 133),
    5: (255, 232, 105),
    6: (91, 231, 196),
}


# objects
myBoard = None
myGourdsList = None

myButtons = None
myCells = None
myGourds = None
myHamiltonianCycle = None



# size of the window
sizeOfTheWindow = (600, 400)
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
# background colour setting
screen.fill(coloursLibrary['backGround'])



def mouseClicked(pos):
    # search Gourds by the given Coordinate
    indexOfGourd, xGourd, yGourd = myGourds.gourdsSearchingByCoordinate(pos)
    if indexOfGourd != -1:
        # print(xGourd, yGourd)
        # search if there is an Empty Cell Around
        xCell, yCell = myGourds.emptyCellSearchingAroundAGourd(xGourd, yGourd)
        if xCell != -1:
            # move gourd to the empty cell
            myGourds.gourdsMovementController(indexOfGourd, xGourd, yGourd, xCell, yCell)
            # finally refresh the cells and gourds
            redrawTheScreen()
            return 0

        redrawTheScreen()
        return 0

    # search button by the given coordinate
    if myButtons.buttonsSearchingByCoordinate(pos) != -1:

        redrawTheScreen()
        return 0

    return -1;


def redrawTheScreen():

    screen.fill(coloursLibrary['backGround'])
    myButtons.buttonConstructorAndPainter()
    myCells.cellsAndAxisConstructor(myButtons.buttonStates[1])
    myGourds.gourdsConstructor(myButtons.buttonStates[1])
    myHamiltonianCycle.hamiltonianCycleDrawer(myButtons.buttonStates[2])
    pygame.display.update()


def main():
    # initialization
    global myBoardsConfig
    myBoardsConfig = boardsConfig();


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
    myButtons = buttons(screen, coloursLibrary, sizeOfTheWindow, buttonSize)

    global myCells
    myCells = cells(screen, myBoardsConfig.board, coloursLibrary, offset, widthOfHexCell)

    global myGourds
    myGourds = gourds(screen, myBoardsConfig.board, myBoardsConfig.gourdsList, coloursLibrary, offset, widthOfHexCell, gourdSize)

    global myHamiltonianCycle
    myHamiltonianCycle = hamiltonianCycle(screen, myBoardsConfig.board, coloursLibrary, offset, widthOfHexCell)


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
