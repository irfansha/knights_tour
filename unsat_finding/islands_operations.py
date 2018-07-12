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
