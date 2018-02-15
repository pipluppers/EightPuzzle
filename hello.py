def main():
	welcome = input('Welcome to Alex Nguyen\'s 8-puzzle solver.\nType "1" to use a default puzzle, or "2" to enter your own puzzle.\n')
	
	if (welcome == 1):
		#default puzzle
		default = [[1,2,3],[4,5,0],[7,8,6]]
		print_puzzle(default)
		print("Default puzzle\n")

	elif (welcome == 2):
		print('Enter your puzzle, use a zero to represent the blank\n')
		#topleft = input('Enter the first row, use space or tabs between numbers: ')
		#topmid = input('')
		#topright = input('')
		toprow = raw_input('Enter the first row (only three numbers), use space or tabs between numbers: ').split()
		for x in range(0,3):
			toprow[x] = int(toprow[x])
			#print(toprow[x])
		midrow = raw_input('Enter the second row (only three numbers), use space or tabs between numbers: ').split()
		for x in range(0,3):
			midrow[x] = int(midrow[x])
			#print(midrow[x])
		botrow = raw_input('Enter the third row (only three numbers), use space or tabs between numbers: ').split()
		for x in range(0,3):
			botrow[x] = int(botrow[x])
			#print(botrow[x])
		puzzledesign = [toprow, midrow, botrow]

		print_puzzle(puzzledesign)
		
		alg = input('\nEnter your choice of algorithm:\n1. Uniform Cost Search\n2. A* with ' +
			'the Misplaced Tile heuristic\n3. A* with the Manhatten distance heuristic.\n')
		if (alg == 1):
			print("Beginning Uniform Cost Search")
			#UCS()
		elif (alg == 2):
			print('Beginning A* with Misplaced Tile heuristic')
			#MTH();
		elif (alg == 3):
			print('Beginning A* with the Manhatten distance heuristic')
			#ManDH()
		else:
			print('Not a valid number')



def print_puzzle(puzzleLayout):
	for x in range(0, 3):
			print(puzzleLayout[x])
	#print('\n')




if __name__ == "__main__":
	main()















