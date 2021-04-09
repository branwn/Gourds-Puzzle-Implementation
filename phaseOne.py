import pygame
class phaseOne(object):

    def __init__(self, BoardConfig, gourdsConstructor, HCycle):
        self.myBoardConfig = BoardConfig
        self.myGourdsConstructor = gourdsConstructor
        self.myHCycle = HCycle
        self.firstRun = True

    def runPhaseOne(self, buttonState3):
        if not buttonState3:
            self.firstRun = True
            return
        if not self.firstRun: return
        self.firstRun = False



        self.myGourdsConstructor.gourdsClicked([ 4, 2], 'a')


        print("run phase one")

