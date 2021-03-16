import pygame
import numpy  # for matrix

displayIndexOnTheScreen = False

# set a matrix of board
board = numpy.array([
    # x  0, 1, 2, 3, 4, 5, 6, 7, 8
    [0, 4, 0, 4, 0, 1, 0],  # 0
    [2, 0, 2, 0, 3, 0, 2],  # 1
    [0, 1, 0, 1, 0, 1, 0],  # 2
    [2, 0, 2, 0, 3, 0, 0],  # 3
])

# set a initial gourds placement
gourdsList = numpy.array([
    # x, y, x, y, colourLib_1, colourLib_2
    [1, 0, 0, 1, 4, 2],
    [2, 1, 4, 1, 4, 3],
    [1, 2, 3, 2, 1, 2],
    [0, 3, 2, 3, 3, 1],
    [4, 3, 5, 2, 2, 1],
    [5, 0, 6, 1, 2, 2]
])

# colour dictionary
coloursLibrary = {
    'backGround': (242, 242, 242),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    1: (190, 127, 73),
    2: (80, 193, 233),
    3: (122, 87, 209),
    4: (237, 84, 133),
    5: (255, 232, 105),
    6: (91, 231, 196),
}

# button states
buttonStates = [0, 0, 0, 0, 0, 0, 0]  # 0 by default

# Hamiltonian Cycle Storage
totalNumberOfCells = 0
hamiltonianCycleRoot = -1, -1
hamiltonianCycleMap = numpy.zeros_like(board) # 1 for right hand side, and count in clockwise



# size of the window
sizeOfTheWindow = (600, 400)
# button size
buttonSize = 200, 30
# set width of the hexagonal cell
if (sizeOfTheWindow[0] - buttonSize[0]) / (len(board[0])) <= sizeOfTheWindow[1] / 1.732 / (len(board)):
    widthOfHexCell = int((sizeOfTheWindow[0] - buttonSize[0]) / (len(board[0]) + 2))
else:
    widthOfHexCell = int(sizeOfTheWindow[1] / 1.732 / (len(board) + 1))
offset = widthOfHexCell * 1.5
# gourd size
gourdSize = int(widthOfHexCell * 0.3)
# first run flag
runFirstTimeFlag = True

pygame.init()
# size of the window
screen = pygame.display.set_mode(sizeOfTheWindow)
# caption setting
pygame.display.set_caption('Gourds')
# background colour setting
screen.fill(coloursLibrary['backGround'])


# for algorithm Hamiltonian Cycle seeking


def searchNeighbourCells(cellIn):
    x = cellIn[0]
    y = cellIn[1]
    # obtain the size of the boardMatrix
    maxOfX = len(board[0]) - 1
    maxOfY = len(board) - 1

    results = []# (x, y, from, to)
    # search neighbour cells around the cellIn
    # know the neighbour x, y, from but not know where to go(set as default 0)
    if x + 2 <= maxOfX:
        if (board[y][x + 2] != 0):  # From Left 1 to right 4
            results.append([x + 2, y, 1, 0])
    if x + 1 <= maxOfX and y + 1 <= maxOfY:
        if (board[y + 1][x + 1] != 0):  # from upper left 2 to lower right 5
            results.append([x + 1, y + 1, 2, 0])
    if x - 1 >= 0 and y + 1 <= maxOfY:
        if (board[y + 1][x - 1] != 0):  # from upper right 3 to lower left 6
            results.append([x - 1, y + 1, 3, 0])
    if x - 2 >= 0:
        if (board[y][x - 2] != 0):  # from right 4 to left 1
            results.append  ([x - 2, y, 4, 0])
    if x - 1 >= 0 and y - 1 >= 0:
        if (board[y - 1][x - 1] != 0):  # from lower right 5 to upper left 2
            results.append  ([x - 1, y - 1, 5, 0])
    if x + 1 <= maxOfX and y - 1 >= 0:
        if (board[y - 1][x + 1] != 0):  # from lower left 6 to upper right 3
            results.append ([x + 1, y - 1, 6, 0])

    return results

