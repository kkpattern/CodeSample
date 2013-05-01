/*
 * Author: Kai Zhang
 * Email: kylerzhang11@gmail.com
 *
 * Problem Statement
 *     
 * Manao is conducting an experiment to measure the humidity level of some
 * spongy material. The experiment is conducted in a closed room which is
 * observed from a side, so we will consider it in two dimensions.  The room is
 * N centimeters wide. There are N drop counters built in the ceiling of the
 * room. Drop counter 0 is attached 0.5 centimeters from the left end of the
 * room, and each next one is attached 1 centimeter to the right of the previous
 * one. The i-th (0-based index) drop counter drips intensity[i] drops per
 * minute.  There are also M sponges in the room. The i-th (0-based) sponge is
 * horizontally attached (i+1) centimeters below the ceiling and its left end is
 * leftEnd[i] centimeters apart from the left wall of the room. All sponges are
 * exactly L centimeters long and their thickness is negligible. Each sponge
 * will totally absorb every drop that drips at it.    You are given a vector
 * <int> intensity containing exactly N elements, a vector <int> leftEnd
 * containing exactly M elements and a int L. You have to model the experiment
 * that Manao is conducting to compute the amount of drops that each sponge will
 * absorb per minute. Return a vector <int> of length M, where i-th element will
 * be the number of drops absorbed by the i-th sponge.
 *
 * Definition
 *     
 * Class:
 * TheExperimentDiv2
 * Method:
 * determineHumidity
 * Parameters:
 * vector <int>, int, vector <int>
 * Returns:
 * vector <int>
 * Method signature:
 * vector <int> determineHumidity(vector <int> intensity, int L, vector <int>
 * leftEnd)
 * (be sure your method is public)
 *     
 *
 * Constraints
 * - intensity will contain N elements, where N is between 1 and 50, inclusive.
 * - Each element of intensity will be between 1 and 1000, inclusive.
 * - L will be between 1 and N, inclusive.
 * - leftEnd will contain M elements, where M is between 1 and 50, inclusive.
 * - Each element of leftEnd will be between 0 and N - L, inclusive.
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
int tbl[51][51];

class TheExperimentDiv2 {
 public:
  vector <int> determineHumidity(vector <int> intensity,
                                 int L,
                                 vector <int> leftEnd) {
    fill_n(&tbl[0][0], sizeof(tbl)/sizeof(tbl[0][0]), -1);
    for (int i = 0; i < leftEnd.size(); ++i) {
      int height = i+1;
      for (int j = leftEnd[i]; j < leftEnd[i]+L; ++j) {
        tbl[height][j] = i;
      }
    }
    vector<int> ans;
    ans.resize(leftEnd.size(), 0);
    for (int i = 0; i < intensity.size(); ++i) {
      for (int j = 0; j < 51; ++j) {
        if (tbl[j][i] != -1) {
          ans[tbl[j][i]] += intensity[i];
        }
      }
    }
    return ans;
  }
};

int main() {
  return 0;
}
