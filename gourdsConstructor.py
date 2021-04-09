import pygame

class gourdsConstructor(object):

    def __init__(self, screen, board, gourdsList, coloursLibrary, offset, widthOfHexCell, gourdSize):
        self.screen = screen
        self.board = board
        self.gourdsList = gourdsList
        self.coloursLibrary = coloursLibrary
        self.offset = offset
        self.widthOfHexCell = widthOfHexCell
        self.gourdSize = gourdSize


    def gourdPainter(self, firstPart, secondPart):
        # draw a gourd
        pygame.draw.circle(self.screen, self.coloursLibrary[firstPart[2]], (firstPart[0], firstPart[1]), self.gourdSize, 0)
        pygame.draw.circle(self.screen, self.coloursLibrary[secondPart[2]], (secondPart[0], secondPart[1]), self.gourdSize, 0)
        pygame.draw.line(self.screen, self.coloursLibrary[firstPart[2]],
                         (firstPart[0], firstPart[1]),
                         (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                         width=int(self.widthOfHexCell * 0.1 + 6))
        pygame.draw.line(self.screen, self.coloursLibrary[secondPart[2]],
                         (int((firstPart[0] + secondPart[0]) / 2), int((firstPart[1] + secondPart[1]) / 2)),
                         (secondPart[0], secondPart[1]),
                         width=int(self.widthOfHexCell * 0.1 + 6))

    def gourdsConstructor(self, isDisplayIndex):
        # (x of the window, y of the window, index of the gourds)
        firstPart = (-1, -1, -1)
        secondPart = (-1, -1, -1)

        for i in range(len(self.gourdsList)):
            firstPart = (int(self.offset + self.gourdsList[i][0] * self.widthOfHexCell),
                         int(self.offset + self.gourdsList[i][1] * self.widthOfHexCell * 1.732),
                         self.gourdsList[i][4])
            secondPart = (int(self.offset + self.gourdsList[i][2] * self.widthOfHexCell),
                          int(self.offset + self.gourdsList[i][3] * self.widthOfHexCell * 1.732),
                          self.gourdsList[i][5])
            self.gourdPainter(firstPart, secondPart)

            # display the numbers / indexes on the gourds
            if isDisplayIndex:
                # set the font size
                if len(self.coloursLibrary) > 15:
                    fontSize = 15
                else:
                    fontSize = 22
                theFont = pygame.font.Font('OpenSans-Light.ttf', fontSize)

                # first part
                theText = theFont.render(str(firstPart[2]), True, self.coloursLibrary['backGround'])
                self.screen.blit(theText, (firstPart[0] - int(fontSize * 0.25) + fontSize - 20, firstPart[1] - int(fontSize * 0.75)))
                # second part
                theText = theFont.render(str(secondPart[2]), True, self.coloursLibrary['backGround'])
                self.screen.blit(theText, (secondPart[0] - int(fontSize * 0.25) + fontSize - 20, secondPart[1] - int(fontSize * 0.75)))

        # refresh the window
        # pygame.display.update()

    def gourdsSearchingByCoordinate(self, pos):
        x, y = pos
        # shrink the searching area
        x = x - self.offset
        y = y - self.offset
        x = x / self.widthOfHexCell
        y = y / 1.732 / self.widthOfHexCell
        x = int(x + 0.5)
        y = int(y + 0.5)

        return self.gourdsSearchingByIndex(x, y)

    def gourdsSearchingByIndex(self, x, y):
        # search if there is a gourd on (x, y)
        for i in range(len(self.gourdsList)):
            if (x == self.gourdsList[i][0] and y == self.gourdsList[i][1]):
                return i, x, y
            if (x == self.gourdsList[i][2] and y == self.gourdsList[i][3]):
                return i, x, y
        return -1, -1, -1

    def emptyCellSearchingAroundAGourd(self, x, y):
        # obtain the size of the self.boardMatrix
        maxOfX = len(self.board[0]) - 1
        maxOfY = len(self.board) - 1

        # search an empty cell around x, y
        if x - 1 >= 0 and y - 1 >= 0:
            if (self.board[y - 1][x - 1] != 0) and (self.gourdsSearchingByIndex(x - 1, y - 1)[0] == -1):  # upper left
                return x - 1, y - 1
        if x - 1 >= 0 and y + 1 <= maxOfY:
            if (self.board[y + 1][x - 1] != 0) and (self.gourdsSearchingByIndex(x - 1, y + 1)[0] == -1):  # lower left
                return x - 1, y + 1
        if x + 1 <= maxOfX and y + 1 <= maxOfY:
            if (self.board[y + 1][x + 1] != 0) and (self.gourdsSearchingByIndex(x + 1, y + 1)[0] == -1):  # lower right
                return x + 1, y + 1
        if x + 1 <= maxOfX and y - 1 >= 0:
            if (self.board[y - 1][x + 1] != 0) and (self.gourdsSearchingByIndex(x + 1, y - 1)[0] == -1):  # upper right
                return x + 1, y - 1
        if x - 2 >= 0:
            if (self.board[y][x - 2] != 0) and (self.gourdsSearchingByIndex(x - 2, y)[0] == -1):  # left
                return x - 2, y
        if x + 2 <= maxOfX:
            if (self.board[y][x + 2] != 0) and (self.gourdsSearchingByIndex(x + 2, y)[0] == -1):  # right
                return x + 2, y
        return -1, -1

    def gourdsMovementAnimation(self, before, after, indexOfGourd):
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
            firstPart = (int(self.offset + (before[0] + distance[0] * i * eachPaceInAnimation) * self.widthOfHexCell),
                         int(self.offset + (before[1] + distance[1] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                         self.gourdsList[indexOfGourd][4])
            secondPart = (int(self.offset + (before[2] + distance[2] * i * eachPaceInAnimation) * self.widthOfHexCell),
                          int(self.offset + (before[3] + distance[3] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                          self.gourdsList[indexOfGourd][5])
            self.gourdPainter(firstPart, secondPart)

            # refresh the window
            pygame.display.update()

            # cover the gourds by background
            firstPart = (int(self.offset + (before[0] + distance[0] * i * eachPaceInAnimation) * self.widthOfHexCell),
                         int(self.offset + (before[1] + distance[1] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                         'backGround')
            secondPart = (int(self.offset + (before[2] + distance[2] * i * eachPaceInAnimation) * self.widthOfHexCell),
                          int(self.offset + (before[3] + distance[3] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                          'backGround')
            self.gourdPainter(firstPart, secondPart)

            # redraw relative cells
            #//TODO
            # myCells.cellPainter(before[0], before[1])
            # myCells.cellPainter(before[2], before[3])
            # myCells.cellPainter(after[0], after[1])
            # myCells.cellPainter(after[2], after[3])

        # draw a final gourd place
        firstPart = (int(self.offset + (before[0] + distance[0] * i * eachPaceInAnimation) * self.widthOfHexCell),
                     int(self.offset + (before[1] + distance[1] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                     self.gourdsList[indexOfGourd][4])
        secondPart = (int(self.offset + (before[2] + distance[2] * i * eachPaceInAnimation) * self.widthOfHexCell),
                      int(self.offset + (before[3] + distance[3] * i * eachPaceInAnimation) * self.widthOfHexCell * 1.732),
                      self.gourdsList[indexOfGourd][5])
        self.gourdPainter(firstPart, secondPart)

        # refresh the window
        pygame.display.update()

    def gourdsMovementController(self, indexOfGourd, xGourdClicked, yGourdClicked, xCell, yCell):
        # identify the clicked and linked parts of gourd
        if self.gourdsList[indexOfGourd][0] == xGourdClicked and self.gourdsList[indexOfGourd][1] == yGourdClicked:
            firstPartClicked = True
            xGourdLinked = self.gourdsList[indexOfGourd][2]
            yGourdLinked = self.gourdsList[indexOfGourd][3]
        elif self.gourdsList[indexOfGourd][2] == xGourdClicked and self.gourdsList[indexOfGourd][3] == yGourdClicked:
            firstPartClicked = False
            xGourdLinked = self.gourdsList[indexOfGourd][0]
            yGourdLinked = self.gourdsList[indexOfGourd][1]
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
            self.gourdsMovementAnimation(
                (self.gourdsList[indexOfGourd][0], self.gourdsList[indexOfGourd][1], self.gourdsList[indexOfGourd][2],
                 self.gourdsList[indexOfGourd][3]),
                (xGourdClicked, yGourdClicked, xGourdLinked, yGourdLinked),
                indexOfGourd)
            self.gourdsList[indexOfGourd][0] = xGourdClicked
            self.gourdsList[indexOfGourd][1] = yGourdClicked
            self.gourdsList[indexOfGourd][2] = xGourdLinked
            self.gourdsList[indexOfGourd][3] = yGourdLinked

        else:
            # animation
            self.gourdsMovementAnimation(
                (self.gourdsList[indexOfGourd][0], self.gourdsList[indexOfGourd][1], self.gourdsList[indexOfGourd][2],
                 self.gourdsList[indexOfGourd][3]),
                (xGourdLinked, yGourdLinked, xGourdClicked, yGourdClicked),
                indexOfGourd)
            self.gourdsList[indexOfGourd][0] = xGourdLinked
            self.gourdsList[indexOfGourd][1] = yGourdLinked
            self.gourdsList[indexOfGourd][2] = xGourdClicked
            self.gourdsList[indexOfGourd][3] = yGourdClicked

        # finally refresh the whole self.board
        # cellsAndAxisConstructor()
        # gourdsConstructor()

        return 0
