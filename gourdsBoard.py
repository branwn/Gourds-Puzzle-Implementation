import pygame
import numpy as np  # for matrix

def main():
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # caption setting
    pygame.display.set_caption('Gourds Board')
    # background colour setting
    screen.fill((242, 242, 242))
    # set width of the hexagonal cell
    widthOfHex = 80;
    # draw a matrix with offsets in even rows
    nd_two = np.array([[1, 0, 3], [0, 5, 0]])
    offset = 100
    for i in range(len(nd_two)):
        for j in range(len(nd_two[0])):
            if(nd_two[i][j]):
                pygame.draw.circle(screen, (0,0,0), [offset+j*widthOfHex, offset+i*widthOfHex*1.732], 8, 1)
                # draw a hexagonal cell
                pygame.draw.polygon(screen, (100, 100, 200,),
                                    [(offset + j * widthOfHex, offset + i * widthOfHex * 1.732 + widthOfHex * 1.1547), (
                                    offset + j * widthOfHex + widthOfHex,
                                    offset + i * widthOfHex * 1.732 + widthOfHex * 0.57735), (
                                     offset + j * widthOfHex + widthOfHex,
                                     offset + i * widthOfHex * 1.732 - widthOfHex * 0.57735),
                                     (offset + j * widthOfHex, offset + i * widthOfHex * 1.732 - widthOfHex * 1.1547),
                                     (offset + j * widthOfHex - widthOfHex,
                                      offset + i * widthOfHex * 1.732 - widthOfHex * 0.57735), (
                                     offset + j * widthOfHex - widthOfHex,
                                     offset + i * widthOfHex * 1.732 + widthOfHex * 0.57735)], 1)

    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
