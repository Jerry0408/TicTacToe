class TicTocToe():
	"""docstring for ClassName"""
	def __init__(self):
		self.board = {
			'%d' % (i): ' '  for i in range(1, 10)
		}
		self.rows_cols_edges = [
			['1', '2', '3'],
			['4', '5', '6'],
			['7', '8', '9'],
			['1', '4', '7'],
			['2', '5', '8'],
			['3', '6', '9'],
			['1', '5', '9'],
			['3', '5', '7']
		]
		
	def print_board(self):
		print(self.board['7'], '|', self.board['8'], '|', self.board['9'])
		print('-', '+', '-', '+', '-')
		print(self.board['4'], '|', self.board['5'], '|', self.board['6'])
		print('-', '+', '-', '+', '-')
		print(self.board['1'], '|', self.board['2'], '|', self.board['3'])

	def game(self):
		turn_set = ['X', 'O']
		count = 0

		while True:
			self.print_board()
			turn = turn_set[count % 2]
			print("It's" + turn +"'s turn.")
			print("Come on make your move.")

			move = input()

			if move not in self.board:
				print('Wrong Input!!!')
				continue

			if self.board[move] != ' ':
				print('Filled!!!')
				continue

			self.board[move] = turn
			count += 1

			if count >= 5:
				for a, b, c in self.rows_cols_edges:
					if self.board[a] == self.board[b] == self.board[c] != ' ':
						self.print_board()
						for _ in range(9):
							print(turn, ' wins!!!!!!!!!')
						return

			if count == 9:
				self.print_board()
				print('Tie!!!!!!!!!!')
				break


yes_ans = set(['y', 'Yes', 'yes', '1', 'yeah'])
while True:
	a = TicTocToe()
	a.game()
	print('Wanna replay???????????')
	ans = input()
	if ans not in yes_ans:
		break




