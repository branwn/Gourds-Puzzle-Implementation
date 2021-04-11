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

    def buttonPainter(self, btnIndex, stringDefault, stringFinished, stringWorking):
        theFont = pygame.font.Font('OpenSans-Light.ttf', 20)

        if self.buttonStates[btnIndex] == 0:
            pygame.draw.rect(self.screen, self.coloursLibrary['button'], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * (btnIndex-1) + btnIndex * 10,
                self.buttonSize[0], self.buttonSize[1]), 4)
            theText = theFont.render(stringDefault, True, self.coloursLibrary['black'])
        elif self.buttonStates[btnIndex] == 1:
            pygame.draw.rect(self.screen, self.coloursLibrary['button'], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * (btnIndex-1) + btnIndex * 10,
                self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render(stringFinished, True, self.coloursLibrary['black'])
        elif self.buttonStates[btnIndex] == 2:
            pygame.draw.rect(self.screen, self.coloursLibrary['button'], (
                self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, self.buttonSize[1] * (btnIndex - 1) + btnIndex * 10,
                self.buttonSize[0], self.buttonSize[1]), 0)
            theText = theFont.render(stringWorking, True, self.coloursLibrary['black'])

        self.screen.blit(theText, (self.sizeOfTheWindow[0] - self.buttonSize[0] + 5, self.buttonSize[1] * (btnIndex-1) + btnIndex*10))


    def buttonConstructor(self):
        pygame.draw.rect(self.screen, self.coloursLibrary['backGround'],
                         (self.sizeOfTheWindow[0] - self.buttonSize[0] - 10, 0, self.buttonSize[0], self.sizeOfTheWindow[1]), 0)

        self.buttonPainter(1, "Index Hidden", "Index Displayed", "running")
        self.buttonPainter(2, "Hamiltonian Cycle?", "Hamiltonian Cycle!", "running")
        self.buttonPainter(3, "Phase 1", "Phase 1 Finished", "running")
        self.buttonPainter(4, "Phase 2 O(n^3)", "Phase 2 Finished", "running")
        self.buttonPainter(5, "Phase 2 O(n^2)", "Phase 2 Finished", "running")
        self.buttonPainter(6, "Phase 3", "Phase 3 Finished", "running")

        return


    def buttonsClicked(self, pos):
        # search button by the given coordinate

        indexOfButton = -1
        if pos[0] > self.sizeOfTheWindow[0] - self.buttonSize[0]:
            if pos[1] < self.buttonSize[1] + 10:  self.buttonStates[1] = 1 - self.buttonStates[1]
            elif pos[1] < self.buttonSize[1] * 2 + 20: self.buttonStates[2] = 1 - self.buttonStates[2]
            elif pos[1] < self.buttonSize[1] * 3 + 30:
                if self.buttonStates[3] == 0:
                    self.buttonStates[3] = 2
            elif pos[1] < self.buttonSize[1] * 4 + 40:
                if self.buttonStates[4] == 0:
                    self.buttonStates[4] = 2
            elif pos[1] < self.buttonSize[1] * 5 + 50:
                if self.buttonStates[5] == 0:
                    self.buttonStates[5] = 2
            elif pos[1] < self.buttonSize[1] * 6 + 60:
                if self.buttonStates[6] == 0:
                    self.buttonStates[6] = 2

        return





