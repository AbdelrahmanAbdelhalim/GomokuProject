from gomokuAgent import GomokuAgent
import misc as mis
class Player(GomokuAgent):
	def __init__ (self,ID,BOARD_SIZE,X_IN_A_LINE):
		GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

	def move(self,board):
		print(123)

	def terminalTest(self,board):
		if mis.winningTest(self.ID,board,X_ON_A_LINE) or mis.winningTest(-1*self.ID,board,X_IN_A_LINE):
			return True
		if not 0 in board:
			return True
	
	def utility(self,board):
		if terminaTest(self,board):
			if mis.winningTest(self.ID,board,X_ON_A_LINE):
				return self.ID
			elif mis.winningTest(-1*self.ID,board,X_ON_A_LINE):
				return -1 * self.ID
			else:
				return 0.5
	def actions(self,board):
		legalMoves = []
		for r in range(self.BOARD_SIZE):
			for c in range(self.BOARD_SIZE):
				if legalMove(board,[r,c]):
					legalMoves.append([r,c])
		return legalMoves

