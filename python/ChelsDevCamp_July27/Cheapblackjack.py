class Deck:
	"""
	Class for handling a deck of cards.
	"""

	def __init__(self, cards_in_deck, num_decks=4):
		self.num_decks = num_decks
		self.cards_in_deck = []
		# self._build_deck()
		pass

	def deal(self, num_cards=1):
		"""
		input: num_cards
		returns: list of card(s)
		"""
		pass

	def _build_deck(self, cards):
		"""
		input: calls rand.shuffle on cards
		returns: a list of cards
		"""

class Card:
	"""
	Class of cards
	"""

	def __init__(self, face_value, real_value, suit):
		self.face_value = face_value
		self.real_value = real_value
		self.suit = suit

	def cheat(self, face_value):
		"""
		TODO cheats and changes value.
		"""
		pass

	def face_up(self):
		"""
		returns True cards is face up
		"""

	def print_card(self):
		"""
		pretty prints the card.
		"""
		pass

class Player:

	def __init__(self, hand, name, is_dealer=False):

		self.hand = hand
		self.name = name
		self.is_dealer = is_dealer

	def score(self):
		"""
		keeps track player score
		returns total points
		"""

		pass

	def hit_stay(self):
		"""
		Todo place holder for AI bot
		"""
		pass

	def ace_high_low(self, card):
		"""
		Sets card to low
		imput ace to change
		"""
		pass

	def new_card(self, new_card):
		"""
		Adds new card to hand
		imput new card
		return hand
		"""
		pass

	def print_hand(self):
		"""
		Prints players hand
		"""
		pass


class Game:

	def __init__(self, num_players):
		self.num_players = num_players
		self.players = []

	def winner(self, players):
		"""
		imput = player
		prints the hight score and winning player
		"""
		pass

	def define_players(self, num_players):
		"""
		imput num_players makes players
		returns player list
		"""
		pass

	def start_game(self, num_players):
		"""
		init deck
		"""
		pass

	def turn(self, player):
		"""
		promts user for hit or stay
		"""
		pass

	def main(self):
		"""
		kicks off game
		loops through the players and plays game
		"""
		pass




















