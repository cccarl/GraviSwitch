import pygame
from Wall import Wall
from Box import Box
from Spike import Spike
from Door import Door
from constants import BLOCK_SIZE
from Box_Filter import Box_Filter

def load_level(mapa):
	sprite_list = pygame.sprite.Group()
	updatable_list = pygame.sprite.Group() #Un grupo por tipo de accion a sprites.
	box_list = pygame.sprite.Group()
	col_list = pygame.sprite.Group()
	door_list = pygame.sprite.Group()
	bfilter_list = pygame.sprite.Group()
	
	id_given = 0
	door_id = 0
	pos_y = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(wall)
				col_list.add(wall)
				wall.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1 
			elif cuadro == 'P':
				p_inicio = (pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				p_id = id_given
				id_given += 1
			elif cuadro == 'B':
				box = Box(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(box)
				col_list.add(box)
				updatable_list.add(box)
				box_list.add(box)
				box.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1
			elif cuadro == 'S':
				spike = Spike(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(spike)
				col_list.add(spike)
				spike.ID = id_given
				id_given += 1
			elif cuadro == 'D':
				door = Door(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				door.exitID = door_id
				door_list.add(door)
				door_id += 1
			elif cuadro == 'F':
				bfilter = Box_Filter(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				bfilter_list.add(bfilter)
				bfilter.ID = id_given
				id_given += 1
			pos_x += 1
		pos_y += 1
	ex = bfilter_list, sprite_list, updatable_list, door_list, box_list, col_list, p_inicio, p_id
	return ex
