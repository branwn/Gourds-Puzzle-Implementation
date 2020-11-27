import pygame
import numpy as np  # for matrix


# set a matrix of board
displayMatrix = False
board = np.array([ # 0, 1, 2, 3, 4, 5, 6, 7, 8
                            [0, 1, 0, 1, 0, 0],  #0
                            [1, 0, 1, 0, 1, 0],  #1
                            [0, 1, 0, 1, 0, 0]   #2
                            ])

# set a initial gourds placement
gourds = np.array([
   # x, y, x, y, colourDict_1, colourDict_2
    [1, 0, 0, 1, 3, 3],
    [2, 1, 4, 1, 3, 3],
    [1, 2, 3, 2, 3, 3]
])
# colour dictionary
colourDictionary = {
    1:(242,242,242),
    2:(100,100,200),
    3:(100,0,0)
}

pygame.init()
# size of the window
screen = pygame.display.set_mode((500, 400))
# caption setting
pygame.display.set_caption('Gourds')
# background colour setting
screen.fill(colourDictionary[1])
# set width of the hexagonal cell
widthOfHexCell = 50;
offset = widthOfHexCell*1.5
# gourd size
gourdSize = widthOfHexCell * 0.6


def gourdPainter(firstPart, secondPart):
    pygame.draw.circle(screen, colourDictionary[firstPart[2]], (firstPart[0],firstPart[1]), gourdSize, 4)
    pygame.draw.circle(screen, colourDictionary[secondPart[2]], (secondPart[0], secondPart[1]), gourdSize, 4)
    pygame.draw.line(screen, colourDictionary[firstPart[2]],(firstPart[0],firstPart[1]),(secondPart[0],secondPart[1]), width=3)


def boardConstructor():
    font = pygame.font.Font('OpenSans-Light.ttf', 16)


    for i in range(len(board)):
        for j in range(len(board[0])):
            # display matrix
            text = font.render(str(board[i][j]), True, (0, 0, 255))
            if displayMatrix:
                screen.blit(text, (-4 + offset + j * widthOfHexCell, int(-12 + offset + i * widthOfHexCell * 1.732)))
            # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

            if (board[i][j]):
                # draw a hexagonal cell
                pygame.draw.polygon(screen, (100, 100, 200,),
                                    [
                                    (  # up corner
                                      int(offset + j * widthOfHexCell),
                                      int(offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 1.1547)
                                    ),
                                    (  # up-right corner
                                      int(offset + j * widthOfHexCell + widthOfHexCell),
                                      int(offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735)
                                    ),
                                    (  # down-right corner
                                      offset + j * widthOfHexCell + widthOfHexCell,
                                      int(offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735)
                                    ),
                                    (  # down corner
                                      int(offset + j * widthOfHexCell),
                                      int(offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 1.1547)
                                    ),
                                    (  # down-left corner
                                      int(offset + j * widthOfHexCell - widthOfHexCell),
                                      int(offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735)
                                    ),
                                    (  # up-left corner
                                      int(offset + j * widthOfHexCell - widthOfHexCell),
                                      int(offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735)
                                    )
                                    ], 1)

    # refresh the window
    # pygame.display.update()


def gourdsConstructor():
    firstPart = (-1, -1, -1)
    secondPart = (-1, -1, -1)

    for i in range(len(gourds)):
        firstPart = (int(offset + gourds[i][0] * widthOfHexCell),
                     int(offset + gourds[i][1] * widthOfHexCell * 1.732),
                     gourds[i][4])
        secondPart = (int(offset + gourds[i][2] * widthOfHexCell),
                      int(offset + gourds[i][3] * widthOfHexCell * 1.732),
                      gourds[i][4])
        gourdPainter(firstPart,secondPart)
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
    for i in range(len(gourds)):
        if (x == gourds[i][0] and y == gourds[i][1]):
            return i, x, y
        if (x == gourds[i][2] and y == gourds[i][3]):
            return i, x, y
    return -1, -1, -1


def searchAnEmptyCellAround(x, y):
    # obtain the size of the boardMatrix
    maxOfX = len(board[0]) - 1
    maxOfY = len(board) - 1

    # search an empty cell around x, y
    if x - 1 >= 0 and y - 1 >= 0:
        if (board[y - 1][x - 1] == 1) and (searchGourdsByIndex(x - 1, y - 1)[0] == -1):  # upper left
            return x - 1, y - 1
    if x - 1 >= 0 and y + 1 <= maxOfY:
        if (board[y + 1][x - 1] == 1) and (searchGourdsByIndex(x - 1, y + 1)[0] == -1):  # lower left
            return x - 1, y + 1
    if x + 1 <= maxOfX and y + 1 <= maxOfY:
        if (board[y + 1][x + 1] == 1) and (searchGourdsByIndex(x + 1, y + 1)[0] == -1):  # lower right
            return x + 1, y + 1
    if x + 1 <= maxOfX and y - 1 >= 0:
        if (board[y - 1][x + 1] == 1) and (searchGourdsByIndex(x + 1, y - 1)[0] == -1):  # upper right
            return x + 1, y - 1
    if x - 2 >= 0:
        if (board[y][x - 2] == 1) and (searchGourdsByIndex(x - 2, y)[0] == -1):  # left
            return x - 2, y
    if x + 2 <= maxOfX:
        if (board[y][x + 2] == 1) and (searchGourdsByIndex(x + 2, y)[0] == -1):  # right
            return x + 2, y
    return -1, -1


