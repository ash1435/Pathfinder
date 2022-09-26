import pygame
from Utils.spots import *
from Utils.constants import font, font2
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
	click = False
	win.fill(WHITE)
	if 'unknown.png' in os.listdir('Utils'):
		BackGround = Background('Utils/unknown.png', [0,0])
		win.blit(BackGround.image, BackGround.rect)

	draw_text('Pathfinder', font, BLACK, win, 410, 150)

	draw_text('BREADTH FIRST', font2, BLACK, win, 175, 425)
	draw_text('BEST FIRST', font2, BLACK, win, 175, 495)
	draw_text('A STAR', font2, BLACK, win, 395, 425)
	draw_text('DUAL BFS', font2, BLACK, win, 395, 495)
	draw_text('BEST FIRST', font2, BLACK, win, 615, 425)

	button_1 = pygame.Rect(75, 400, 200, 50)
	button_2 = pygame.Rect(75, 470, 200, 50)
	button_3 = pygame.Rect(295, 400, 200, 50)
	button_4 = pygame.Rect(295, 470, 200, 50)
	button_5 = pygame.Rect(515, 400, 200, 50)
	button_6 = pygame.Rect(515, 470, 200, 50)
	
	pygame.draw.rect(win, (200, 200, 200), button_1, 2, 3)
	pygame.draw.rect(win, (200, 200, 200), button_2, 2, 3)
	pygame.draw.rect(win, (200, 200, 200), button_3, 2, 3)
	pygame.draw.rect(win, (200, 200, 200), button_4, 2, 3)
	pygame.draw.rect(win, (200, 200, 200), button_5, 2, 3)
	pygame.draw.rect(win, (200, 200, 200), button_6, 2, 3)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if 275 > mouse[0] > 75 and 450 > mouse[1] > 400:
		pygame.draw.rect(win, (200, 100, 100), button_1, 2, 3)
	if 275 > mouse[0] > 75 and 520 > mouse[1] > 470:
		pygame.draw.rect(win, (200, 100, 100), button_2, 2, 3)
	if 495 > mouse[0] > 295 and 450 > mouse[1] > 400:
		pygame.draw.rect(win, (200, 100, 100), button_3, 2, 3)
	if 495 > mouse[0] > 295 and 520 > mouse[1] > 470:
		pygame.draw.rect(win, (200, 100, 100), button_4, 2, 3)
	if 715 > mouse[0] > 515 and 450 > mouse[1] > 400:
		pygame.draw.rect(win, (200, 100, 100), button_5, 2, 3)

	smallText = pygame.font.SysFont("comicsansms",20)
    # textSurf, textRect = text_objects(msg, smallText)
    # textRect.center = ( (x+(w/2)), (y+(h/2)) )
    # gameDisplay.blit(textSurf, textRect)

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