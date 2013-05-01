/*
 * Author: Kai Zhang
 * Email: kylerzhang11@gmail.com
 *
 * Problem Statement
 *     
 * You might remember the old computer arcade games. Here is one about Manao.
 * The game level is an NxM grid of equal cells. The bottom of some cells has a
 * platform at which Manao can stand. All the cells in the bottommost row
 * contain a platform, thus covering the whole ground of the level. The rows of
 * the grid are numbered from 1 to N starting from the top and the columns are
 * numbered from 1 to M starting from the left. Exactly one cell contains a coin
 * and Manao needs to obtain it.  Initially, Manao is standing on the ground,
 * i.e., in the bottommost row. He can move between two horizontally adjacent
 * cells if both contain a platform. Also, Manao has a ladder which he can use
 * to climb. He can use the ladder to climb both up and down. If the ladder is L
 * units long, Manao can climb between two cells (i1, j) and (i2, j) if both
 * contain a platform and |i1-i2| <= L. Note that Manao carries the ladder
 * along, so he can use it multiple times. You need to determine the minimum
 * ladder length L which is sufficient to acquire the coin.  Take a look at the
 * following picture. On this level, Manao will manage to get the coin with a
 * ladder of length 2.    You are given a vector <int> level containing N
 * elements. The j-th character in the i-th row of level is 'X' if cell (i+1,
 * j+1) contains a platform and '.' otherwise. You are also given ints coinRow
 * and coinColumn. The coin which Manao seeks is located in cell (coinRow,
 * coinColumn) and it is guaranteed that this cell contains a platform.  Return
 * the minimum L such that ladder of length L is enough to get the coin. If
 * Manao can perform the task without using the ladder, return 0.
 *
 * Definition
 *     
 * Class:
 * ArcadeManao
 * Method:
 * shortestLadder
 * Parameters:
 * vector <string>, int, int
 * Returns:
 * int
 * Method signature:
 * int shortestLadder(vector <string> level, int coinRow, int coinColumn)
 * (be sure your method is public)
 *     
 *
 * Notes
 * - Manao is not allowed to fall. The only way in which he may change his
 * vertical coordinate is by using the ladder.
 *
 * Constraints
 * - level will contain N elements, where N is between 1 and 50, inclusive.
 * - Each element of level will be M characters long, where M is between 1 and
 *   50, inclusive.
 * - Each element of level will consist of '.' and 'X' characters only.
 * - The last element of level will be entirely filled with 'X'.
 * - coinRow will be between 1 and N, inclusive.
 * - coinColumn will be between 1 and M, inclusive.
 * - level[coinRow - 1][coinColumn - 1] will be 'X'.
 */
#include <stdio.h>

#include <algorithm>
#include <limits>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// const int IINF = numeric_limits<int>::max();
// const long long LLINF = numeric_limits<long long>::max();
//
int dest[51][51];

class ArcadeManao {
 public:
  void search(const vector<string> &level, int l) {
    fill_n(&dest[0][0], sizeof(dest)/sizeof(dest[0][0]), 0);
    int x = level.size()-1;
    int y = 0;
    dest[x][y] = 1;
    list<pair<int, int> > q;
    q.push_back(make_pair(x, y));
    while (!q.empty()) {
      pair<int, int> position = q.front();
      q.pop_front();
      int x = position.first;
      int y = position.second;
      if (y-1 >= 0 && level[x][y-1] == 'X' && dest[x][y-1] == 0) {
        dest[x][y-1] = 1;
        q.push_back(make_pair(x, y-1));
      }
      if (y+1 < level[0].size() && level[x][y+1] == 'X' && dest[x][y+1] == 0) {
        dest[x][y+1] = 1;
        q.push_back(make_pair(x, y+1));
      }
      for (int i = x+1; i <= x+l && i < level.size(); ++i) {
        if (level[i][y] == 'X' && dest[i][y] == 0) {
          dest[i][y] = 1;
          q.push_back(make_pair(i, y));
        }
      }
      for (int i = x-1; i >= x-l && i >= 0; --i) {
        if (level[i][y] == 'X' && dest[i][y] == 0) {
          dest[i][y] = 1;
          q.push_back(make_pair(i, y));
        }
      }
    }

  }
  int shortestLadder(vector <string> level, int coinRow, int coinColumn) {
    int height = level.size();
    int width = level[0].size();
    for (int i = 0; i <= height; ++i) {
      search(level, i);
      if (dest[coinRow-1][coinColumn-1] == 1)
        return i;
    }
    return height;
  }
};

int main() {
  return 0;
}
