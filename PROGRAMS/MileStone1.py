from __future__ import print_function
import random
from IPython.display import clear_output
def display(board):
	clear_output()
	print("-------------") 
	print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')       
	print('-------------')       
	print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')        
	print('-------------')      
	print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
	print('-------------')
def player_input():
	marker=''
	while not (marker == 'X' or marker == 'O'):
		x=raw_input("What do you want? X or O").upper()
		if x=='X':
			return ('X','O')
		elif x=='O':
			return ('O','X')
		else:
			print("Enter Correct Data")
def win_check(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top    
	(board[4] == mark and board[5] == mark and board[6] == mark) or # across t he middle    
	(board[1] == mark and board[2] == mark and board[3] == mark) or # across t he bottom    
	(board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle    
	(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle    
	(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side    
	(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal    
	(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
def choose_first():    
	if random.randint(0, 1) == 0:     
	   return 'Player 2'    
	else:        
		return 'Player 1'
def full_board(board):    
 	if " " in board[1:]:        
 		return False    
 	else:        
 		return True
print("WELCOME TO THE GAME")
board=['']*10
player1,player2=player_input()
turn=choose_first()
print(turn+"Will go first")
game='True'
while game:
	if turn=='Player 1':
		display(board)
		position=int(raw_input("Enter position 1 (1-9) : "))
		board[position]=player1
		if win_check(board,player1):
			display(board)
			print("CONGRATULATIONS! YOU WON")
		else:
			if full_board(board):
				display(board)
				print("Game Draw")
				game='False'
			else:
				turn="Player 2"
	elif turn=='Player2':
		display(board)
		position=int(raw_input("Enter position 2 (1-9) : "))
		board[position]=player2
		if win_check(board,player2):
			display(board)
			print("CONGRATULATIONS! YOU WON")
		else:
			if full_board(board):
				display(board)
				print("Game Draw")
				game='False'
			else:
				turn="Player 1"


