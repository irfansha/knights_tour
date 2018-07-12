import knight_moves
import sys
import pylab as p
import networkx as nx

N = int(sys.argv[1])

k_moves = knight_moves.gen_knight_moves(N)

visited = [0]*(N*N+1) # maintains if the vertex is visited

move_count = 0 # keeps track of number of moves made

total_moves = N*N

#print (k_moves)

G = nx.Graph()


for i in range(1,len(k_moves)):
	for nr in k_moves[i]:
		G.add_edge(i,nr)

cur_G = G.copy()

def place(visited,cur_move):
	visited[cur_move] = 1

def remove(visited,cur_move):
	visited[cur_move] = 0

def edge_remove(cur_G,cur_move,temp):
	for nr in temp:
		if (cur_G.has_edge(cur_move,nr) and visited[nr] != 1):
			cur_G.remove_edge(cur_move,nr)

def edge_add(cur_G,cur_move,temp):
	for nr in temp:
		cur_G.add_edge(cur_move,nr)


def recur(cur_G,cur_move,move_count,tour_count):
	#check if the graph is disconnected
	if (tour_count < 1000):
			place(visited,cur_move)
			if move_count < total_moves:
				for move in G[cur_move]:
					if visited[move] == 0:
						if(move_count < 1):
							temp = G.neighbors(cur_move)
							temp.remove(move)
							#print (cur_G.edges())
							edge_remove(cur_G,cur_move,temp)
							#print (cur_G.edges(),cur_move,temp)
							#print ("\n")
							if (nx.algorithms.is_connected(cur_G)):
								tour_count = recur(cur_G,move,move_count+1,tour_count)
							edge_add(cur_G,cur_move,temp)
						else:
								tour_count = recur(cur_G,move,move_count+1,tour_count)
			elif move_count == total_moves:
				tour_count = tour_count + 1
				print (tour_count)
			remove(visited,cur_move)
	return tour_count


for i in range(1,2):
	tour_count = recur(cur_G,i,1,0)
	print (tour_count)
