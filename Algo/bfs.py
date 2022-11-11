from collections import deque
from Utils.func import reconstruct_path
import pygame


def BFS(draw, grid, start, end):
	came_from = {}
	visited = deque()
	open_hash = deque()
	open_hash.append(start)


	while open_hash:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		if open_hash[-1] == end or end in open_hash:
			reconstruct_path(came_from, end, draw, start)
			end.make_end()
			return True
			
		current = open_hash.popleft()
		visited.append(current)

		for neighbor in current.neighbors:					
			if neighbor not in visited and neighbor not in open_hash:
				came_from[neighbor] = current
				open_hash.append(neighbor)
				neighbor.make_open()		

		draw()

		if current != start:
			current.make_closed()

	return False