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

        self.buttonPainter(1, "<- Prev.", "<-     ", "running")
        self.buttonPainter(2, "Next ->", "        ->", "running")

        self.buttonPainter(8, "Start", "Finished", "running")

        return


    def buttonsClicked(self, pos):
        # search button by the given coordinate

        indexOfButton = -1
        if pos[0] > self.sizeOfTheWindow[0] - self.buttonSize[0]:
            if pos[1] < self.buttonSize[1] + 10:
                if self.buttonStates[1] == 0:
                    self.buttonStates[1] = 2
            elif pos[1] < self.buttonSize[1] * 2 + 20:
                if self.buttonStates[2] == 0:
                    self.buttonStates[2] = 2
            elif pos[1] < self.buttonSize[1] * 7 + 70:
                pass
            elif pos[1] < self.buttonSize[1] * 8 + 80:
                if self.buttonStates[8] == 0:
                    self.buttonStates[8] = 2

        return





