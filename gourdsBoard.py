import pygame
import numpy as np  # for matrix

pygame.init()
# size of the window
screen = pygame.display.set_mode((800, 600))
# caption setting
pygame.display.set_caption('Gourds')
# background colour setting
screen.fill((242, 242, 242))
# set width of the hexagonal cell
widthOfHexCell = 80;
offset = widthOfHexCell*1.7


# set a matrix of board
matrixOfBoard = np.array([[1, 0, 3], [0, 5, 0]])

# set a initial gourds placement
gourdsPlacement = np.array([[[1,1],[2,2],[255,0,0],[0,255,0]]])
gourdsColour = np.array([[[1,1],[2,2],[255,0,0],[0,255,0]]])

def boardConstructor():
    for i in range(len(matrixOfBoard)):
        for j in range(len(matrixOfBoard[0])):
            pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)
            if(matrixOfBoard[i][j]):
                # draw a hexagonal cell
                pygame.draw.polygon(screen, (100, 100, 200,),
                                    [(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 1.1547), (
                                    offset + j * widthOfHexCell + widthOfHexCell,
                                    offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735), (
                                     offset + j * widthOfHexCell + widthOfHexCell,
                                     offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735),
                                     (offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 1.1547),
                                     (offset + j * widthOfHexCell - widthOfHexCell,
                                      offset + i * widthOfHexCell * 1.732 - widthOfHexCell * 0.57735), (
                                     offset + j * widthOfHexCell - widthOfHexCell,
                                     offset + i * widthOfHexCell * 1.732 + widthOfHexCell * 0.57735)], 1)

    # refresh the window
    pygame.display.flip()

def gourdsConstructor():
    for i in range(len(gourdsPlacement)):
        pygame.draw.circle(screen,(255,0,0),(offset + 1 * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,widthOfHexCell*0.6,0)
        print(i[0][0])
    # refresh the window
    pygame.display.flip()
    
def main():
    # 开启一个事件循环处理发生的事件
    running = True
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    boardConstructor()
    gourdsConstructor()
    main()
