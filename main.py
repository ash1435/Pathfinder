from Utils.func import *
from Algo import astar, best, bfs, bidirectionalbfs, bidirectionalgreedy
import keyboard


def main(win, width, algo):
	ROWS =70
	grid = make_grid(ROWS, width)

	start = None
	end = None
	run = True


	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT or keyboard.is_pressed('backspace'):
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					while run:						
						draw_menu(win)

						mouse = pygame.mouse.get_pos()
						click = pygame.mouse.get_pressed()

						if 275 > mouse[0] > 75 and 450 > mouse[1] > 400:
							if click[0] == 1:
								algo = 0
								start = None
								end = None
								grid = make_grid(ROWS, width)
								break

						if 275 > mouse[0] > 75 and 520 > mouse[1] > 470:
							if click[0] == 1:
								algo = 1
								start = None
								end = None
								grid = make_grid(ROWS, width)
								break

						if 495 > mouse[0] > 295 and 450 > mouse[1] > 400:
							if click[0] == 1:
								algo = 2
								start = None
								end = None
								grid = make_grid(ROWS, width)
								break
								
						if 495 > mouse[0] > 295 and 520 > mouse[1] > 470:
							if click[0] == 1:
								algo = 3
								start = None
								end = None
								grid = make_grid(ROWS, width)
								break

						if 715 > mouse[0] > 515 and 450 > mouse[1] > 400:
							if click[0] == 1:
								algo = 4
								start = None
								end = None
								grid = make_grid(ROWS, width)
								break


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
							
					if algo == 0:
						bfs.BFS(lambda: draw(win, grid, ROWS, width), grid, start, end)
					if algo == 1:
						best.best(lambda: draw(win, grid, ROWS, width), grid, start, end)					
					if algo == 2:
						astar.algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
					if algo == 3:
						bidirectionalbfs.dualbfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
					if algo == 4:
						bidirectionalgreedy.dualbest(lambda: draw(win, grid, ROWS, width), grid, start, end)
					

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)
	
	pygame.quit()

main(WIN, 1000, 0)
