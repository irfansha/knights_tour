//this is a simple backtraking algorithm to find number of knight's open tour.

//can be improved by giving the moves in early. improved tp knights_tour_sep_rec.cpp which is faster.

#include <iostream>
#include <vector>
#include <bitset>

std::vector<bool> knight;

int count = 0, N;

int depth;

# define M_moves 8

//the knight that can go.
int moves[M_moves][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

void knight_backtracking(int x, int y, int size) {
	//std::cout << int (bitset_vect[(x-1) * N + y]) << "\n"; 
	if (size == depth) ++count;
	else if (size < depth){
	int n_x , n_y;
	for (int i = 0 ; i < M_moves ; ++i) {
			n_x = x + moves[i][0];
			n_y = y + moves[i][1];
			if (n_x > 0 and n_y > 0 and n_x <= N and n_y <= N and knight[(n_x-1) * N + n_y] == 0) {
			knight[(x-1) * N + y] = 1;		
			knight_backtracking(n_x,n_y,size+1);
			knight[(x-1) * N + y] = 0; }
		}
	}
}


int main(const int argc, const char* const argv[]) {
  if (argc != 2) { std::cout << "Usage[qcount]: N\n"; return 0; }
  const unsigned long arg1 = std::stoul(argv[1]);
  N = arg1;
	depth = N*N;
  knight.resize(N*N+1);
	for (int i = 1 ; i <= N ; ++i)
		for (int j = 1 ; j <= N ; ++j) {
			count = 0;
			std::cout << i << " " << j << "\n" ;
			knight[(i-1) * N + j] = 1;			
			knight_backtracking(i,j,1);
			knight[(i-1) * N + j] = 0;
			std::cout << count << "\n";
}
}
