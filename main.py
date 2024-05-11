import sys
import os
import string
import pygame
#from Character import character

window_size = 600
key = 12
end_level = False
tile_size = window_size / key
window = pygame.display.set_mode((window_size, window_size))
tile_color = (127, 127, 127)
winning_color = (255, 0, 0)
background_color = (0, 0, 0)
ending_y = -1
ending_x = -1

class Character:
	def __init__(self):
		self.x = window_size/2
		self.y = 0

	def update(self, level, change_x, change_y):
		new_x = self.x + change_x
		new_y = self.y + change_y

		# Prevent player from moving off screen horizontally
		if new_x < 0:
			new_x = 0
		elif new_x > 600:
			new_x = 600

		# Prevent player from moving off screen vertically
		if new_y < 0:
			new_y = 0
		elif new_y > 600:
			new_y = 600

		# return if there's a collision (true)
		if self.collide(level, new_x, new_y):
			new_x = self.x  #+ change_x
			new_y = self.y #+ change_y # this stops the player from moving

		# Update the player position to the new position
		self.x = new_x
		self.y = new_y

		# Check if the player is in the end
	def player_winning(self):
		grid_x = int(self.x / (600 / key))
		grid_y = int(self.y / (600 / key))
		if self.x >= 0 and self.x < 600 and self.y >= 0 and self.y < 600 and level.maze[grid_y][grid_x] == 2:
			return True
		else: return False


	def collide(self, level, check_x, check_y):
		maze_x = int(check_x / (600 / key))
		maze_y = int(check_y / (600 / key))

		# Collisions happen if the player is on-screen and trying to move into a wall
		# since I want a secret passage maze_x which is the index should only return a collsion when it is
		# less than key not equal to that way they can be on index 12 without issues
		if maze_x < key and maze_y < key and level.maze[maze_y][maze_x] == 1:
			#print("Collide!")
			return True
		else:
			return False

	def draw(self):
		pygame.draw.rect(window, (0,0,127), pygame.Rect(self.x, self.y, 600/key, 600/key))

class level_template:
	def __init__(self, filename):
		self.maze = []

		with open("maze_code.txt", "r") as maze_data:
			file = ''.join(maze_data.read().split()) # Read file & remove all whitespace

			# Generate maze data from file
			for i in range(0, len(file)):
				if i % key == 0: # New row
					self.maze.append([])

				# Map '_' to 0 and 'x' to 1
				if file[i] == '_':
					self.maze[i // key].append(0)
				elif file[i] == 'x':
					self.maze[i // key].append(1)
				elif file[i] == '+':
					self.maze[i // key].append(2)
	def draw(self):
		for y in range(0, key):
			for x in range(0, key):
				color = background_color

				if self.maze[y][x] == 1:
					color = tile_color
				elif self.maze[y][x] == 2:
					color = winning_color


				pygame.draw.rect(window, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))

class Level1(level_template):


	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				# Move the player
				if event.key == pygame.K_RIGHT:
					player.update(level, 600 / key, 0)
				if event.key == pygame.K_LEFT:
					player.update(level, -600 / key, 0)
				if event.key == pygame.K_UP:
					player.update(level, 0, -600 / key)
				if event.key == pygame.K_DOWN:
					player.update(level, 0, 600 / key)




player = Character()
level = Level1("maze_code.txt")
class Level2(level_template):
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				# Move the player
				if event.key == pygame.K_LEFT:
					player.update(level, 600 / key, 0)
				if event.key == pygame.K_RIGHT:
					player.update(level, -600 / key, 0)
				if event.key == pygame.K_DOWN:
					player.update(level, 0, -600 / key)
				if event.key == pygame.K_UP:
					player.update(level, 0, 600 / key)

class Level3(level_template):
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				# Move the player
				if event.key == pygame.K_UP:
					player.update(level, 600 / key, 0)
				if event.key == pygame.K_DOWN:
					player.update(level, -600 / key, 0)
				if event.key == pygame.K_LEFT:
					player.update(level, 0, -600 / key)
				if event.key == pygame.K_RIGHT:
					player.update(level, 0, 600 / key)

class Level4(level_template):
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				# Move the player
				if event.key == pygame.K_UP:
					player.update(level, 600 / key, 0)
				if event.key == pygame.K_DOWN:
					player.update(level, -600 / key, 0)
				if event.key == pygame.K_LEFT:
					player.update(level, 0, -600 / key)
				if event.key == pygame.K_RIGHT:
					player.update(level, 0, 600 / key)

def run_level_1():
	while True:
		level.check_events()
		level.draw()
		player.draw()
		if player.player_winning():
			break
		pygame.display.flip()

def run_level_2():
	player.x = window_size/2
	player.y = 0
	level = Level2("maze_code.txt")
	while True:
		level.check_events()
		level.draw()
		player.draw()
		if player.player_winning():
			break
		pygame.display.flip()


def run_level_3():
	player.x = window_size/2
	player.y = 0
	level = Level3("maze_code.txt")
	while True:
		level.check_events()
		level.draw()
		player.draw()
		if player.player_winning():
			break
		pygame.display.flip()


def run_level_4():
	player.x = window_size/2
	player.y = 0
	level = Level4("maze_code.txt")
	while True:
		level.check_events()
		level.draw()
		player.draw()
		if player.player_winning():
			print("YOU WON")
			break
		pygame.display.flip()
player = Character()


if __name__ == '__main__':
	pygame.init()
	run_level_1()
	print("Congratulations you beat level 1, but now it's going to get trickier.")
	run_level_2()
	print("Give up.")
	run_level_3()
	print("mid.")
	run_level_4()
