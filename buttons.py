import pygame



class buttons(object):

    def __init__(self, screen, coloursLibrary, sizeOfTheWindow, buttonSize):
        self.screen = screen
        self.coloursLibrary = coloursLibrary
        self.sizeOfTheWindow = sizeOfTheWindow
        self.buttonSize = buttonSize
        # button states
        self.buttonStates = [0, 0, 0, 0, 0, 0, 0]  # 0 by default

    def buttonConstructorAndPainter(self):
        pygame.draw.rect(self.screen, self.coloursLibrary['backGround'],
                         (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, 0, self.buttonSize[0], self.sizeOfTheWindow[1]), 0)
        theFont = pygame.font.Font('OpenSans-Light.ttf', 20)

        # the first button
        if self.buttonStates[1] == 0:
            pygame.draw.rect(self.screen, self.coloursLibrary[2],
                             (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, 10, self.buttonSize[0], self.buttonSize[1]), 4)
            theText = theFont.render("Index Hidden", True, self.coloursLibrary['black'])

        else:
            pygame.draw.rect(self.screen, self.coloursLibrary[2],
                             (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, 10, self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render("Index Displayed", True, self.coloursLibrary['black'])

        self.screen.blit(theText, (self.sizeOfTheWindow[0] - self.buttonSize[0] + 5, 10))

        # the second button
        if self.buttonStates[2] == 0:
            pygame.draw.rect(self.screen, self.coloursLibrary[2],
                             (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] + 20, self.buttonSize[0], self.buttonSize[1]), 4)
            theText = theFont.render("Hamiltonian Cycle?", True, self.coloursLibrary['black'])
        else:
            pygame.draw.rect(self.screen, self.coloursLibrary[2],
                             (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] + 20, self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render("Hamiltonian Cycle!", True, self.coloursLibrary['black'])

        self.screen.blit(theText, (self.sizeOfTheWindow[0] - self.buttonSize[0] + 5, self.buttonSize[1] + 20))

        # the third button
        if self.buttonStates[3] == 0:
            pygame.draw.rect(self.screen, self.coloursLibrary[2], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * 2 + 30, self.buttonSize[0], self.buttonSize[1]), 4)
            theText = theFont.render("in state 0", True, self.coloursLibrary['black'])

        else:
            pygame.draw.rect(self.screen, self.coloursLibrary[2], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * 2 + 30, self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render("in state 1", True, self.coloursLibrary['black'])

        self.screen.blit(theText, (self.sizeOfTheWindow[0] - self.buttonSize[0] + 5, self.buttonSize[1] * 2 + 30))

        # # refresh the window
        # pygame.display.update()


    def buttonsSearchingByCoordinate(self, pos):
        # search button by the given coordinate

        indexOfButton = -1
        if pos[0] > self.sizeOfTheWindow[0] - self.buttonSize[0]:
            if pos[1] < self.buttonSize[1] + 10: indexOfButton = 1;
            elif pos[1] < self.buttonSize[1] * 2 + 20: indexOfButton = 2;
            elif pos[1] < self.buttonSize[1] * 3 + 30: indexOfButton = 3;

        if indexOfButton == -1: return -1
        if indexOfButton == 1:
            self.buttonOneClicked()
            return 0
        if indexOfButton == 2:
            self.buttonTwoClicked()
            return 0
        if indexOfButton == 3:
            self.buttonThreeClicked()
            return 0

        return -1


    def buttonOneClicked(self):
        # switcher
        self.buttonStates[1] = 1 - self.buttonStates[1]


    def buttonTwoClicked(self):
        # switcher
        self.buttonStates[2] = 1 - self.buttonStates[2]



    def buttonThreeClicked(self):
        self.buttonStates[3] = 1 - self.buttonStates[3]
        self.buttonConstructorAndPainter()
        # pygame.display.update()
