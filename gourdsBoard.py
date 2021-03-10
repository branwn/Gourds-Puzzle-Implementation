import pygame
import numpy  # for matrix

# set a matrix of board
displayMatrix = True
board = numpy.array([
   # x  0, 1, 2, 3, 4, 5, 6, 7, 8
    [0, 4, 0, 4, 0, 1, 0],  # 0
    [2, 0, 2, 0, 3, 0, 2],  # 1
    [0, 1, 0, 1, 0, 1, 0],  # 2
    [2, 0, 2, 0, 3, 0, 0],  # 3
])

# set a initial gourds placement
gourdsList = numpy.array([
   # x, y, x, y, colourDict_1, colourDict_2
    [1, 0, 0, 1, 4, 2],
    [2, 1, 4, 1, 4, 3],
    [1, 2, 3, 2, 1, 2],
    [0, 3, 2, 3, 3, 1],
    [4, 3, 5, 2, 2, 1],
    [5, 0, 6, 1, 2, 2]
])

# colour dictionary
colourDictionary = {
    'backGround': (242, 242, 242),
    'black': (0, 0, 0),
    1: (91, 231, 196),
    2: (80, 193, 233),
    3: (122, 87, 209),
    4: (237, 84, 133),
    5: (255, 232, 105)
}

# button states
buttonStates = [0, 0, 0, 0, 0, 0, 0]

# size of the window
sizeOfTheWindow = (600, 400)
# button size
buttonSize = 150, 30
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
screen.fill(colourDictionary['backGround'])


# for buttons
def buttonPainter():
    pygame.draw.rect(screen, colourDictionary['backGround'],
                     (sizeOfTheWindow[0] - buttonSize[0] - 10, 0, buttonSize[0], sizeOfTheWindow[1]), 0)

    # the first button
    if buttonStates[1] == 1:
        pygame.draw.rect(screen, colourDictionary[1],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, 10, buttonSize[0], buttonSize[1]), 0)
    else:
        pygame.draw.rect(screen, colourDictionary[1],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, 10, buttonSize[0], buttonSize[1]), 4)
    theFont = pygame.font.Font('OpenSans-Light.ttf', 20)
    theText = theFont.render("the 1st btn", True, colourDictionary['black'])
    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, 10))

    # the second button
    if buttonStates[2] == 1:
        pygame.draw.rect(screen, colourDictionary[1],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] + 20, buttonSize[0], buttonSize[1]), 0)
    else:
        pygame.draw.rect(screen, colourDictionary[1],
                         (sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] + 20, buttonSize[0], buttonSize[1]), 4)
    theFont = pygame.font.Font('OpenSans-Light.ttf', 20)
    theText = theFont.render("the 2nd btn", True, colourDictionary['black'])
    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, buttonSize[1] + 20))

    # the third button
    if buttonStates[3] == 1:
        pygame.draw.rect(screen, colourDictionary[1], (
        sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] * 2 + 30, buttonSize[0], buttonSize[1]), 0)
    else:
        pygame.draw.rect(screen, colourDictionary[1], (
            sizeOfTheWindow[0] - buttonSize[0] - 10, buttonSize[1] * 2 + 30, buttonSize[0], buttonSize[1]), 4)
    theFont = pygame.font.Font('OpenSans-Light.ttf', 20)
    theText = theFont.render("the 3rd btn", True, colourDictionary['black'])
    screen.blit(theText, (sizeOfTheWindow[0] - buttonSize[0] + 5, buttonSize[1] * 2 + 30))

    # refresh the window
    pygame.display.update()


def searchButtonsByCoordinate(pos):
    if pos[0] > sizeOfTheWindow[0] - buttonSize[0]:
        if pos[1] < buttonSize[1] + 10: return 1;
        if pos[1] < buttonSize[1] * 2 + 20: return 2;
        if pos[1] < buttonSize[1] * 3 + 30: return 3;

    return -1


def buttonOneClicked():
    buttonStates[1] = 1 - buttonStates[1]
    buttonPainter()


def buttonTwoClicked():
    buttonStates[2] = 1 - buttonStates[2]
    buttonPainter()


def buttonThreeClicked():
    buttonStates[3] = 1 - buttonStates[3]
    buttonPainter()


# for cells

