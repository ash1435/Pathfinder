from queue import PriorityQueue
from Utils.func import reconstruct_path, h
import pygame
import time

def dualbest(draw, grid, start, end):
	count_start = 0
	count_end = 0

	open_set_start = PriorityQueue()
	open_set_start.put((0, count_start, start))

	open_set_end = PriorityQueue()
	open_set_end.put((0, count_end, end))

	came_from_start = {}
	came_from_end = {}

	f_score_start = {spot: float("inf") for row in grid for spot in row}
	f_score_start[start] = h(start.get_pos(), end.get_pos())

	f_score_end = {spot: float("inf") for row in grid for spot in row}
	f_score_end[end] = h(start.get_pos(), end.get_pos())

	open_set_hash_start = {start}
	open_set_hash_end = {end}

	x = time.time()

	while not open_set_start.empty() and not open_set_end.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current_start = open_set_start.get()[2]
		open_set_hash_start.remove(current_start)

		current_end = open_set_end.get()[2]
		open_set_hash_end.remove(current_end)

		# if current == end:
		# 	reconstruct_path(came_from, end, draw, start)
		# 	end.make_end()
		# 	return True
		
		for neighbor in current_start.neighbors:
			temp_g_score_start = f_score_start[current_start] + 1

			if temp_g_score_start < f_score_start[neighbor]:
				came_from_start[neighbor] = current_start
				f_score_start[neighbor] = h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash_start:
					count_start += 1
					open_set_start.put((f_score_start[neighbor], count_start, neighbor))
					open_set_hash_start.add(neighbor)
					neighbor.make_open()
				
				if neighbor in open_set_hash_end:
					print(time.time()-x)
					reconstruct_path(came_from_start, neighbor, draw, start)
					reconstruct_path(came_from_end, neighbor, draw, end)
					end.make_end()
					neighbor.make_path()
					return True

		for neighbor in current_end.neighbors:
			temp_g_score_end = f_score_end[current_end] + 1

			if temp_g_score_end < f_score_end[neighbor]:
				came_from_end[neighbor] = current_end
				f_score_end[neighbor] = h(neighbor.get_pos(), start.get_pos())
				if neighbor not in open_set_hash_end:
					count_end += 1
					open_set_end.put((f_score_end[neighbor], count_end, neighbor))
					open_set_hash_end.add(neighbor)
					neighbor.make_open()
			if neighbor in open_set_hash_start:
				print(time.time()-x)
				reconstruct_path(came_from_start, neighbor, draw, start)
				reconstruct_path(came_from_end, neighbor, draw, end)
				end.make_end()
				neighbor.make_path()
				return True


		draw()

		if current_start != start:
			current_start.make_closed()
		
		if current_end != end:
			current_end.make_closed()

	return False