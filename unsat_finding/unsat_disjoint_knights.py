# Step 1 : Check if dictionary/lists are good for these operations.

# Step 2 : Print all the unvisited but neighbour vertices.

# Step 3 : Next connect them if they are neighbour vertices.

# Step 4 : Check the unsatisfiabity i.e. if they are disjoint from the graph.

# Step 5 : After getting this work, now add merging of different parts.

# Step 6 : Now check the correctness of the approach

# Step 7 : If everything works out find now check if there is any speed up, this should be the last one.


import sys
import knight_moves
N = int(sys.argv[1])

visited = [0]*(N*N+1) # maintains if the vertex is visited

islands = [-1]*(N*N+1)

move_count = 0 # keeps track of number of moves made

total_moves = N*N

k_li = knight_moves.gen_knight_moves(N)


def place(visited,cur_move):
	visited[cur_move] = 1

def remove(visited,cur_move):
	visited[cur_move] = 0

def recur(cur_move,move_count,tour_count):
		if tour_count < 1000:
			place(visited,cur_move)
			if move_count < total_moves:
				for move in k_li[cur_move]:
					if visited[move] == 0:
						tour_count = recur(move,move_count+1,tour_count)
			elif move_count == total_moves:
				tour_count = tour_count + 1
				print (tour_count)
			remove(visited,cur_move)
		return tour_count


for i in range(1,2):
	tour_count = recur(i,1,0)
	print (tour_count)

