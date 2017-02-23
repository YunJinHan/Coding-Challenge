
# One Card - Card

import random

class Card:
	
	class pips:
		Ace = 1
		Jack = 11
		Queen = 12
		King = 13
		ColorJoker = 14
		BlackJoker = 15
	## 카드 숫자

	class suits:
		Club = 1
		Diamond = 2
		Heart = 3
		Spade = 4
		Joker = 5
	## 카드 모양

	class abilities:
		Attack = 100
		Jump = 101
		Revers = 102
		Onemore = 103
		Suitchange = 104
	## 카드 능력

	def __init__(self,suit,pip):

		self.__suit = suit
		self.__pip = pip
		self.__priority = 0
		self.__ability = 0

		if self.__pip == self.pips.Ace:
			if self.__suit==self.suits.Spade:
				self.__priority = 3
				self.__ability = 5
			else :
				self.__priority = 2
				self.__ability = 3

		elif self.__pip == 2:
			self.__priority = 1
			self.__ability = 2

		elif self.__pip == 7:
			self.__ability = self.abilities.Suitchange

		elif self.__pip == self.pips.Jack:
			self.__ability = self.abilities.Jump

		elif self.__pip == self.pips.Queen:
			self.__ability = self.abilities.Revers

		elif self.__pip == self.pips.King:
			self.__ability = self.abilities.Onemore

		elif self.__pip == self.pips.ColorJoker:
			self.__ability = 10
			self.__priority = 3

		elif self.__pip == self.pips.BlackJoker:
			self.__ability = 7
			self.__priority = 3

	def IsSameRank(self,card):
		if (self.__suit == card.ReturnSuit or self.__pip == card.ReturnPip or \
			self.__suit == 5 or card.ReturnSuit == 5):
			return True
		else :
			return False

	def IsHighPriority(self,card):
		if self.__pip == card.ReturnPip:
			return True
		elif self.__priority >= card.ReturnPropery :
			return ((self.__suit == card.ReturnSuit) or (self.__suit == 5))

	@property
	def ReturnPip(self):
		return int(self.__pip)

	@property
	def ReturnSuit(self):
		return self.__suit
	
	@property
	def ReturnPropery(self):
		return self.__priority

	@staticmethod
	def fresh_deck():
		cards = []
		for s in range(1,5):
			for r in range(1,14):
				cards.append(Card(s,r))
		cards.append(Card(5,14))
		cards.append(Card(5,15))
		random.shuffle(cards)
		return cards

class Deck:

	def __init__(self):
		self.__deck = Card.fresh_deck()

	def shuffle(self):
		return random.shuffle(self.__deck)

	def GetCard(self):
		if not self.IsEmpty():
			return self.__deck.pop()

	def IsEmpty(self):
		return len(self.__deck)==0

	def Add(self,card):
		return self.__deck.append(card)

