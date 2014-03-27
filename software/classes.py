from random import randrange

class Square(object):
	def __init__(self, name):
		self.name = name
		
class Property(Square):
	totalProperties = 0
	
	def __init__(self, name, price, rent, oneHouse, twoHouse, threeHouse, fourHouse, hotel, costHouse, group):
		self.name = name
		self.price = price
		self.rent = rent
		self.nroHouses = 0
		self.hasHotel = 0
		self.oneHouse = oneHouse
		self.twoHouse = twoHouse
		self.threeHouse = threeHouse
		self.hotel = hotel
		self.costHouse = costHouse
		self.group = group
		self.isMorgaged = 0
		self.isOwned = 0
		self.owner = -1
		self.inBankrupt = 0
		Property.totalProperties = Property.totalProperties + 1
		self.id = Property.totalProperties
		
	def morgage(self):
		return self.price / 2
		
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
	'''
	chance = [Event('Advance to Go', 200, '0', 0),
			  Event('Advance to Illinois Ave.'), '24', 0]
	'''
	def __init__(self, name, income, move, payTax, specialTax=0):
		self.name = name
		self.income = income
		self.move = move
		self.payTax = payTax
		self.specialTax = specialTax
'''		
	def runEvent(player):
		if specialTax == 1:
			if name = 'Community Chest':
				pass
			cash = cash * 0.9
		else:
			player.cash = player.cash + income
			player.position = player.position + move
			player.correctPosition()
			player.cash = player.cash - payTax
			player.cash = player.cash - specialTax
'''
class Board(object):
	def __init__(self):
		#def __init__(self, id, name, price, rent, oneHouse, twoHouse, threeHouse, fourHouse, hotel, costHouse, group):
		#def __init__(self, name, income, move, payTax, specialTax):
		self.squares = [Event(	'Go', 200, 0, 0),
						Property('Mediterranean Ave.',    60,  2, 10, 30,  90,  60, 250, 50,0),
						Event('Community Chest', 0, 0, 0, 1),
						Property('Baltic Ave.', 	      60,  4, 20, 60, 180, 320, 450, 50,0),
						Event(	'Income tax', 0, 0, 0, 1),
						Property('Reading Railroad',     200, 50,  0,  0,  0,   0,   0, 50,8),
						Property('Oriental Ave.', 	     100,  6, 30, 90, 270, 400, 550, 50,1),
						Event(	'Chance', 0, 0, 0, 1),
						Property('Vermont Ave.', 	     100,  6, 30, 90, 270, 400, 550, 50,1),
						Property('Connecticut Ave.',     120,  8, 40,100, 300, 450, 600, 50,1),
						Event(	'Jail', 0, 0, 0, 1),
						Property('St. Charles Place',    140, 10, 50,150, 450, 625, 750,100,2),
						Property('Electric Company',     150, 10,  0,  0,  0,   0,   0,  0,9),
						Property('States Ave.', 	     140, 10, 50,150, 450, 625, 750,100,2),
						Property('Virginia Ave.',	     160, 12, 60,180, 500, 700, 900,100,2),
						Property('Pennsylvania Railroad',200, 12,  0,  0,  0,   0,   0,  0,8),
						Property('St. James Place',		 180, 14, 70,200, 550, 750, 950,100,3),
						Event('Community Chest', 0, 0, 0, 1),
						Property('Tennessee Ave.',		 180, 14, 70,200, 550, 750, 950,100,3),
						Property('New York Ave.',		 200, 16, 80,220, 600, 800,1000,100,3),
						Event(	'Free Parking', 0, 0, 0, 1),
						Property('Kentucky Ave.',		 220, 18, 90,250, 700, 875,1050,150,4),
						Event(	'Chance', 0, 0, 0, 1),
						Property('Indiana Ave.',		 220, 18, 90,250, 700, 875,1050,150,4),
						Property('Illinois Ave.',		 240, 20,100,300, 750, 925,1100,150,4),
						Property('B&O Railroad',		 200, 0,   0,  0,  0,   0,   0,  0,8),
						Property('Atlantic Ave.',		 260, 22,110,330, 800, 975,1150,150,5),
						Property('Ventnor Ave.',		 260, 22,110,330, 800, 975,1150,150,5),
						Property('Water Works',		 	 150,  0,  0,  0,  0,   0,   0,  0,9),
						Property('Marvin Gardens',		 280, 24,120,360, 850,1025,1200,150,5),
						Event(	'Go to Jail', 0, 0, 0, 1),
						Property('Pacific Ave.',		 300, 26,130,390, 900,1100,1275,200,6),
						Property('North Carolina Ave.',	 300, 26,130,390, 900,1100,1275,200,6),
						Event('Community Chest', 0, 0, 0, 1),
						Property('Pennsylvania Ave.',	 320, 28,150,450,1000,1200,1400,200,6),
						Property('Short Line Railroad',	 200, 0,   0,  0,   0,   0,   0,  0,8),
						Event(	'Chance', 0, 0, 0, 1),
						Property('Park Place',	 		 350, 35,175,500,1100,1300,1500,200,7),
						Event(	'Luxury Tax', 0, 0, 0, 1),
						Property('Boardwalk',	 		 400, 50,200,600,1400,1700,2000,200,7)
						]
		
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
		if position >= 100 :
			position = 0
		elif position >= 40 :
			position = position - 40
		
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