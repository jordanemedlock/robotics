#!/usr/local/bin/python

import time
from baymax import *

class Board(object):
	def __init__(self, n):
		self.n = n
		self.baymax = Baymax(0, n-1, NORTH, (n/2,n/2), (n-1,0))

	def run(self):
		self.baymax.run()
		self.printBoard()

	def printBoard(self):
		for j in xrange(self.n):
			for i in xrange(self.n):
				if self.baymax.x == i and self.baymax.y == j:
					if self.baymax.direction is NORTH:
						print '^',
					elif self.baymax.direction is EAST:
						print '>',
					elif self.baymax.direction is SOUTH:
						print 'v',
					elif self.baymax.direction is WEST:
						print '<',
					else:
						print MSG
				elif self.baymax.hiro_x == i and self.baymax.hiro_y == j:
					print 'h',
				elif self.baymax.home_x == i and self.baymax.home_y == j:
					print 'H',
				else:
					print '_',
			print
		print 
		print
		print

if __name__ == '__main__':
	board = Board(10)
	while True:
		board.run()
		time.sleep(1)  