def gourdsMovementAnimation(before, after, indexOfGourd):
    distance = [
        after[0] - before[0],
        after[1] - before[1],
        after[2] - before[2],
        after[3] - before[3]
    ]
    persentageMoveStep = 0.05

    firstPart = (-1, -1, -1)
    secondPart = (-1, -1, -1)
    for i in range(0,20):
        pygame.time.delay(10)
        # draw a gourd
        firstPart = (int(offset + (before[0]+distance[0]*i*persentageMoveStep) * widthOfHexCell),
                     int(offset + (before[1]+distance[1]*i*persentageMoveStep) * widthOfHexCell * 1.732),
                     gourds[indexOfGourd][4])
        secondPart = (int(offset + (before[2]+distance[2]*i*persentageMoveStep) * widthOfHexCell),
                      int(offset + (before[3]+distance[3]*i*persentageMoveStep) * widthOfHexCell * 1.732),
                      gourds[indexOfGourd][5])
        gourdPainter(firstPart, secondPart)

        # refresh the window
        pygame.display.update()

        # cover the gourds by background
        firstPart = (int(offset + (before[0] + distance[0] * i * persentageMoveStep) * widthOfHexCell),
                     int(offset + (before[1] + distance[1] * i * persentageMoveStep) * widthOfHexCell * 1.732),
                     1)
        secondPart = (int(offset + (before[2] + distance[2] * i * persentageMoveStep) * widthOfHexCell),
                      int(offset + (before[3] + distance[3] * i * persentageMoveStep) * widthOfHexCell * 1.732),
                      1)
        gourdPainter(firstPart, secondPart)

        # refresh the window
        # pygame.display.update()


def gourdsMovement(indexOfGourd, xGourdClicked, yGourdClicked, xCell, yCell):

    # identify the clicked and linked parts of gourd
    if gourds[indexOfGourd][0] == xGourdClicked and gourds[indexOfGourd][1] == yGourdClicked:
        firstPartClicked = True
        xGourdLinked = gourds[indexOfGourd][2]
        yGourdLinked = gourds[indexOfGourd][3]
    elif gourds[indexOfGourd][2] == xGourdClicked and gourds[indexOfGourd][3] == yGourdClicked:
        firstPartClicked = False
        xGourdLinked = gourds[indexOfGourd][0]
        yGourdLinked = gourds[indexOfGourd][1]
    else:
        print("Something went wrong in gourdsMovement")
        return -1
    # move gourd

    distanceSquare = ((xGourdLinked - xCell) ** 2) + (((yGourdLinked - yCell)*1.732) ** 2)
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
        gourdsMovementAnimation((gourds[indexOfGourd][0], gourds[indexOfGourd][1], gourds[indexOfGourd][2], gourds[indexOfGourd][3]),
                                (xGourdClicked, yGourdClicked, xGourdLinked, yGourdLinked),
                                indexOfGourd)
        gourds[indexOfGourd][0] = xGourdClicked
        gourds[indexOfGourd][1] = yGourdClicked
        gourds[indexOfGourd][2] = xGourdLinked
        gourds[indexOfGourd][3] = yGourdLinked

    else:
        # animation
        gourdsMovementAnimation((gourds[indexOfGourd][0], gourds[indexOfGourd][1], gourds[indexOfGourd][2], gourds[indexOfGourd][3]),
                                (xGourdLinked, yGourdLinked, xGourdClicked, yGourdClicked),
                                indexOfGourd)
        gourds[indexOfGourd][0] = xGourdLinked
        gourds[indexOfGourd][1] = yGourdLinked
        gourds[indexOfGourd][2] = xGourdClicked
        gourds[indexOfGourd][3] = yGourdClicked

    return 0


def mouseClicked(pos):
    # search Gourds From Coordinate
    indexOfGourd, xGourd, yGourd = searchGourdsByCoordinate(pos)
    if indexOfGourd == -1: return -1;
    # print(xGourd, yGourd)
    # search An Empty Cell Around
    xCell, yCell = searchAnEmptyCellAround(xGourd, yGourd)
    if xCell == -1: return -1
    # move gourds
    gourdsMovement(indexOfGourd, xGourd, yGourd, xCell, yCell)
    # refresh screen
    # screen.fill((242, 242, 242))
    boardConstructor()
    gourdsConstructor()

def main():
    # main loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # MOUSE BUTTON DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked(event.pos)
            # MOUSE BUTTON UP
            if event.type == pygame.MOUSEBUTTONUP:
                pass


if __name__ == '__main__':
    boardConstructor()
    gourdsConstructor()
    main()
