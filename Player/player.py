from gomokuAgent import GomokuAgent
import misc as mis
import numpy as np
import random as rand
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	def terminalTest(self,board):
		if mis.winningTest(self.ID,board,self.X_IN_A_LINE) or mis.winningTest(-1*self.ID,board,self.X_IN_A_LINE):
			return True
		if not 0 in board:
			return True
	
	def utility(self,board,depth):
		if mis.winningTest(self.ID,board,self.X_IN_A_LINE):
			return self.ID 
		if mis.winningTest((-1*self.ID),board,self.X_IN_A_LINE):	
			return (self.ID*-1)
		if not 0 in board:
			return 0

	def actions(self,board):
		legalMoves = []
		for r in range(0,self.BOARD_SIZE+1):
			for c in range(0,self.BOARD_SIZE+1):
				if mis.legalMove(board,(r,c)):
					legalMoves.append((r,c))
		return legalMoves

	def makeMove(self,board,move,player):
		newBoard = np.copy(board)
		newBoard[move] = player
		return newBoard

	def maxFunct(self,board,modifier,alpha,beta,depth):
		if self.terminalTest(board):
			return self.utility(board,depth)
		legalMoves = self.actions(board)
		mxx = -1000
		for move in legalMoves:
			newBoard = self.makeMove(board,move,self.ID*modifier)
			mxx = max(mxx,self.minFunct(newBoard,modifier*-1,alpha,beta,depth+1))
			if mxx >= beta:
				return mxx
			alpha = max(mxx,alpha)
		return mxx

	def minFunct(self,board,modifier,alpha,beta,depth):
		if self.terminalTest(board):
			return self.utility(board,depth)
		legalMoves = self.actions(board)
		mnn = 1000
		for move in legalMoves:
			newBoard = self.makeMove(board,move,self.ID*modifier)
			mnn = min(mnn,self.maxFunct(newBoard,modifier*-1,alpha,beta,depth+1))
			if mnn <= alpha:
				return mnn
			beta = min(mnn,beta)
		return mnn

    #return a tuple with the move
	def move(self,board):
		legalMoves = self.actions(board)
		if self.ID == 1:
			mxxSoFar = -1000
			actionToReturn = None
			for action in legalMoves:
				newBoard = self.makeMove(board,action,self.ID)
				mxxForThisAction = self.minFunct(newBoard,-1,-1000,1000,1)
				if mxxForThisAction > mxxSoFar:
					actionToReturn = action
					mxxSoFar = mxxForThisAction
			return actionToReturn
		if self.ID == -1:
			minSoFar = 1000
			actionToReturn = None
			for action in legalMoves:
				newBoard = self.makeMove(board,action,self.ID)
				minForThisAction = self.maxFunct(newBoard,-1,-1000,1000,1)
				if minForThisAction < minSoFar:
					actionToReturn = action
					minSoFar = minForThisAction
			return actionToReturn

