import pygame

class cellsConstructor(object):

    def __init__(self, screen, board, coloursLibrary, offset, widthOfHexCell):
        self.screen = screen
        self.board = board
        self.coloursLibrary = coloursLibrary
        self.offset = offset
        self.widthOfHexCell = widthOfHexCell

    def cellPainter(self, x, y):
        widthOfBlackFrameLine = -1
        widthOfColourCell = (self.widthOfHexCell * 0.8)

        # draw colour
        pygame.draw.polygon(self.screen, self.coloursLibrary[self.board[y][x]],
                            [
                                (  # down corner
                                    int(self.offset + x * self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + widthOfColourCell * 1.1547)
                                ),
                                (  # down-right corner
                                    int(self.offset + x * self.widthOfHexCell + widthOfColourCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + widthOfColourCell * 0.57735)
                                ),
                                (  # up-right corner
                                    int(self.offset + x * self.widthOfHexCell + widthOfColourCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - widthOfColourCell * 0.57735)
                                ),
                                (  # up corner
                                    int(self.offset + x * self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - widthOfColourCell * 1.1547)
                                ),
                                (  # up-left corner
                                    int(self.offset + x * self.widthOfHexCell - widthOfColourCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - widthOfColourCell * 0.57735)
                                ),
                                (  # down-left corner
                                    int(self.offset + x * self.widthOfHexCell - widthOfColourCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + widthOfColourCell * 0.57735)
                                )
                            ], int(self.widthOfHexCell / 10))

        # draw a frame
        pygame.draw.polygon(self.screen, self.coloursLibrary['black'],
                            [
                                (  # down corner
                                    int(self.offset + x * self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + self.widthOfHexCell * 1.1547)
                                ),
                                (  # down-right corner
                                    int(self.offset + x * self.widthOfHexCell + self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + self.widthOfHexCell * 0.57735)
                                ),
                                (  # up-right corner
                                    int(self.offset + x * self.widthOfHexCell + self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - self.widthOfHexCell * 0.57735)
                                ),
                                (  # up corner
                                    int(self.offset + x * self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - self.widthOfHexCell * 1.1547)
                                ),
                                (  # up-left corner
                                    int(self.offset + x * self.widthOfHexCell - self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 - self.widthOfHexCell * 0.57735)
                                ),
                                (  # down-left corner
                                    int(self.offset + x * self.widthOfHexCell - self.widthOfHexCell),
                                    int(self.offset + y * self.widthOfHexCell * 1.732 + self.widthOfHexCell * 0.57735)
                                )
                            ], widthOfBlackFrameLine)


    def cellsAndAxisConstructor(self, isDisplayIndex):
        self.theFont = pygame.font.Font('OpenSans-Light.ttf', 16)

        # draw the axis
        # print("widthOfHexCell = ", widthOfHexCell)
        for y in range(len(self.board[0])):
            theText = self.theFont.render(str(y), True, self.coloursLibrary['black'])
            self.screen.blit(theText, (-6 + self.offset + y * self.widthOfHexCell, 0))
        for x in range(len(self.board)):
            theText = self.theFont.render(str(x), True, self.coloursLibrary['black'])
            self.screen.blit(theText, (8, int(-14 + self.offset + x * self.widthOfHexCell * 1.732)))

        # draw the cells
        if len(self.coloursLibrary) > 15:
            fontSize = 15
        else:
            fontSize = 22
        theFont = pygame.font.Font('OpenSans-Light.ttf', fontSize)

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                # display matrix numbers on screen
                if isDisplayIndex:
                    if self.board[y][x]:
                        # display if not board[i][j] is not 0
                        theText = theFont.render(str(self.board[y][x]), True, self.coloursLibrary[self.board[y][x]])
                        self.screen.blit(theText, (int(-self.widthOfHexCell / 1.6) + fontSize - 20 + self.offset + x * self.widthOfHexCell,
                                              int(- fontSize + 5 + self.offset + y * self.widthOfHexCell * 1.732)))
                # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

                if (self.board[y][x]):
                    # draw a hexagonal cell
                    self.cellPainter(x, y)
        # refresh the window
        # pygame.display.update()
