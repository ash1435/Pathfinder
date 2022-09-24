from queue import PriorityQueue
from Utils.func import reconstruct_path, h
import pygame
import time

def best(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}
	x = time.time()
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			print(time.time()-x)
			reconstruct_path(came_from, end, draw, start)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = f_score[current] + 1

			if temp_g_score < f_score[neighbor]:
				came_from[neighbor] = current
				f_score[neighbor] = h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False