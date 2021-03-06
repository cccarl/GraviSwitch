import pygame
import sound
from misc_functions import get_image
from constants import CHROMA_KEY

class Checkpoint(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		
		self.ani1 = []
		self.ani1_frame = 0 #60 frames total (1 sec of animation)
		ani1_cod = [(0,0),(32,0),(64,0),(96,0)]
		ani1_sheet = pygame.image.load('images/tiles/checkpoint.png').convert()
		
		for i in ani1_cod:
			cuadro = get_image(ani1_sheet, i[0], i[1], 32,32).convert()
			cuadro.set_colorkey(CHROMA_KEY)
			self.ani1.append(cuadro)
		
		self.image = self.ani1[0]
		
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
		
	def reboot(self):
		self.image = self.ani1[0]

	def ani1_play(self):
		if self.image == self.ani1[0] and self.ani1_frame >= 15:
			self.image = self.ani1[1]
			sound.checkpoint.play()
		elif self.image == self.ani1[1] and self.ani1_frame >= 30:
			self.image = self.ani1[2]
		elif self.image == self.ani1[2] and self.ani1_frame >= 45:
			self.image = self.ani1[3]
			
