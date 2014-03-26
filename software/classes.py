from random import randrange

class Square(object):
	def __init__(self, name):
		self.name = name
		
class Property(Square):
	def __init__(self, id, name, price, rent, oneHouse, twoHouse, threeHouse, fourHouse, hotel, costHouse, group, isRailroad, isUtility):
		self.name = name
		self.id = id
		self.price = price
		self.rent = rent
		self.oneHouse = oneHouse
		self.twoHouse = twoHouse
		self.threeHouse = threeHouse
		self.hotel = hotel
		self.costHouse = costHouse
		self.group = group
		self.isMorgaged = 0
		self.isOwned = 0
		self.isRailroad = isRailroad
		self.owner = -1
		self.inBankrupt = 0
		
	def morgage(self):
		return price / 2
		
	def monopolyPrice(self):
		return rent * 2
		
	def morgaged():
		self.isMorgaged = 1
	
	def demorgaged():
		self.isMorgaged = 0
		
	def bought(player):
		self.isOwned = 1
		self.owner = player
	
	def sold():
		self.isOwned = 0
		self.owner = -1
		
class Event(Square):
	def __init__(self, name, income, move, payTax, specialTax):
		self.name = name
		self.income = income
		self.move = move
		self.payTax = payTax
		self.specialTax = specialTax
		
	def runEvent(player):
		player.cash = player.cash + self.income
		player.position = player.position + self.move
		player.cash = player.cash - self.payTax
		player.cash = player.cash - self.specialTax

class Board(object):
	def __init__(self):
		#def __init__(self, id, name, price, rent, oneHouse, twoHouse, threeHouse, fourHouse, hotel, costHouse, group, isRailroad):
		#def __init__(self, name, income, move, payTax, specialTax):
		self.squares = [Event(	'Go', 200, 0, 0, 0),
						Property(0, 'Mediterranean Ave.', 60, 2, 10, 30, 90,  60,  250, 0, 0, 0, 0),
						Event(	'Income tax', 0, 0, 0, 0),
						Property(1, 'Baltic Ave.', 		  60, 4, 20, 60, 180, 320, 450, 0, 0, 0, 0)]
		
class Player(object):
	board = Board()
	playerList = []

	def __init__(self, id):
		self.id = id
		self.properties = []
		self.position = 0
		self.cash = 0
		self.inJail = 0
		self.turnsInJail = 3
		playerList.push(self, id)

	def correctPosition():
		if self.position >= 40 :
			self.position = self.position - 40
		
	def lockUp():
		self.inJail = 1
		
	def setFree():
		self.inJail = 0
		self.turnsInJail = 3
		
	def play():
		if not inBankrupt:
			dice = randrange(12) + randrange(12) + 2
			if inJail:
				if turnsInJail == 3:
					if randrange(2):
						this.cash = this.cash - 50
						#move
					else:
						if turnsInJail > 0:
							self.turnsInJail = self.turnsInJail - 1
							if turnsInJail == 0:
								setFree()
								this.cash = this.cash - 50
								move(dice)
							else:
								#finish turn
								pass
			else: 
				move(dice)
			
	def move(dice):		
		self.position = self.position + dice
		#if passed Go
		if dice >= 40:
			self.cash = self.cash + 200
			correctPosition()
		square = board.squares[self.position]
		if type(square) is Property:
			#Property stuff
			if square.isOwned:
				self.cash = self.cash - square.rent
				if not isMorgaged:
					self.cash = self.cash - square.rent
					owner = playerList[square.owner]
					owner.cash = owner.cash + square.rent
			else:
				#buy
				pass
		elif type(square) is Event: 
			#Event stuff
			pass
		
class Game(object):
	def __init__(self):
		pass
	
	def start():
		#Create 4 players
		p1 = Player(1)
		p2 = Player(2)
		p3 = Player(3)
		p4 = Player(4)