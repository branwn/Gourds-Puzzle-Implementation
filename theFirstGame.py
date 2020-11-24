import pygame

class theFirstGame (object):

	def __init__(self):
		pygame.init()

		self.win = pygame.display.set_mode((500, 500))
		pygame.display.set_caption("First Game")

		self.x = 250
		self.y = 250
		self.width = 40
		self.heigh = 60
		self.vel = 5

		self.runTheGame()


	def runTheGame(self):
		isJump = False
		jumpCount = 10

		run = True
		while run:
			pygame.time.delay(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			keys = pygame.key.get_pressed()

			if keys[pygame.K_LEFT] and self.x > self.vel:
				self.x -= self.vel
			if keys[pygame.K_RIGHT] and self.x < 500 - self.width - self.vel:
				self.x += self.vel
			if not(isJump):
				if keys[pygame.K_UP] and self.y > self.vel:
					self.y -= self.vel
				if keys[pygame.K_DOWN] and self.y < 500 - self.heigh - self.vel:
					self.y += self.vel
				if keys[pygame.K_SPACE]:
					isJump = True
			else:
				if jumpCount >= -10:
					neg = 1
					if jumpCount < 0:
						neg = -1
					self.y -= (jumpCount ** 2 ) * 0.5 * neg
					jumpCount -= 1
				else:
					isJump = False
					jumpCount = 10

			self.win.fill((0,0,0))
			pygame.draw.rect(self.win, (133,60,45), (self.x, self.y, self.width, self.heigh))
			pygame.display.update()

		pygame.quit()

theFirstGame()