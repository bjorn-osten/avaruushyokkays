import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialise the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load a ship image and get its rect

		self.image = pygame.image.load('images/ship.png').convert_alpha()
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom of the screen

		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ships horizontal position
		self.x = float(self.rect.x)

		# Movement flag

		self.moving_right = False
		self.moving_left = False

		super().__init__()

	def update(self):
		"""Update the ship's position based on movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		# Update rect object for self.x.

		self.rect.x = self.x 

	def centre_ship(self):
		"""Centre the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)