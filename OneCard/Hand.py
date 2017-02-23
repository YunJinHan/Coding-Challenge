
# One Card - Hand

class TurnList :

	def __init__(self):
		self.List = []
		self.__count = 0

	def Add(self,player):
		self.List.append(player)
		self.__count+=1

	def Remove(self,count):
		self.List.pop(count)
		self.__count-=1

	@property
	def getCount(self):
		return self.__count


class Player :

	def __init__(self,name):
		self.__name = name
		self.__card = []
		self.__card_count = 0

	def getCard(self,card):
		self.__card.append(card)
		self.__card_count += 1

	def RemoveCard(self,number):
		self.__card.pop(number-1)
		self.__card_count -= 1

	def ReturnCard2(self,count):
		return self.__card[count]

	@property
	def ReturnCard(self):
		return self.__card

	@property
	def getName(self):
		return self.__name	

	@property
	def getCard_Count(self):
		return int(self.__card_count)

	@property
	def player_card_empty(self):
		return self.__card_count == 0
