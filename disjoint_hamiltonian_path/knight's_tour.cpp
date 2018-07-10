//this is for taking advantage of disjointness of knights path.

#include <iostream>
#include <vector>
#include <bitset>

std::vector<bool> knight;

int count = 0, N;

int depth;
typedef std::uint_fast64_t knight_t; //for knight problem N <= 8.  change it for bigger problems
# define M_moves 8
std::vector<knight_t> bitset_vect;
//the knight that can go.
int moves[M_moves][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

void bitset_init() {
	knight_t val = knight_t(1);
	for ( int i = 1 ; i <= N*N ; ++i ) {
		bitset_vect.push_back(val);
		val <<= 1;
		}
}

void zero() {
	std::fill(knight.begin(), knight.end(), 0);
}

void knight_backtracking(int x, int y, int size, knight_t path) {
	path |= bitset_vect[(x-1) * N + y];
	//std::cout << int (bitset_vect[(x-1) * N + y]) << "\n"; 
	if (size == depth) ++count;
	else if (size < depth){
	int n_x , n_y;
	for (int i = 0 ; i < M_moves ; ++i) {
			n_x = x + moves[i][0];
			n_y = y + moves[i][1];
			if (n_x > 0 and n_y > 0 and n_x <= N and n_y <= N and knight[(n_x-1) * N + n_y] == 0) {
			knight[(x-1) * N + y] = 1;		
			knight_backtracking(n_x,n_y,size+1,path);
			knight[(x-1) * N + y] = 0; }
		}
	}
}


int main(const int argc, const char* const argv[]) {
  if (argc != 2) { std::cout << "Usage[qcount]: N\n"; return 0; }
  const unsigned long arg1 = std::stoul(argv[1]);
  N = arg1;
	depth = N;
	knight_t path = 0;
  knight.resize(N*N+1);
	bitset_init();
	for (int i = 1 ; i <= N ; ++i)
		for (int j = 1 ; j <= N ; ++j) {
			//zero();
			std::cout << i << " " << j << "\n" ;
			knight_backtracking(i,j,1,path);}

	std::cout << count << "\n";

	//for (auto i : bitset_vect) std::cout << std::bitset<25> {i} << "\n";
}
