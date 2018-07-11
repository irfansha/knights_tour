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


def place(move_count,visited,cur_move):
	visited[cur_move] = 1
	return move_count + 1

def remove(move_count,visited,cur_move):
	visited[cur_move] = 0
	return move_count - 1

def n_check(n):
	temp = []
	for next_nr in k_li[n]:
		if islands[next_nr] != -1:
			temp.append(next_nr)
	return temp

def reset(islands):
	temp = sorted(islands)
	for i in range(len(temp)):
		if temp[i] != -1 :
			new_i = islands.index(temp[i])
			islands[new_i] = i

def island_add(temp_islands,cur_move):
	for nr in k_li[cur_move]:
		temp = n_check(nr)
		min_temp = max(temp_islands)
		if temp == [] :
			temp_islands[nr] = max(temp_islands) + 1
		else:
			for i in temp:
				if islands[i] < min_temp :
					min_temp = temp_islands[i]
			for i in temp:
				temp_islands[i] = min_temp

def island_del(temp_islands,cur_move):
	temp_islands[cur_move] = -1


def recur(cur_move,island,move_count,tour_count):
		print (islands)
		if max(islands) > total_moves :
			reset(islands)
		move_count = place(move_count,visited,cur_move)
		temp_islands = list(islands)
		island_del(temp_islands,cur_move)
		island_add(temp_islands,cur_move)
		if move_count < total_moves:
			for move in k_li[cur_move]:
				if visited[move] == 0:
					tour_count = recur(move,temp_islands,move_count,tour_count)
		elif move_count == total_moves:
			tour_count = tour_count + 1
		move_count = remove(move_count,visited,cur_move)
		return tour_count

island = []

for i in range(1,2):
	tour_count = recur(i,island,0,0)
	print (tour_count)

