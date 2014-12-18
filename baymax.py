import utilities

NORTH = 'NORTH'
EAST  = 'EAST'
SOUTH = 'SOUTH'
WEST  = 'WEST'

MSG = "Everybody knows SHIT, FUCK!"

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Baymax(object):
	def __init__ (self, x, y, direction, hiro, home):
		self.x = x
		self.y = y

		self.direction = direction;

		self.hiro_x, self.hiro_y = hiro
		self.home_x, self.home_y = home

		self.picked_up = False
		self._turn_up = False
		self.going_home = False

	def run(self):
		self._turn_up = False
		self.think()

	def think(self):
		if self.direction == NORTH and self.y != self.hiro_y and self.y != self.home_y:
				print 'd'
			 	self.walk()
		if self.direction == EAST and self.x != self.hiro_x and self.x != self.home_x:
				print 'b'
				self.walk()
		if self.y == self.hiro_y and self.x != self.hiro_x:
				print 'c'
				self.turnRight()	
		
		if self.x == self.hiro_x and self.y == self.hiro_y and not self.picked_up:
				print 'a'
				self.pickupHiro() 
		if self.picked_up:
			self.turnLeft()

		
		if self.y == self.home_y:
			self.turnRight()
 
		



	@utilities.mkmove
	def walk(self):
		if self.direction is NORTH:
			self.y -= 1
		elif self.direction is EAST:
			self.x += 1
		elif self.direction is SOUTH:
			self.y += 1
		elif self.direction is WEST:
			self.x -= 1
		else:
			print MSG

		if self.picked_up:
			self.hiro_x, self.hiro_y = self.x, self.y


	@utilities.mkmove
	def turnRight(self):
		if self.direction in DIRECTIONS:
			for i, direction in enumerate(DIRECTIONS):
				if self.direction == direction:
					self.direction = DIRECTIONS[(i + 1)%4]
					return None
		else:
			print MSG

	@utilities.mkmove
	def turnLeft(self):
		if self.direction in DIRECTIONS:
			for i, direction in enumerate(DIRECTIONS):
				if self.direction == direction:
					self.direction = DIRECTIONS[(i - 1)%4]
					return None
		else:
			print MSG

	@utilities.mkmove
	def pickupHiro(self):
		if (self.x - self.hiro_x)**2 == 0 and (self.y - self.hiro_y)**2 == 0:
			self.picked_up = True
			self.hiro_x, self.hiro_y = self.x, self.y
		else:
			print "Hiro is not close enough"

	@utilities.mkmove
	def dropHiro(self):
		self.picked_up = False
		if self.direction is NORTH:
			self.hiro_y -= 1
		elif self.direction is EAST:
			self.hiro_x += 1
		elif self.direction is SOUTH:
			self.hiro_y += 1
		elif self.direction is WEST:
			self.hiro_x -= 1
		else:
			print MSG

