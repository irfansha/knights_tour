#append the value in the desired list or creates new one in the dictonary
	

#Generates a list of legal moves for the knight

knight_moves = [[]]

def generate_legal_moves(x,y,N):
	possible_pos = []
	move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
	for move in move_offsets:
		new_x = x + move[0]
		new_y = y + move[1]

		if (new_x >= N):
			continue
		elif (new_x < 0):
			continue
		elif (new_y >= N):
			continue
		elif (new_y < 0):
			continue
		else:
			possible_pos.append(N*new_x + new_y+1)
			possible_pos.sort()
	return possible_pos

def gen_knight_moves(N):
	for i in range(N):
		for j in range(N):
			knight_moves.append(generate_legal_moves(i,j,N))
	return knight_moves
