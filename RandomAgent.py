from gomokuAgent import GomokuAgent
import misc as mis
import numpy as np
import random as rand
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	#return a tuple with the move
	def move(self,board):
		actions = actions(self,board)
		randomAction = rand.randint(0,len(actions))
		return actions[randomAction]

	def actions(self,board):
		legalMoves = []
		for r in range(self.BOARD_SIZE):
			for c in range(self.BOARD_SIZE):
				if mis.legalMove(board,[r,c]):
					legalMoves.append([r,c])
		return legalMoves