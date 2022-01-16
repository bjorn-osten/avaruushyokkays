import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a singe alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialise alien and set its starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and set its rect attribute
		self.image = pygame.image.load('images/469156.png').convert_alpha()
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()


		# Start each new alien at the top left of the screen

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the aliens exact position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return True if the alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Move the alien to the right"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

