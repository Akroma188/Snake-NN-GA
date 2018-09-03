import pygame
import time
#pylint: disable=E1101


# Size of window -------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# TODO gonna add window extension for info and neural net


# Size of each block - apple and snake 
BLOCK_SIZE = 20
FPS = 20

# Colors for the game --------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
yellow=(200, 200, 0)
light_yellow = (255, 255, 0)
RED = (255, 0, 0)
light_red = (255, 0, 0)
GREEN = (0, 155, 0)
light_green = (0, 255, 0)
BACKGROUND = (62, 62, 62)



class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('My Snake')
		self.clock = pygame.time.Clock()
		self.snakeHead = pygame.image.load('images/head.png')
		self.bodyPart = pygame.image.load('images/body.png')

		# Fonts ---------------------------
		self.small_font = pygame.font.SysFont('verdana', 25)  # size font 25
		self.medium_font = pygame.font.SysFont('verdana', 50)  # size font 50
		self.large_font = pygame.font.SysFont('verdana', 70)  # size font 70
	# Functions to display Text ------------------------------------------
	def text_objects(self, text, color, size):
		if size == 'small':
			textSurface = self.small_font.render(text, True, color)
		elif size == 'medium':
			textSurface = self.medium_font.render(text, True, color)
		elif size == 'large':
			textSurface = self.large_font.render(text, True, color)
		
		return textSurface, textSurface.get_rect()

	def message_to_screen(self, msg, color, y_displace = 0, size = 'small'):
		texSurf, textRect = self.text_objects(msg, color, size)
		textRect.center = (WINDOW_WIDTH/2), (WINDOW_HEIGHT/2) + y_displace
		self.screen.blit(texSurf, textRect)
	def score(self, score):
		text = self.small_font.render("Score: " + str(score), True, WHITE)
		self.screen.blit(text, [0,0])

	def print_time(self, time):
		text = self.small_font.render("TIME_STEP: " + str(time), True, WHITE)
		self.screen.blit(text, [0,WINDOW_HEIGHT - 80])

	def print_generation(self, generation):
		text = self.small_font.render("Generation: " + str(generation), True, WHITE)
		self.screen.blit(text, [500,0])

	def print_best_fitness(self, fitness):
		text = self.small_font.render("Fitness: " + str(fitness), True, WHITE)
		self.screen.blit(text, [0, WINDOW_HEIGHT - 35])

	# Funtions for Game Intro, Pause and Game Over -------------------------
	def game_intro(self):
		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						intro = False
					if event.key == pygame.K_q:
						pygame.quit()
						quit()

			self.screen.fill(BACKGROUND)
			self.message_to_screen('Welcome to Snake 2.0', GREEN, -100, 'large')
			self.message_to_screen('Eat apple to improve your score', WHITE, -30)
			self.message_to_screen('The more you eat the bigger you get', WHITE, 10)
			self.message_to_screen('Enjoy yourself and try not to die!', WHITE, 50)
			self.message_to_screen('Press C to play, P to Pause and Q to quit', WHITE, 180)
			pygame.display.flip()
			self.clock.tick(10)

	def pause(self):
		paused = True
		#gameDisplay.fill(white)
		self.message_to_screen('Pause', WHITE, -100, 'large')
		self.message_to_screen('Press C to continue or Q to Quit', WHITE, 25, 'small')
		pygame.display.flip()
		self.clock.tick(10)
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
						quit()

	# Draw Snake ---------------------------------------------
	def draw_snake(self, head, body, direction, head_img, body_img):
		if direction == "RIGHT":
			headPart = head_img
		if direction == "LEFT":
			headPart = pygame.transform.rotate(head_img, 180)
		if direction == "UP":
			headPart = pygame.transform.rotate(head_img, 90)
		if direction == "DOWN":
			headPart = pygame.transform.rotate(head_img, 270)

		self.screen.blit(headPart, (head[0], head[1]))  # make the head

		# Body 
		for pos in body[1:]:
			self.screen.blit(body_img, (pos[0], pos[1]))

	def drawApple(self, apple_pos):
		pygame.draw.rect(self.screen, RED, (apple_pos[0], apple_pos[1], BLOCK_SIZE, BLOCK_SIZE))
