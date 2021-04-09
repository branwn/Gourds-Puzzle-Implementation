import pygame



class buttons(object):

    def __init__(self, screen, coloursLibrary, sizeOfTheWindow, buttonSize):
        self.screen = screen
        self.coloursLibrary = coloursLibrary
        self.sizeOfTheWindow = sizeOfTheWindow
        self.buttonSize = buttonSize
        # button states
        self.buttonStates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 by default
        # auto display index
        if self.coloursLibrary[1] == self.coloursLibrary[2]:
            self.buttonStates[1] = 1;

    def buttonPainter(self, btnIndex, stringDefault, stringClicked):
        theFont = pygame.font.Font('OpenSans-Light.ttf', 20)

        if self.buttonStates[btnIndex] == 0:
            pygame.draw.rect(self.screen, self.coloursLibrary['button'], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * (btnIndex-1) + btnIndex*10, self.buttonSize[0], self.buttonSize[1]), 4)
            theText = theFont.render(stringDefault, True, self.coloursLibrary['black'])
        else:
            pygame.draw.rect(self.screen, self.coloursLibrary['button'], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * (btnIndex-1) + btnIndex*10, self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render(stringClicked, True, self.coloursLibrary['black'])
        self.screen.blit(theText, (self.sizeOfTheWindow[0] - self.buttonSize[0] + 5, self.buttonSize[1] * (btnIndex-1) + btnIndex*10))


    def buttonConstructor(self):
        pygame.draw.rect(self.screen, self.coloursLibrary['backGround'],
                         (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, 0, self.buttonSize[0], self.sizeOfTheWindow[1]), 0)

        self.buttonPainter(1, "Index Hidden", "Index Displayed")
        self.buttonPainter(2, "Hamiltonian Cycle?", "Hamiltonian Cycle!")
        self.buttonPainter(3, "Start Phase 1", "Phase 1 Finished")
        self.buttonPainter(4, "Start Phase 2", "Phase 2 Finished")
        self.buttonPainter(5, "Start Phase 3", "Phase 3 Finished")

        return


    def buttonsClicked(self, pos):
        # search button by the given coordinate

        indexOfButton = -1
        if pos[0] > self.sizeOfTheWindow[0] - self.buttonSize[0]:
            if pos[1] < self.buttonSize[1] + 10:  self.buttonStates[1] = 1 - self.buttonStates[1]
            elif pos[1] < self.buttonSize[1] * 2 + 20: self.buttonStates[2] = 1 - self.buttonStates[2]
            elif pos[1] < self.buttonSize[1] * 3 + 30: self.buttonStates[3] = 1 - self.buttonStates[3]
            elif pos[1] < self.buttonSize[1] * 4 + 40: self.buttonStates[4] = 1 - self.buttonStates[4]
            elif pos[1] < self.buttonSize[1] * 5 + 50: self.buttonStates[5] = 1 - self.buttonStates[5]

        return





