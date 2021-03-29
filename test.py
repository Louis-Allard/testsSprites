import pygame
import time

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
rectScreen = screen.get_rect()
pygame.display.set_caption("test sprite moves")


class Personnage(pygame.sprite.Sprite):

	spriteSheet = pygame.image.load("advnt_full.png").convert_alpha()
	sequences = [(0, 1, False), (1, 6, True), (7, 3, False)]
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0, 0, 32, 64))
		self.rect = pygame.Rect(0, 0, 32, 64)
		self.rect.bottom = HEIGHT
		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False
		self.deltaTime = 0
		self.vitesse = 5

	def update(self, time):
		self.deltaTime = self.deltaTime + time
		if self.deltaTime >= 150:
			self.deltaTime = 0
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
            # (NumSprite%NbrColonne*W_Celulle, NumSprite//NbrColonne*H_Celulle, W_sprite,H_sprite)
			self.image = Personnage.spriteSheet.subsurface(
			    pygame.Rect(n % 10*32, n//10*64, 32, 64))
			if self.flip:
				self.image = pygame.transform.flip(self.image, True, False)
			self.numeroImage = self.numeroImage+1
			if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
				if Personnage.sequences[self.numeroSequence][2]:
					self.numeroImage = 0
				else:
					self.numeroImage = self.numeroImage-1

	def setSequence(self, n):
		if self.numeroSequence != n:
			self.numeroImage = 0
			self.numeroSequence = n

	def goRight(self):
		self.rect = self.rect.move(self.vitesse, 0).clamp(rectScreen)
		self.flip = False
		self.setSequence(1)

	def goLeft(self):
		self.rect = self.rect.move(-self.vitesse, 0).clamp(rectScreen)
		self.flip = True
		self.setSequence(1)

	def goDown(self):
		self.flip = False
		self.setSequence(2)   

def main():
    clock = pygame.time.Clock()
    time = clock.tick(60)
    game_over = False
    perso = Personnage()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    perso.goLeft()
                if event.key == pygame.K_RIGHT:
                    perso.goRight()
                if event.key == pygame.K_DOWN:
                    perso.goDown()    
            if event.type == pygame.KEYUP:
                perso.setSequence(0)       

        perso.update(time)
        screen.fill(pygame.Color("white"))
        screen.blit(perso.image,perso.rect)
        pygame.display.update()

main()
pygame.quit()
quit()

