from gomokuAgent import GomokuAgent
import misc as mis
import numpy as np
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	def terminalTest(self,board):
		if mis.winningTest(self.ID,board,self.X_IN_A_LINE) or mis.winningTest(-1*self.ID,board,self.X_IN_A_LINE):
			return True
		if not 0 in board:
			return True
	
	def utility(self,board):
		if mis.winningTest(self.ID,board,self.X_IN_A_LINE):
			return self.ID
		elif mis.winningTest(-1*self.ID,board,self.X_IN_A_LINE):
			return -1 * self.ID
		else:
			return 0.5
	def actions(self,board):
		legalMoves = []
		for r in range(self.BOARD_SIZE):
			for c in range(self.BOARD_SIZE):
				if mis.legalMove(board,(r,c)):
					legalMoves.append((r,c))
		return legalMoves

	def makeMove(self,board,move,player):
		newBoard = np.array(board)
		newBoard[move[0]][move[1]] = player
		return newBoard

	def maxFunct(self,board,modifier,alpha,beta):
		if self.terminalTest(board):
			return self.utility(board)
		legalMoves = self.actions(board)
		mxx = -1000
		for move in legalMoves:
			mxx = max(mxx,self.minFunct(self.makeMove(board,move,self.ID*modifier),modifier*-1,alpha,beta))
			if mxx >= alpha:
				return mxx
			alpha = max(mxx,alpha)
		return mxx

	def minFunct(self,board,modifier,alpha,beta):
		if self.terminalTest(board):
			return self.utility(board)
		legalMoves = self.actions(board)
		mnn = 1000
		for move in legalMoves:
			mnn = min(mnn,self.maxFunct(self.makeMove(board,move,self.ID*modifier),modifier*-1,alpha,beta))
			if mnn <= beta:
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
				mxxForThisAction = self.maxFunct(self.makeMove(board,action,self.ID),-1,-1000,1000)
				if mxxForThisAction > mxxSoFar:
					actionToReturn = action
					mxxSoFar = mxxForThisAction
			return actionToReturn
		if self.ID == -1:
			minSoFar = 1000
			actionToReturn = None
			for action in legalMoves:
				minForThisAction = self.minFunct(self.makeMove(board,action,self.ID),-1,-1000,1000)
				if minForThisAction < minSoFar:
					actionToReturn = action
					minSoFar = minForThisAction
			return actionToReturn