def hamiltonianCycleInitialization():
    # to generate a root and count the #cells
    #
    global hamiltonianCycleRoot
    global totalNumberOfCells
    totalNumberOfCells = 0


    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != 0:
                totalNumberOfCells = totalNumberOfCells + 1
                hamiltonianCycleRoot = x, y
    return

def hamiltonianCycleGenerator():
    # DFS
    global hamiltonianCycleMap
    global hamiltonianCycleRoot

    footPrintsStack = []
    footPrintsMap = numpy.zeros_like(board)
    thisCell = (hamiltonianCycleRoot[0], hamiltonianCycleRoot[1], -1)
    completeFlag = False
    footPrintsStack.append(thisCell)

    while (not completeFlag):

        pygame.time.delay(1000)
        # search for next step

        neighbourList = searchNeighbourCells(thisCell)
        availableNextCellList = []

        # filter
        for neighbour in neighbourList:
            if neighbour not in footPrintsStack:# not visit yet
                if neighbour[2] > hamiltonianCycleMap[thisCell[1]][thisCell[0]]:# next.from >= this.to
                    availableNextCellList.append(neighbour)

            else: # visited previously
                if neighbour == footPrintsStack[0]:#is the root
                    if totalNumberOfCells == len(footPrintsStack)-1:
                        footPrintsStack.append(neighbour)
                        footPrintsMap[thisCell[1]][thisCell[0]] = neighbour[2]
                        completeFlag = True
                        break
                else: # not the root
                    pass

        # go to next step
        print("available: ",availableNextCellList)
        if not completeFlag:
            if len(availableNextCellList) == 0: # no next step
                footPrintsStack.pop()
                print("go back")

            else:# there is next step
                # record the footprint
                thisCell = availableNextCellList[0]
                footPrintsStack.append(thisCell)
                footPrintsMap[thisCell[1]][thisCell[0]] = thisCell[2]
                print("goto: ", thisCell)



def hamiltonianCycleDisplay():
    pass


# for buttons
def buttonConstructorAndPainter():
    pygame.draw.rect(screen, coloursLibrary['backGround'],
                     (sizeOfTheWindow[0] - buttonSize[0] - 10, 0, buttonSize[0], sizeOfTheWindow[1]), 0)
    theFont = pygame.font.Font('OpenSans-Light.ttf', 20)

    # the first button
    if buttonStates[1] == 0:
        pygame.draw.rect(screen, coloursLibrary[2],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, 10, buttonSize[0], buttonSize[1]), 4)
        theText = theFont.render("Index Hidden", True, coloursLibrary['black'])

    else:
        pygame.draw.rect(screen, coloursLibrary[2],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, 10, buttonSize[0], buttonSize[1]), 0)
        theText = theFont.render("Index Displayed", True, coloursLibrary['black'])

    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, 10))

    # the second button
    if buttonStates[2] == 0:
        pygame.draw.rect(screen, coloursLibrary[2],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] + 20, buttonSize[0], buttonSize[1]), 4)
        theText = theFont.render("Hamiltonian Cycle?", True, coloursLibrary['black'])
    else:
        pygame.draw.rect(screen, coloursLibrary[2],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] + 20, buttonSize[0], buttonSize[1]), 0)
        theText = theFont.render("Hamiltonian Cycle!", True, coloursLibrary['black'])

    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, buttonSize[1] + 20))

    # the third button
    if buttonStates[3] == 0:
        pygame.draw.rect(screen, coloursLibrary[2], (
            sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] * 2 + 30, buttonSize[0], buttonSize[1]), 4)
        theText = theFont.render("in state 0", True, coloursLibrary['black'])

    else:
        pygame.draw.rect(screen, coloursLibrary[2], (
            sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] * 2 + 30, buttonSize[0], buttonSize[1]), 0)
        theText = theFont.render("in state 1", True, coloursLibrary['black'])

    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, buttonSize[1] * 2 + 30))

    # # refresh the window
    # pygame.display.update()