def cellPainter(x, y):
    widthOfBlackFrameLine = -1
    widthOfColourCell = (widthOfHexCell * 0.8)

    # draw colour
    pygame.draw.polygon(screen, colourDictionary[board[y][x]],
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
    pygame.draw.polygon(screen, colourDictionary['black'],
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
    if runFirstTimeFlag:
        print(widthOfHexCell)
        for y in range(len(board[0])):
            theText = theFont.render(str(y), True, colourDictionary['black'])
            screen.blit(theText, (-6 + offset + y * widthOfHexCell, 0))
        for x in range(len(board)):
            theText = theFont.render(str(x), True, colourDictionary['black'])
            screen.blit(theText, (8, int(-14 + offset + x * widthOfHexCell * 1.732)))


    # draw the cells
    theFont = pygame.font.Font('OpenSans-Light.ttf', 22)
    for y in range(len(board)):
        for x in range(len(board[0])):
            # display matrix numbers on screen
            if displayMatrix:
                if board[y][x]:
                    # display if not board[i][j] is not 0
                    theText = theFont.render(str(board[y][x]), True, colourDictionary[board[y][x]])
                    screen.blit(theText, (int(-widthOfHexCell/1.6) + offset + x * widthOfHexCell, int(-16 + offset + y * widthOfHexCell * 1.732)))
            # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

            if (board[y][x]):
                # draw a hexagonal cell
                cellPainter(x, y)
    # refresh the window
    # pygame.display.update()


# for gourds

def gourdPainter(firstPart, secondPart):
    pygame.draw.circle(screen, colourDictionary[firstPart[2]], (firstPart[0], firstPart[1]), gourdSize, 0)
    pygame.draw.circle(screen, colourDictionary[secondPart[2]], (secondPart[0], secondPart[1]), gourdSize, 0)
    pygame.draw.line(screen, colourDictionary[firstPart[2]],
                     (firstPart[0], firstPart[1]),
                     (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                     width=int(widthOfHexCell * 0.1 + 2))
    pygame.draw.line(screen, colourDictionary[secondPart[2]],
                     (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                     (secondPart[0], secondPart[1]),
                     width=int(widthOfHexCell * 0.1 + 2))


def gourdsConstructor():
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
    # refresh the window
    pygame.display.update()


def searchGourdsByCoordinate(pos):
    x, y = pos
    # shrink the searching area
    x = x - offset
    y = y - offset
    x = x / widthOfHexCell
    y = y / 1.732 / widthOfHexCell
    x = int(x + 0.5)
    y = int(y + 0.5)

    return searchGourdsByIndex(x, y)


def searchGourdsByIndex(x, y):
    # search if there is a gourd on (x, y)
    for i in range(len(gourdsList)):
        if (x == gourdsList[i][0] and y == gourdsList[i][1]):
            return i, x, y
        if (x == gourdsList[i][2] and y == gourdsList[i][3]):
            return i, x, y
    return -1, -1, -1


def searchAnEmptyCellAround(x, y):
    # obtain the size of the boardMatrix
    maxOfX = len(board[0]) - 1
    maxOfY = len(board) - 1

    # search an empty cell around x, y
    if x - 1 >= 0 and y - 1 >= 0:
        if (board[y - 1][x - 1] != 0) and (searchGourdsByIndex(x - 1, y - 1)[0] == -1):  # upper left
            return x - 1, y - 1
    if x - 1 >= 0 and y + 1 <= maxOfY:
        if (board[y + 1][x - 1] != 0) and (searchGourdsByIndex(x - 1, y + 1)[0] == -1):  # lower left
            return x - 1, y + 1
    if x + 1 <= maxOfX and y + 1 <= maxOfY:
        if (board[y + 1][x + 1] != 0) and (searchGourdsByIndex(x + 1, y + 1)[0] == -1):  # lower right
            return x + 1, y + 1
    if x + 1 <= maxOfX and y - 1 >= 0:
        if (board[y - 1][x + 1] != 0) and (searchGourdsByIndex(x + 1, y - 1)[0] == -1):  # upper right
            return x + 1, y - 1
    if x - 2 >= 0:
        if (board[y][x - 2] != 0) and (searchGourdsByIndex(x - 2, y)[0] == -1):  # left
            return x - 2, y
    if x + 2 <= maxOfX:
        if (board[y][x + 2] != 0) and (searchGourdsByIndex(x + 2, y)[0] == -1):  # right
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


def gourdsMovement(indexOfGourd, xGourdClicked, yGourdClicked, xCell, yCell):
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
    cellsAndAxisConstructor()
    gourdsConstructor()

    return 0


def mouseClicked(pos):
    # search Gourds by the given Coordinate
    indexOfGourd, xGourd, yGourd = searchGourdsByCoordinate(pos)
    if indexOfGourd != -1:
        # print(xGourd, yGourd)
        # search if there is an Empty Cell Around
        xCell, yCell = searchAnEmptyCellAround(xGourd, yGourd)
        if xCell != -1:
            # move gourd to the empty cell
            gourdsMovement(indexOfGourd, xGourd, yGourd, xCell, yCell)
            return 0
        # refresh screen
        # screen.fill((242, 242, 242))
        # boardConstructor()
        # gourdsConstructor()
        return 0

    # search button by the given coordinate
    indexOfButton = searchButtonsByCoordinate(pos)
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


def main():
    # initialization
    buttonPainter()
    cellsAndAxisConstructor()
    gourdsConstructor()
    global runFirstTimeFlag
    runFirstTimeFlag = False

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



