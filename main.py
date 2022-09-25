from Utils.func import *
from Algo import astar, best, bfs, bidirectionalbfs, bidirectionalgreedy
import keyboard


def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = False
	
	while not run:
		draw_menu(win)
		if keyboard.is_pressed('space'):
			run = True
		if keyboard.is_pressed('escape') or keyboard.is_pressed('backspace'):
			break

	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT or keyboard.is_pressed('backspace'):
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					while run:						
						draw_menu(win)
						for event in pygame.event.get():
							if event.type == pygame.QUIT or keyboard.is_pressed('backspace'):
								run = False
						if keyboard.is_pressed('space'):
							start = None
							end = None
							grid = make_grid(ROWS, width)
							break


			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					# bidirectionalgreedy.dualbest(lambda: draw(win, grid, ROWS, width), grid, start, end)
					best.best(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

main(WIN, 800)