def buttonsSearchingByCoordinate(pos):
    if pos[0] > sizeOfTheWindow[0] - buttonSize[0]:
        if pos[1] < buttonSize[1] + 10: return 1;
        if pos[1] < buttonSize[1] * 2 + 20: return 2;
        if pos[1] < buttonSize[1] * 3 + 30: return 3;

    return -1


def buttonOneClicked():
    # switcher
    buttonStates[1] = 1 - buttonStates[1]

    global displayIndexOnTheScreen
    if buttonStates[1] == 0:
        displayIndexOnTheScreen = False
    else:
        displayIndexOnTheScreen = True

    # refresh the whole window
    screen.fill(coloursLibrary['backGround'])
    buttonConstructorAndPainter()
    cellsAndAxisConstructor()
    gourdsConstructor()
    pygame.display.update()


def buttonTwoClicked():
    # switcher
    buttonStates[2] = 1 - buttonStates[2]

    if buttonStates[2]:
        # update button
        buttonConstructorAndPainter()
        pygame.display.update()
        hamiltonianCycleInitialization()
        hamiltonianCycleGenerator()
        hamiltonianCycleDisplay()
        pygame.display.update()
    else:
        redrawTheScreen()



def buttonThreeClicked():
    buttonStates[3] = 1 - buttonStates[3]
    buttonConstructorAndPainter()
    pygame.display.update()


# for cells

def cellPainter(x, y):
    widthOfBlackFrameLine = -1
    widthOfColourCell = (widthOfHexCell * 0.8)

    # draw colour
    pygame.draw.polygon(screen, coloursLibrary[board[y][x]],
                        [
                            (  # down corner
                                int(offset + x * widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfColourCell * 1.1547)
                            ),
                            (  # down-right corner
                                int(offset + x * widthOfHexCell + widthOfColourCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfColourCell * 0.57735)
                            ),
                            (  # up-right corner
                                int(offset + x * widthOfHexCell + widthOfColourCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfColourCell * 0.57735)
                            ),
                            (  # up corner
                                int(offset + x * widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfColourCell * 1.1547)
                            ),
                            (  # up-left corner
                                int(offset + x * widthOfHexCell - widthOfColourCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfColourCell * 0.57735)
                            ),
                            (  # down-left corner
                                int(offset + x * widthOfHexCell - widthOfColourCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfColourCell * 0.57735)
                            )
                        ], int(widthOfHexCell / 10))

    # draw a frame
    pygame.draw.polygon(screen, coloursLibrary['black'],
                        [
                            (  # down corner
                                int(offset + x * widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfHexCell * 1.1547)
                            ),
                            (  # down-right corner
                                int(offset + x * widthOfHexCell + widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735)
                            ),
                            (  # up-right corner
                                int(offset + x * widthOfHexCell + widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735)
                            ),
                            (  # up corner
                                int(offset + x * widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfHexCell * 1.1547)
                            ),
                            (  # up-left corner
                                int(offset + x * widthOfHexCell - widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735)
                            ),
                            (  # down-left corner
                                int(offset + x * widthOfHexCell - widthOfHexCell),
                                int(offset + y * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735)
                            )
                        ], widthOfBlackFrameLine)


