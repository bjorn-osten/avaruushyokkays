class Settings:
	"""A class to store all of the settings for Alien Invasion."""

	def __init__(self):

		"""Initialise the game's static settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		self.bullets_allowed = 8

		# Ship settings

		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 3.0
		self.bullet_height = 15
		self.bullet_color = (0, 255, 0)

		# Alien Settings
		self.fleet_drop_speed = 10
		

		# How quickly the game speeds up
		self.speedup_scale = 0.2

		# How quickly the alien points value increases 

		self.score_scale = 1.5


		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize setting that can change throughout the game"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.8

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		# Alien scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and Alien Points Value"""
		self.ship_speed += self.speedup_scale
		self.bullet_speed += self.speedup_scale
		self.alien_speed += self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
