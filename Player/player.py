'''
Author: Abdelrahman Abdelhalim (988156)
All the code has been written and tested by Abdelrahman Abdelhalim (988156)
Unfortunately due to some health issues (Catching COVID and an ear infection) that I failed to report in time for this coursework, I did not manage to come up with a better solution. The program can play the gameon an 11 by 11 board, however it is not very optimal with a very simple evaluation function. The Program might also timeout for longer games.

The Algorithm starts off with a list of moves that are close to a move that has been made by either players on the board
It then proceeds through the minimax algorithm, with a depth cutoff of 2 which is very bad considering how little time I had to construct a solution
The evaluation funtion discourages when the opponent has 3 stones in a row and encourages when the agent has 3 stones in a row
This results in semeingly a very defensive behavior by the AI

With more time we could try improving the algorithm by doing the following:
1. Developnig a better evaluation function
2. Developing a transposition lookup table
3. Looking into initial node selection in a better way
4. Optimizing the low level computations that don't impact decision making
'''
from gomokuAgent import GomokuAgent
import misc as mis
import numpy as np
import random as rand
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	'''
	Terminal Test for the minimax Algorithm
	Parameters:
	1.Board: The current position to be evaluated
	'''
	def terminalTest(self,board):
		if mis.winningTest(self.ID,board,self.X_IN_A_LINE) or mis.winningTest(-1*self.ID,board,self.X_IN_A_LINE):
			return True
		if not 0 in board:
			return True

	'''
	Finding all the possible legal moves in the position
	Parameters:
	1.Board: The current board for which to find the legal moves
	'''
	def actions(self,board):
			legalMoves = []
			for r in range(0,self.BOARD_SIZE+1):
				for c in range(0,self.BOARD_SIZE+1):
					if mis.legalMove(board,(r,c)):
						legalMoves.append((r,c))
			return legalMoves
	'''
	Utility function for the minimax algorithm
	Parameters:
	1.Board: The board for which to determine the utility value
	'''
	def utility(self,board):
		if mis.winningTest(self.ID,board,5):
			return self.ID*self.X_IN_A_LINE
		if mis.winningTest((-1*self.ID),board,5):	
			return (self.ID*-1)*self.X_IN_A_LINE
		if not 0 in board:
			return 0.5*self.X_IN_A_LINE

	'''
	A misc function that makes a copy of the board with the intended move
	Parameters:
	1.board: The board for which the move is to be made
	2.move: The move to be made in the position
	3.player: The player that is making the move
	'''
	def makeMove(self,board,move,player):
		newBoard = np.copy(board)
		newBoard[move] = player
		return newBoard
	'''
	Maxmimizing Function for the minimax algorithm
	Parameters:
	1.board:Current node for which to calculate max
	2.modifier: This modifier determines if it is the agent's move or the opponent move, and it is alternated every recursion by multiplying it by -1
	3.alpha,beta: Alpha and beta parameters for pruning
	4.depth: Current depth in the search tree
	'''
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
	'''	
	Minimizing Function for the minimax algorithm
	Parameters:
	1.board:Current node for which to calculate max
	2.modifier: This modifier determines if it is the agent's move or the opponent move, and it is alternated every recursion by multiplying it by -1
	3.alpha,beta: Alpha and beta parameters for pruning
	4.depth: Current depth in the search tree
	'''
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

	'''
	Function to test if three stones are alligned in the position for eithe player
	This is part of the strategy implemented for evaluation
	Parameters:
	1.board: The board for which to determine if three stones are alligned
	'''		
	def testForThreeStones(self,board):
		if self.terminalTest(board):
			return self.utility(board)
		if mis.winningTest(self.ID,board,3):
			return True
		if mis.winningTest(-1*self.ID,board,3):
			return True
		return False
	'''
	Funciton that determines if the node is a good node to cut the search at and start the evaluation function
	Parameters:
	1.board: The state to evaluate
	2.depth: The current depth of the node
	'''
	def cutOffTest(self,board,depth):
		if depth == 2:
			return True
		if self.testForThreeStones(board):
			return True
		return False

	'''
	Evalutaion function
	'''
	def evaluate(self,board):
		if mis.winningTest(self.ID,board,2):
			return self.ID*2
		if mis.winningTest(-1*self.ID,board,2):
			return -1*self.ID*2
		else:
			return 1.5*self.ID
	'''
	Tests if the legal moves has any moves that have been previously made by either player
	if that is the case, the move is considered in the evaluation
	if not the node is discarded
	Parameters:
	1.board: the current position
	2.move: the move to test the surroundings for
	'''
	def testSurroundings(self,board,move):
#		[-1,-1][0,-1][-1,1][0,-1][0,1][1,-1][1,0][1,1]
		for r in range(-1,2):
			for c in range(-1,2):
				if move[0]+r >= 0 and move[0]+r < self.BOARD_SIZE and move[1]+c >= 0 and move[1]+c < self.BOARD_SIZE:
					squareToCheck = (move[0]+r,move[1]+c)
					if board[squareToCheck] == 1 or board[squareToCheck] == -1:
						return True
		return False
	'''
	Function that selects the moves that are surrounded by previous moves from either players for evaluation
	Parameters:
	1.board: Current position
	2.legalMoves: All the legal moves in the position
	'''
	def selectLegalMoves(self,board,legalMoves):
		selectedLegalMoves = []
		for move in legalMoves:
			if self.testSurroundings(board,move):
				selectedLegalMoves.append(move)
		return selectedLegalMoves

	
    '''
    Entry point to the program
    Parameters:
    1.board: The current position
	'''
	def move(self,board):
		legalMoves = self.selectLegalMoves(board,self.actions(board))
		if len(legalMoves) == 0:
				legalMoves.append((5,5))
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