def cellsAndAxisConstructor():
    theFont = pygame.font.Font('OpenSans-Light.ttf', 16)

    # draw the axis
    # print("widthOfHexCell = ", widthOfHexCell)
    for y in range(len(board[0])):
        theText = theFont.render(str(y), True, coloursLibrary['black'])
        screen.blit(theText, (-6 + offset + y * widthOfHexCell, 0))
    for x in range(len(board)):
        theText = theFont.render(str(x), True, coloursLibrary['black'])
        screen.blit(theText, (8, int(-14 + offset + x * widthOfHexCell * 1.732)))

    # draw the cells
    theFont = pygame.font.Font('OpenSans-Light.ttf', 22)
    for y in range(len(board)):
        for x in range(len(board[0])):
            # display matrix numbers on screen
            if displayIndexOnTheScreen:
                if board[y][x]:
                    # display if not board[i][j] is not 0
                    theText = theFont.render(str(board[y][x]), True, coloursLibrary[board[y][x]])
                    screen.blit(theText, (int(-widthOfHexCell / 1.6) + offset + x * widthOfHexCell,
                                          int(-16 + offset + y * widthOfHexCell * 1.732)))
            # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

            if (board[y][x]):
                # draw a hexagonal cell
                cellPainter(x, y)
    # refresh the window
    # pygame.display.update()


# for gourds

