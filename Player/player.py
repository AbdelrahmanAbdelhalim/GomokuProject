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

	def utility(self,board):
		if mis.winningTest(self.ID,board,5):
			return self.ID*self.X_IN_A_LINE
		if mis.winningTest((-1*self.ID),board,5):	
			return (self.ID*-1)*self.X_IN_A_LINE
		if not 0 in board:
			return 0.5*self.X_IN_A_LINE

	def testForThreeStones(self,board):
		if self.terminalTest(board):
			return self.utility(board)
		if mis.winningTest(self.ID,board,3):
			return True
		if mis.winningTest(-1*self.ID,board,3):
			return True
		return False

	def cutOffTest(self,board,depth):
		if depth == 2:
			return True
		if self.testForThreeStones(board):
			return True
		return False

	def actions(self,board):
		legalMoves = []
		for r in range(0,self.BOARD_SIZE+1):
			for c in range(0,self.BOARD_SIZE+1):
				if mis.legalMove(board,(r,c)):
					legalMoves.append((r,c))
		return legalMoves

	def evaluate(self,board):
		if mis.winningTest(self.ID,board,3):
			return self.ID*3
		if mis.winningTest(-1*self.ID,board,3):
			return -1*self.ID*3
		else:
			return 2*self.ID

	def makeMove(self,board,move,player):
		newBoard = np.copy(board)
		newBoard[move] = player
		return newBoard
	def testSurroundings(self,board,move):
#		[-1,-1][0,-1][-1,1][0,-1][0,1][1,-1][1,0][1,1]
		for r in range(-1,2):
			for c in range(-1,2):
				if move[0]+r >= 0 and move[0]+r < self.BOARD_SIZE and move[1]+c >= 0 and move[1]+c < self.BOARD_SIZE:
					squareToCheck = (move[0]+r,move[1]+c)
					if board[squareToCheck] == 1 or board[squareToCheck] == -1:
						return True
		return False
	def selectLegalMoves(self,board,legalMoves):
		selectedLegalMoves = []
		for move in legalMoves:
			if self.testSurroundings(board,move):
				selectedLegalMoves.append(move)
		return selectedLegalMoves

	def maxFunct(self,board,modifier,alpha,beta,depth):
		if self.cutOffTest(board,depth):
			return self.evaluate(board)
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
		if self.cutOffTest(board,depth):
			return self.evaluate(board)
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
		legalMoves = self.selectLegalMoves(board,self.actions(board))
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

