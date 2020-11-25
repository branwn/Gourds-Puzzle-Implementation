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
offset = widthOfHexCell


# set a matrix of board
matrixOfBoard = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0]])

# set a initial gourds placement
#                           x, y, x, y
gourdsLocation = np.array([[2, 1, 3, 2]])


def boardConstructor():

    font = pygame.font.Font('OpenSans-Light.ttf', 16)

    for i in range(len(matrixOfBoard)):
        for j in range(len(matrixOfBoard[0])):
            #display matrix
            text = font.render(str(matrixOfBoard[i][j]), True, (0, 0, 255))
            screen.blit(text, (-4 + offset + j * widthOfHexCell, -12 + offset + i * widthOfHexCell * 1.732))
            # pygame.draw.circle(screen,(0,0,0),(offset + j * widthOfHexCell, offset + i * widthOfHexCell * 1.732) ,6,1)

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
    for i in range(len(gourdsLocation)):
        pygame.draw.circle(screen, (100,0,0), (offset + gourdsLocation[i][0] * widthOfHexCell, offset + gourdsLocation[i][1] * widthOfHexCell * 1.732), widthOfHexCell * 0.5, 1)
        pygame.draw.circle(screen, (100,0,0), (offset + gourdsLocation[i][2] * widthOfHexCell, offset + gourdsLocation[i][3] * widthOfHexCell * 1.732), widthOfHexCell * 0.5, 1)
        pygame.draw.line(screen, (100,0,0), (offset + gourdsLocation[i][0] * widthOfHexCell, offset + gourdsLocation[i][1] * widthOfHexCell * 1.732), (offset + gourdsLocation[i][2] * widthOfHexCell, offset + gourdsLocation[i][3] * widthOfHexCell * 1.732), width=1)
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
