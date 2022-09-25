import pygame
from Utils.spots import *
from Utils.constants import font
import os


def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw, start):
	while current in came_from:
		current = came_from[current]
		if current != start:
			current.make_path()
		draw()

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def draw_text(text, font, color, win, x, y):
	text = font.render(text, 1, color)
	text_rect = text.get_rect()
	text_rect.center = (x, y)
	win.blit(text, text_rect)

def draw_menu(win):
	win.fill(WHITE)
	if 'unknown.png' in os.listdir('Utils'):
		BackGround = Background('Utils/unknown.png', [0,0])
		win.blit(BackGround.image, BackGround.rect)
	draw_text('Pathfinding', font, BLACK, win, 410, 70)
	draw_text('Visualizer', font, BLACK, win, 410, 140)
	pygame.display.update()

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col