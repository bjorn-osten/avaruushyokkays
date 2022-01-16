class GameStats:
	"""Track Stats for Alien Invasion"""
	def __init__(self, ai_game):
		"""Initialise Statisitcs"""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start Alien Invasion in an active state
		self.game_active = False
		# High score should NEVER reset
		self.high_score = 0

	def reset_stats(self):
		"""Initialise Stats that can be chaged inside game itself"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		

