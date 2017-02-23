
# One Card - View


class Reader :

	@staticmethod
	def show_information():
		response = input(" 게임 설명을 보시겠습니까? (y/n) :").lower()
		while not (response == 'y' or response == 'n'):
			response = input(" 게임 설명을 보시겠습니까? (y/n) :").lower()
		return response == 'y'

	@staticmethod
	def register(count):
		names = []
		for i in range(1,count+1):
			name = input("플레이어 "+str(i)+" 이름 : ")
			names.append(name)
		return names

	@staticmethod
	def get_player_number(message,low,high):
		response = input(message)
		while not (response.isdigit() and low <= int(response) <= high):
			response = input(message)
		return int(response)
	
	@staticmethod
	def ox(message):
		response = input(message).lower()
		while not (response =='o' or response =='x'):
			response = input(message).lower()
		return response == 'o'

	@staticmethod
	def get_choice_card(message,low,high):
		response = input(message)
		resp = response.partition("-")
		while not ((resp[1]=="-" and resp[2].isdigit() and int(resp[2]) == 1 and len(resp[2])==1) or \
				(response.isdigit() and low <= int(response) <= high)):
			response = input(message)
			resp = response.partition("-")
		return int(response)

	@staticmethod
	def get_choice_suit():
		response = input("1) ♧ 2) ◇ 3) ♡ 4) ♤\n바꿀 모양을 선택하세요 : ")
		while not (1 <= int(response) <= 4):
			response = input("1) ♧ 2) ◇ 3) ♡ 4) ♤\n바꿀 모양을 선택하세요 : ")
		return int(response)


class Writer :

	def show_card_pip(card):
		if card.ReturnPip == 1:
			return "Ace"
		elif card.ReturnPip == 11:
			return "J"
		elif card.ReturnPip == 12:
			return "Q"
		elif card.ReturnPip == 13:
			return "K"
		elif card.ReturnPip == 14:
			return "Color"
		elif card.ReturnPip == 15:
			return "Black"
		else :
			return str(card.ReturnPip)

	def show_card_suit(card):
		if card.ReturnSuit == 1:
			return "♧"
		elif card.ReturnSuit == 2:
			return "◇"
		elif card.ReturnSuit == 3:
			return "♡"
		elif card.ReturnSuit == 4:
			return "♤"
		elif card.ReturnSuit == 5:
			return "Joker"

	@staticmethod
	def show_player_name(player):
		print("현재 플레이어 : ",player.getName)

	@staticmethod
	def show_next_player_name(player):
		print("다음 플레이어 : ",player.getName)

	@staticmethod
	def start_game(Round_count):
		print("=========== New Game ===========")
		print("=========== "+str(Round_count)+"  Round ===========")

	@staticmethod
	def show_bottom_card(card):
		i = len(card) - 1
		print("< Bottom Card >")
		print(" -----")
		print("|     |")
		print("|"+Writer.show_card_suit(card[i]).center(5)+"|")
		print("|"+Writer.show_card_pip(card[i]).center(5)+"|")
		print("|     |")
		print(" -----")
		print("================================================")

	@staticmethod
	def show_my_card(card):
		print("< Player Card >")
		for i in range(0,len(card)):
			if i < 10 :
				print(str(i+1).center(7),end="")
				#print("   "+str(i+1)+"   ",end="")
			else :
				print(str(i+1).center(7),end="")
		print()
		for i in range(0,len(card)):
			print(" -----",""*int(i/2),end="")
		print()
		for i in range(0,len(card)):
			print("|     |",end="")
		print()
		for i in range(0,len(card)):
			print("|"+Writer.show_card_suit(card[i]).center(5)+"|",end="")
		print()
		for i in range(0,len(card)):
			print("|"+Writer.show_card_pip(card[i]).center(5)+"|",end="")
		print()
		for i in range(0,len(card)):
			print("|     |",end="")
		print()
		for i in range(0,len(card)):
			print(" -----",""*int(i/2),end="")
		print("\n================================================")

	@staticmethod
	def show_change_suit(before,after):
		print("  < Change Suit >")
		print(" [",before,"] -> [",after,"]")
		print("==================")

	@staticmethod
	def show_attackPoint(point):
		print(" < Total Attack Point >")
		print("========  ",str(point),"  ========")

	@staticmethod
	def inform_whatcard(name,count):
		what = ["Jump","Queen","King"]
		Str = what[count-1]
		print("================================================")
		print(name,"플레이어 님께서 ",Str," 카드 발동")
		print("================================================")

	@staticmethod
	def Win(name,count):
		if count == 1:
			print("================================================")
			print(name,"플레이어 님께서 게임 승리!!")
			print("================================================")
		elif count == 2:
			print("================================================")
			print("혼자만이 게임에서 살아남으셨습니다.!!")
			print(name,"플레이어 님께서 게임 승리!!")
			print("================================================")

	@staticmethod
	def Lose(name):
		print("================================================")
		print(name,"플레이어 님께서 게임에서 패배..")
		print("================================================")

	@staticmethod
	def inform(card):
		print("방어 하지 못하여 추가 카드를 받으셨습니다.")
		Writer.show_my_card(card)

	@staticmethod
	def Show_Next_Trun():
		print("3초 후 턴이 종료됩니다.")

	@staticmethod
	def Wrong_choice():
		print("해당 카드를 선택 할 수 없습니다. 규칙에 맞는 카드를 선택해주세요.")

	@staticmethod
	def information():
		print(" ==============================================================")
		print("|","< 게임 설명 >".center(56),"|")
		print("|","본 게임은 원카드 게임으로써 Bottom 에 있는 Card와".center(44),"|")
		print("|","무늬/기호가 같은 카드를 내면서 자신기 가진 모든 카드".center(38),"|")
		print("|","를 모두 소진하면 이기는 게임이다. 규칙은 다음과 같다.".center(38),"|")
		print("|","카드의 기호가 7인 경우 다음에 낼 카드무늬를 바꿀수 있다.".center(37),"|")
		print("|","카드의 기호가 J인 경우 다음 플레이어를 건너뛰고 진행한다.".center(36),"|")
		print("|","카드의 기호가 Q인 경우 플레이의 턴 방향을 반대로 바꾼다.".center(37),"|")
		print("|","카드의 기호가 K인 경우 자신이 한번 더 플레이 한다.".center(40),"|")
		print("|","카드의 기호가 A / 2 / Joker 인 경우 공격 카드로서".center(45),"|")
		print("|","다음 플레이어가 방어를 못하면 해당 카드개수 만큼 가져간다.".center(35),"|")
		print("|","A -> 4개 ( A / Joker 로 방어 가능 )".center(54),"|")
		print("|","2 -> 2개 ( A / 2 / Joker 로 방어 가능 )".center(54),"|")
		print("|","ColorJoker -> 7 개 ( Joker 로 방어 가능 )".center(54),"|")
		print("|","BlackJoker -> 5 개 ( Joker 로 방어 가능 )".center(54),"|")
		print(" ==============================================================")

