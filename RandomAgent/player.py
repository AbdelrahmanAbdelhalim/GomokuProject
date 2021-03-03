from gomokuAgent import GomokuAgent
import misc as mis
import numpy as np
import random as rand
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	def actions(self,board):
		legalMoves = []
		for r in range(self.BOARD_SIZE):
			for c in range(self.BOARD_SIZE):
				if mis.legalMove(board,(r,c)):
					legalMoves.append((r,c))
		return legalMoves

	def move(self,board):
		legalMoves = self.actions(board)
		mv = rand.randint(0,len(legalMoves)-1)
		return legalMoves[mv]