def gourdPainter(firstPart, secondPart):
    # draw a gourd
    pygame.draw.circle(screen, coloursLibrary[firstPart[2]], (firstPart[0], firstPart[1]), gourdSize, 0)
    pygame.draw.circle(screen, coloursLibrary[secondPart[2]], (secondPart[0], secondPart[1]), gourdSize, 0)
    pygame.draw.line(screen, coloursLibrary[firstPart[2]],
                     (firstPart[0], firstPart[1]),
                     (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                     width=int(widthOfHexCell * 0.1 + 2))
    pygame.draw.line(screen, coloursLibrary[secondPart[2]],
                     (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                     (secondPart[0], secondPart[1]),
                     width=int(widthOfHexCell * 0.1 + 2))


def gourdsConstructor():
    # (x of the window, y of the window, index of the gourds)
    firstPart = (-1, -1, -1)
    secondPart = (-1, -1, -1)

    for i in range(len(gourdsList)):
        firstPart = (int(offset + gourdsList[i][0] * widthOfHexCell),
                     int(offset + gourdsList[i][1] * widthOfHexCell * 1.732),
                     gourdsList[i][4])
        secondPart = (int(offset + gourdsList[i][2] * widthOfHexCell),
                      int(offset + gourdsList[i][3] * widthOfHexCell * 1.732),
                      gourdsList[i][5])
        gourdPainter(firstPart, secondPart)

        # display the numbers / indexes on the gourds
        if displayIndexOnTheScreen:
            # first part
            numberSize = widthOfHexCell / 2
            theFont = pygame.font.Font('OpenSans-Light.ttf', int(numberSize))
            theText = theFont.render(str(firstPart[2]), True, coloursLibrary['backGround'])
            screen.blit(theText, (firstPart[0] - int(numberSize * 0.25), firstPart[1] - int(numberSize * 0.75)))
            # second part
            numberSize = widthOfHexCell / 2
            theFont = pygame.font.Font('OpenSans-Light.ttf', int(numberSize))
            theText = theFont.render(str(secondPart[2]), True, coloursLibrary['backGround'])
            screen.blit(theText, (secondPart[0] - int(numberSize * 0.25), secondPart[1] - int(numberSize * 0.75)))

    # refresh the window
    # pygame.display.update()


def gourdsSearchingByCoordinate(pos):
    x, y = pos
    # shrink the searching area
    x = x - offset
    y = y - offset
    x = x / widthOfHexCell
    y = y / 1.732 / widthOfHexCell
    x = int(x + 0.5)
    y = int(y + 0.5)

    return gourdsSearchingByIndex(x, y)


def gourdsSearchingByIndex(x, y):
    # search if there is a gourd on (x, y)
    for i in range(len(gourdsList)):
        if (x == gourdsList[i][0] and y == gourdsList[i][1]):
            return i, x, y
        if (x == gourdsList[i][2] and y == gourdsList[i][3]):
            return i, x, y
    return -1, -1, -1


def emptyCellSearchingAroundAGourd(x, y):
    # obtain the size of the boardMatrix
    maxOfX = len(board[0]) - 1
    maxOfY = len(board) - 1

    # search an empty cell around x, y
    if x - 1 >= 0 and y - 1 >= 0:
        if (board[y - 1][x - 1] != 0) and (gourdsSearchingByIndex(x - 1, y - 1)[0] == -1):  # upper left
            return x - 1, y - 1
    if x - 1 >= 0 and y + 1 <= maxOfY:
        if (board[y + 1][x - 1] != 0) and (gourdsSearchingByIndex(x - 1, y + 1)[0] == -1):  # lower left
            return x - 1, y + 1
    if x + 1 <= maxOfX and y + 1 <= maxOfY:
        if (board[y + 1][x + 1] != 0) and (gourdsSearchingByIndex(x + 1, y + 1)[0] == -1):  # lower right
            return x + 1, y + 1
    if x + 1 <= maxOfX and y - 1 >= 0:
        if (board[y - 1][x + 1] != 0) and (gourdsSearchingByIndex(x + 1, y - 1)[0] == -1):  # upper right
            return x + 1, y - 1
    if x - 2 >= 0:
        if (board[y][x - 2] != 0) and (gourdsSearchingByIndex(x - 2, y)[0] == -1):  # left
            return x - 2, y
    if x + 2 <= maxOfX:
        if (board[y][x + 2] != 0) and (gourdsSearchingByIndex(x + 2, y)[0] == -1):  # right
            return x + 2, y
    return -1, -1


def gourdsMovementAnimation(before, after, indexOfGourd):
    distance = [
        after[0] - before[0],
        after[1] - before[1],
        after[2] - before[2],
        after[3] - before[3]
    ]

    eachPaceInAnimation = 0.05
    rangeMax = int(1 / eachPaceInAnimation) + 1

    firstPart = (-1, -1, -1)
    secondPart = (-1, -1, -1)
    for i in range(0, rangeMax):
        pygame.time.delay(10)
        # draw a gourd
        firstPart = (int(offset + (before[0] + distance[0] * i * eachPaceInAnimation) * widthOfHexCell),
                     int(offset + (before[1] + distance[1] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                     gourdsList[indexOfGourd][4])
        secondPart = (int(offset + (before[2] + distance[2] * i * eachPaceInAnimation) * widthOfHexCell),
                      int(offset + (before[3] + distance[3] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                      gourdsList[indexOfGourd][5])
        gourdPainter(firstPart, secondPart)

        # refresh the window
        pygame.display.update()

        # cover the gourds by background
        firstPart = (int(offset + (before[0] + distance[0] * i * eachPaceInAnimation) * widthOfHexCell),
                     int(offset + (before[1] + distance[1] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                     'backGround')
        secondPart = (int(offset + (before[2] + distance[2] * i * eachPaceInAnimation) * widthOfHexCell),
                      int(offset + (before[3] + distance[3] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                      'backGround')
        gourdPainter(firstPart, secondPart)

        # redraw relative cells
        cellPainter(before[0], before[1])
        cellPainter(before[2], before[3])
        cellPainter(after[0], after[1])
        cellPainter(after[2], after[3])

    # draw a final gourd place
    firstPart = (int(offset + (before[0] + distance[0] * i * eachPaceInAnimation) * widthOfHexCell),
                 int(offset + (before[1] + distance[1] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                 gourdsList[indexOfGourd][4])
    secondPart = (int(offset + (before[2] + distance[2] * i * eachPaceInAnimation) * widthOfHexCell),
                  int(offset + (before[3] + distance[3] * i * eachPaceInAnimation) * widthOfHexCell * 1.732),
                  gourdsList[indexOfGourd][5])
    gourdPainter(firstPart, secondPart)

    # refresh the window
    pygame.display.update()


def gourdsMovementController(indexOfGourd, xGourdClicked, yGourdClicked, xCell, yCell):
    # identify the clicked and linked parts of gourd
    if gourdsList[indexOfGourd][0] == xGourdClicked and gourdsList[indexOfGourd][1] == yGourdClicked:
        firstPartClicked = True
        xGourdLinked = gourdsList[indexOfGourd][2]
        yGourdLinked = gourdsList[indexOfGourd][3]
    elif gourdsList[indexOfGourd][2] == xGourdClicked and gourdsList[indexOfGourd][3] == yGourdClicked:
        firstPartClicked = False
        xGourdLinked = gourdsList[indexOfGourd][0]
        yGourdLinked = gourdsList[indexOfGourd][1]
    else:
        print("Something went wrong in gourdsMovement()")
        return -1
    # move gourd

    distanceSquare = ((xGourdLinked - xCell) ** 2) + (((yGourdLinked - yCell) * 1.732) ** 2)
    if distanceSquare < 4.3:  # pivot
        xGourdClicked = xCell
        yGourdClicked = yCell
    else:  # slide or turn
        xGourdLinked = xGourdClicked
        yGourdLinked = yGourdClicked
        xGourdClicked = xCell
        yGourdClicked = yCell

    # identify the clicked and linked parts and save
    if firstPartClicked:
        # animation
        gourdsMovementAnimation((gourdsList[indexOfGourd][0], gourdsList[indexOfGourd][1], gourdsList[indexOfGourd][2],
                                 gourdsList[indexOfGourd][3]),
                                (xGourdClicked, yGourdClicked, xGourdLinked, yGourdLinked),
                                indexOfGourd)
        gourdsList[indexOfGourd][0] = xGourdClicked
        gourdsList[indexOfGourd][1] = yGourdClicked
        gourdsList[indexOfGourd][2] = xGourdLinked
        gourdsList[indexOfGourd][3] = yGourdLinked

    else:
        # animation
        gourdsMovementAnimation((gourdsList[indexOfGourd][0], gourdsList[indexOfGourd][1], gourdsList[indexOfGourd][2],
                                 gourdsList[indexOfGourd][3]),
                                (xGourdLinked, yGourdLinked, xGourdClicked, yGourdClicked),
                                indexOfGourd)
        gourdsList[indexOfGourd][0] = xGourdLinked
        gourdsList[indexOfGourd][1] = yGourdLinked
        gourdsList[indexOfGourd][2] = xGourdClicked
        gourdsList[indexOfGourd][3] = yGourdClicked

    # finally refresh the whole board
    # cellsAndAxisConstructor()
    # gourdsConstructor()

    return 0


def mouseClicked(pos):
    # search Gourds by the given Coordinate
    indexOfGourd, xGourd, yGourd = gourdsSearchingByCoordinate(pos)
    if indexOfGourd != -1:
        # print(xGourd, yGourd)
        # search if there is an Empty Cell Around
        xCell, yCell = emptyCellSearchingAroundAGourd(xGourd, yGourd)
        if xCell != -1:
            # move gourd to the empty cell
            gourdsMovementController(indexOfGourd, xGourd, yGourd, xCell, yCell)
            # finally refresh the cells and gourds
            cellsAndAxisConstructor()
            gourdsConstructor()
            pygame.display.update()

            return 0

        return 0

    # search button by the given coordinate
    indexOfButton = buttonsSearchingByCoordinate(pos)
    if indexOfButton == -1: return -1
    if indexOfButton == 1:
        buttonOneClicked()
        return 0
    if indexOfButton == 2:
        buttonTwoClicked()
        return 0
    if indexOfButton == 3:
        buttonThreeClicked()
        return 0

    return -1;


def redrawTheScreen():
    screen.fill(coloursLibrary['backGround'])
    buttonConstructorAndPainter()
    cellsAndAxisConstructor()
    gourdsConstructor()
    pygame.display.update()


def main():
    # initialization
    buttonConstructorAndPainter()
    cellsAndAxisConstructor()
    gourdsConstructor()
    global runFirstTimeFlag
    runFirstTimeFlag = False

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
