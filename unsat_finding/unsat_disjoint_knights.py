# Step 1 : Check if dictionary/lists are good for these operations.

# Step 2 : Print all the unvisited but neighbour vertices.

# Step 3 : Next connect them if they are neighbour vertices.

# Step 4 : Check the unsatisfiabity i.e. if they are disjoint from the graph.

# Step 5 : After getting this work, now add merging of different parts.

# Step 6 : Now check the correctness of the approach

# Step 7 : If everything works out find now check if there is any speed up, this should be the last one.


import sys

N = int(sys.argv[1])

visited = [0]*(N*N+1) # maintains if the vertex is visited

move_count = 0 # keeps track of number of moves made

total_moves = N*N

knight_moves = [[]]


#Generates a list of legal moves for the knight

def generate_legal_moves(x,y):
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

for i in range(N):
	for j in range(N):
		knight_moves.append(generate_legal_moves(i,j))


def recur(cur_move,move_count,tour_count):
	#print (visited)
	if move_count < total_moves:
		for move in knight_moves[cur_move]:
			if visited[move] == 0:
				#print (move)
				move_count = move_count + 1
				visited[move] = 1
				tour_count = recur(move,move_count,tour_count)
				move_count = move_count - 1
				visited[move] = 0

	elif move_count == total_moves:
		tour_count = tour_count + 1
		#print ("found one",tour_count)
	return tour_count

for i in range(1,total_moves):
	visited[i] = 1
	tour_count = recur(i,1,0)
	visited[i] = 0
	print (tour_count)

