
# kernel 160 x 40 크기에서 최적화 실행
# One Card - Controller

import datetime
from Card import *
from View import *
from Hand import *

class OneCard :

	def __init__(self,count,names):

		self.First = True
		self.deck = Deck()
		## 카드 덱
		self.bottom_card = []
		## 맨 위가 현재 카드
		self.TurnList = TurnList()
		## 플레이 순서
		self.onemore = False
		## 한번 더 True 일때 nextTurn 에서 바꾸지 않고 한번더함
		self.Reverse = False
		## 순서가 뒤로 바뀔때 True로 바꿔줌
		self.Jump = False
		## 점프할때 True로 바꿔줌
		self.attackPoint = 0
		## 공격 포인트
		self.Change_Suit = False
		## 7 일때 True 로 바꿔줌
		self.Changed_Suit = 0
		## Change_Suit 가 True 이면 1~4 중 한개 선택
		self.highpass = False
		## 조커 공격을 방어하지 못하고 카드를 먹은 후에는 아무 카드나 낼 수 있다.
		self.midhighpass = False
		## 2 / A 공격을 방어하지 못하고 카드를 먹은 후에는 공/방 상관없이 맞는 무늬 / 숫자
		## 카드를 낼 수 있다.
		self.remessage = -1
		## 다음 사용자에게 현재 특수카드가 사용되었다고 알려줌.
		self.actionCard = -1
		## 특수카드를 사용한 플레이어 순서 번호

		for s in range(0,count):
			p = Player(names[s])
			for i in range(0,7):
				p.getCard(self.deck.GetCard())
			self.TurnList.Add(p)
		self.bottom_card.append(self.deck.GetCard())
		## 카드덱 생성 및 분배

	def From_Bottom_To_Deck(self):
		if (len(self.bottom_card)>=2):
			for _ in range(0,len(self.bottom_card)-1):
				self.deck.Add(self.bottom_card[0])
				self.bottom_card.pop(0)
				self.deck.shuffle()
	## 덱 카드가 모자랄 경우 바닥에 깔려있는 카드를 덱으로 옮김

	def jump(self):
		self.remessage = 1
		self.actionCard = self.TurnList.List[0]
		self.Jump = True
		Writer.inform_whatcard(self.TurnList.List[0].getName,1)
		for _ in range(0,2):
			a = self.TurnList.List.pop(0)
			self.TurnList.List.append(a)
	## J 카드를 냈을 때 다다음 플레이어로 턴이 넘어감
		
	def oneMore(self):
		self.remessage = 2
		self.actionCard = self.TurnList.List[0]
		self.onemore = True
		Writer.inform_whatcard(self.TurnList.List[0].getName,3)
	## K 카드를 냈을 때 해당 플레이어가 한번 더 플레이함

	def reverse(self):
		self.remessage = 3
		self.actionCard = self.TurnList.List[0]
		self.Reverse = True
		self.TurnList.List.reverse()
		Writer.inform_whatcard(self.TurnList.List[-1].getName,2)
	## Q 카드를 냈을 때 해당 플레이어 기준으로 턴을 역순으로 하여 플레이를 함

	def suitChange(self):
		self.Change_Suit = True
		self.Changed_Suit = Reader.get_choice_suit()
	## 7번 카드를 뽑았을때 무늬를 선택함c

	def nextTurn(self):
		if not (self.onemore or self.Reverse or self.Jump):
			a = self.TurnList.List.pop(0)
			self.TurnList.List.append(a)
		Writer.show_next_player_name(self.TurnList.List[0])
	## 다음 턴의 플레이어를 찾아줌

	def addCard(self,player):
		self.From_Bottom_To_Deck()
		c = self.deck.GetCard()
		player.getCard(c)
	## 카드를 덱에서 받아옴

	def IsAttackCard(self,card):
		if (card.ReturnSuit == 5): # 조커 
			if (card.ReturnPip == 14): # 컬러조커
				self.attackPoint += 7
			elif (card.ReturnPip == 15): # 흑백조커
				self.attackPoint += 5
		elif (card.ReturnPip == 1): # A
			self.attackPoint += 4
		elif (card.ReturnPip == 2): # 2
			self.attackPoint += 2
	## 현재 가지고 있는 카드가 공격 카드이면 공격 포인트를 올려줌

	def play(self,Round_count):
		
		Writer.start_game(Round_count)

		while True :

			if (self.remessage!=-1):
				if (self.remessage == 1):
					Writer.inform_whatcard(self.actionCard.getName,1)
				elif (self.remessage == 2):
					Writer.inform_whatcard(self.actionCard.getName,3)
				elif (self.remessage == 3):
					Writer.inform_whatcard(self.actionCard.getName,2)
			self.remessage = -1

			if (self.onemore):
				self.onemore = False

			if (self.Change_Suit):
				before = self.bottom_card[-1].ReturnSuit
				after = self.Changed_Suit
				if before == 1:
					be = "♧"
				elif before == 2:
					be = "◇"
				elif before == 3:
					be = "♡"
				elif before == 4:
					be = "♤"
				if after == 1:
					af = "♧"
				elif after == 2:
					af = "◇"
				elif after == 3:
					af = "♡"
				elif after == 4:
					af = "♤"
				Writer.show_change_suit(be,af)

			self.From_Bottom_To_Deck()
			if (self.First):
				self.IsAttackCard(self.bottom_card[0])
				self.First = False
			## 게임을 시작했을때 처음 깔린 카드가 공격 카드 인지 확인해줌
			Writer.show_attackPoint(self.attackPoint)
			Writer.show_player_name(self.TurnList.List[0])
			Writer.show_bottom_card(self.bottom_card)
			Writer.show_my_card(self.TurnList.List[0].ReturnCard)
				
			choice = Reader.get_choice_card("낼 카드를 선택하세요. (턴 종료 : -1) : ",1,len(self.TurnList.List[0].ReturnCard))
			while not ((choice == -1) or \
				## 플레이어가 낼 카드가 없을때
				(self.midhighpass and self.TurnList.List[0].ReturnCard2(choice-1).IsSameRank(self.bottom_card[-1])) or \
				## 2 / A 을 방어하지 못하고 그 다음 턴에 해당 카드 2 / A 카드의 무늬 / 숫자와 맞는 카드를 선택했을때
				(self.highpass) or \
				## Joker 카드를 방어하지 못하고 그 다음 턴에는 아무거 카드나 낼수 있음
				(self.TurnList.List[0].ReturnCard2(choice-1).IsSameRank(self.bottom_card[-1]) and \
				self.TurnList.List[0].ReturnCard2(choice-1).IsHighPriority(self.bottom_card[-1])) or \
				## 바닥에 깔려있는 카드와 무늬나 숫자가 같은 카드를 냈을때
				(self.Change_Suit and (self.TurnList.List[0].ReturnCard2(choice-1)).ReturnSuit == self.Changed_Suit)):
				## 이전 플레이어가 무늬를 바꾸었을때 해당 무늬를 가진 카드나 7 을 가진 카드를 낼 수 있음
				Writer.Wrong_choice()
				choice = Reader.get_choice_card("낼 카드를 선택하세요. (턴 종료 : -1) : ",1,len(self.TurnList.List[0].ReturnCard))
			
			self.Reverse = False
			self.Jump = False
			current_bottom_card = self.bottom_card[-1] # 내기 전 바닥에 있는 카드

			if choice == -1:
				if (self.attackPoint==0):
					self.addCard(self.TurnList.List[0])
				else :
					for _ in range(0,self.attackPoint):
						self.addCard(self.TurnList.List[0])
				## 현재 방어하지 못한 공격 포인트 만큼 카드를 덱에서 가져온다

				Writer.inform(self.TurnList.List[0].ReturnCard)

				self.attackPoint = 0
				## 카드를 먹은후 공격 포인트는 초기화 시킨다.
				if (current_bottom_card.ReturnSuit == 5):
					self.highpass = True
					## 조커 방어 못하고 카드 먹은후 아무거나 낼수 있다
				if (current_bottom_card.ReturnPip == 1 or current_bottom_card.ReturnPip == 2):
					self.midhighpass = True	
					## 나머지 공격 방어 못하고 카드 먹은후 숫자나 모양 맞는거만 낼수있다.
			
			else :

				self.Change_Suit = False

				if (self.highpass == True):
					self.attackPoint = 0
					self.highpass = False

				elif (self.midhighpass == True):
					self.attackPoint = 0
					self.midhighpass = False

				choice_card = self.TurnList.List[0].ReturnCard2(choice-1)
				self.TurnList.List[0].RemoveCard(choice) # 선택한 카드 냄
				self.bottom_card.append(choice_card) # 선택한 카드 바닥에 냄 


				# 낸 카드가 특수 카드 일때
				if (choice_card.ReturnPip == 11): # J
					self.jump()
				elif (choice_card.ReturnPip == 12): # Q
					self.reverse()
				elif (choice_card.ReturnPip == 13): # K
					self.oneMore()
				elif (choice_card.ReturnPip == 7): # 7
					self.suitChange()

				# 낸 카드가 공격 카드 일때
				self.IsAttackCard(choice_card)

			if (self.TurnList.List[0].getCard_Count == 0):
				Writer.Win(self.TurnList.List[0].getName,1)
				break
				## 플레이어가 카드를 모두 소진하여 게임에서 이길 경우

			elif self.TurnList.List[0].getCard_Count > 15 :
				Writer.Lose(self.TurnList.List[0].getName)
				self.TurnList.Remove(0)
				## 플레이어의 카드가 15장이 넘어가면 해당 게임에서 지게 된다.
		
			self.nextTurn()
			## 다음 턴의 플레이어를 찾아준다.

			if (self.TurnList.getCount==1):
				Writer.Win(self.TurnList.List[0].getName,2)
				break
				## 플레이어가 게임에서 혼자 살아남아 이기는 경우
			Writer.Show_Next_Trun()
			timer()


def timer():
	count = 0
	s_ts = datetime.datetime.now()
	while True:
		count += 1
		e_ts = datetime.datetime.now()
		diff_ts = e_ts - s_ts
		if diff_ts.total_seconds() >= 3:
			break
	for _ in range(1,200):
		print()


def main():
	print("< Welcome to One Card Game! >".center(63),"\n")
	if(Reader.show_information()):
		Writer.information()
	Round_count = 1
	while True:
		player_count = Reader.get_player_number("몇명의 플레이어와 게임을 하시겠습니까? (2~5) ",2,5)
		names = Reader.register(player_count)
		game = OneCard(player_count,names)
		game.play(Round_count)
		if not Reader.ox("더 플레이 하시겠습니까 ? (o/x) "):
			break
		Round_count+=1
	print("이용해주셔서 감사합니다")

main()
