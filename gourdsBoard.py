import pygame
import numpy as np  # for matrix

pygame.init()
# size of the window
screen = pygame.display.set_mode((500, 400))
# caption setting
pygame.display.set_caption('Gourds')
# background colour setting
screen.fill((242, 242, 242))
# set width of the hexagonal cell
widthOfHexCell = 50;
offset = widthOfHexCell*1.5
# gourd size
gourdSize = widthOfHexCell * 0.6

# set a matrix of board
displayMatrix = False
matrixOfBoard = np.array([#0, 1, 2, 3, 4, 5, 6, 7, 8
                          [0, 1, 0, 1, 0, 0],  #0
                          [1, 0, 1, 0, 1, 0],  #1
                          [0, 1, 0, 1, 0, 0]   #2
                          ])

# set a initial gourds placement
gourdsLocation = np.array([# x, y, x, y
                            [1, 0, 0, 1],
                            [2, 1, 4, 1],
                            [1, 2, 3, 2]
                          ])


def boardConstructor():
    font = pygame.font.Font('OpenSans-Light.ttf', 16)


    for i in range(len(matrixOfBoard)):
        for j in range(len(matrixOfBoard[0])):
            # display matrix
            text = font.render(str(matrixOfBoard[i][j]), True, (0, 0, 255))
            if displayMatrix:
                screen.blit(text, (-4 + offset + j * widthOfHexCell, int(-12 + offset + i * widthOfHexCell * 1.732)))
            # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

            if (matrixOfBoard[i][j]):
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
    pygame.display.flip()


def gourdsConstructor():
    for i in range(len(gourdsLocation)):
        pygame.draw.circle(screen, (100, 0, 0), (
            int(offset + gourdsLocation[i][0] * widthOfHexCell), int(offset + gourdsLocation[i][1] * widthOfHexCell * 1.732)),
                           gourdSize, 1)
        pygame.draw.circle(screen, (100, 0, 0), (
            int(offset + gourdsLocation[i][2] * widthOfHexCell), int(offset + gourdsLocation[i][3] * widthOfHexCell * 1.732)),
                           gourdSize, 1)
        pygame.draw.line(screen, (100, 0, 0), (
            offset + gourdsLocation[i][0] * widthOfHexCell, int(offset + gourdsLocation[i][1] * widthOfHexCell * 1.732)), (
                             offset + gourdsLocation[i][2] * widthOfHexCell,
                             int(offset + gourdsLocation[i][3] * widthOfHexCell * 1.732)), width=2)
    # refresh the window
    pygame.display.flip()


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


def searchGourdsByIndex(x, y, xDestination = -1, yDestination = -1):
    # search if there is a gourd on (x, y)
    for i in range(len(gourdsLocation)):
        if (x == gourdsLocation[i][0] and y == gourdsLocation[i][1]):
            if xDestination != -1:
                gourdsLocation[i][0] = xDestination
                gourdsLocation[i][1] = yDestination
            return i, x, y
        if (x == gourdsLocation[i][2] and y == gourdsLocation[i][3]):
            if xDestination != -1:
                gourdsLocation[i][2] = xDestination
                gourdsLocation[i][3] = yDestination
            return i, x, y
    return -1, -1, -1


def searchAnEmptyCellAround(x, y):
    # obtain the size of the boardMatrix
    maxOfX = len(matrixOfBoard[0]) - 1
    maxOfY = len(matrixOfBoard) - 1

    # search an empty cell around x, y
    if x - 1 >= 0 and y - 1 >= 0:
        if (matrixOfBoard[y - 1][x - 1] == 1) and (searchGourdsByIndex(x - 1, y - 1) == (-1, -1, -1)):  # upper left
            return x - 1, y - 1
    if x - 1 >= 0 and y + 1 <= maxOfY:
        if (matrixOfBoard[y + 1][x - 1] == 1) and (searchGourdsByIndex(x - 1, y + 1) == (-1, -1, -1)):  # lower left
            return x - 1, y + 1
    if x + 1 <= maxOfX and y + 1 <= maxOfY:
        if (matrixOfBoard[y + 1][x + 1] == 1) and (searchGourdsByIndex(x + 1, y + 1) == (-1, -1, -1)):  # lower right
            return x + 1, y + 1
    if x + 1 <= maxOfX and y - 1 >= 0:
        if (matrixOfBoard[y - 1][x + 1] == 1) and (searchGourdsByIndex(x + 1, y - 1) == (-1, -1, -1)):  # upper right
            return x + 1, y - 1
    if x - 2 >= 0:
        if (matrixOfBoard[y][x - 2] == 1) and (searchGourdsByIndex(x - 2, y) == (-1, -1, -1)):  # left
            return x - 2, y
    if x + 2 <= maxOfX:
        if (matrixOfBoard[y][x + 2] == 1) and (searchGourdsByIndex(x + 2, y) == (-1, -1, -1)):  # right
            return x + 2, y
    return -1, -1


def gourdsMovement(indexOfGourd, xGourd, yGourd, xCell, yCell):
    searchGourdsByIndex(xGourd, yGourd, xCell, yCell)


def mouseClick(pos):
    # search Gourds From Coordinate
    indexOfGourd, xGourd, yGourd = searchGourdsByCoordinate(pos)
    if indexOfGourd == -1: return -1;
    print(xGourd, yGourd)
    # search An Empty Cell Around
    xCell, yCell = searchAnEmptyCellAround(xGourd, yGourd)
    if xCell == -1: return -1
    # move gourds
    gourdsMovement(indexOfGourd, xGourd, yGourd, xCell, yCell)
    # refresh screen
    screen.fill((242, 242, 242))
    boardConstructor()
    gourdsConstructor()
    pygame.display.flip()


def main():
    # main loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # MOUSE BUTTON DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClick(event.pos)
            # MOUSE BUTTON UP
            if event.type == pygame.MOUSEBUTTONUP:
                pass


if __name__ == '__main__':
    boardConstructor()
    gourdsConstructor()
    main()
