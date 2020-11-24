import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    screen.fill((242, 242, 242))

    #draw a hex
    x, y, r = 100,100,30   
    pygame.draw.polygon(screen, (140, 20, 20,), [(x, y+r*1.1547), (x+r, y+r*0.57735), (x+r, y-r*0.57735), (x, y-r*1.1547), (x-r, y-r*0.57735), (x-r, y+r*0.57735)], 0)
	
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