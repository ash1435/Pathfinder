from collections import deque
from queue import PriorityQueue
from Utils.func import reconstruct_path
import pygame


def dualbfs(draw, grid, start, end):
	came_from_start = {}
	came_from_end = {}

	visited_start = deque()
	open_hash_start = deque()
	open_hash_start.append(start)

	visited_end = deque()
	open_hash_end = deque()
	open_hash_end.append(end)


	while open_hash_start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			
		current_start = open_hash_start.popleft()
		visited_start.append(current_start)

		current_end = open_hash_end.popleft()
		visited_end.append(current_end)

		for neighbor in current_start.neighbors:					
			if neighbor not in visited_start and neighbor not in open_hash_start:
				came_from_start[neighbor] = current_start
				open_hash_start.append(neighbor)
				neighbor.make_open()		

			if neighbor in open_hash_end:
				reconstruct_path(came_from_start, neighbor, draw, start)
				reconstruct_path(came_from_end, neighbor, draw, end)
				end.make_end()
				neighbor.make_path()
				return True

		for neighbor in current_end.neighbors:		
			if neighbor not in visited_end and neighbor not in open_hash_end:
				came_from_end[neighbor] = current_end
				open_hash_end.append(neighbor)
				neighbor.make_open()		

			if neighbor in open_hash_start:
				reconstruct_path(came_from_end, neighbor, draw, end)
				reconstruct_path(came_from_start, neighbor, draw, start)
				end.make_end()
				neighbor.make_path()
				return True

		draw()

		if current_start != start:
			current_start.make_closed()
			
		if current_end != end:
			current_end.make_closed()

	return False