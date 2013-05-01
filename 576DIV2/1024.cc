/*
 * Author: Kai Zhang
 * Email: kylerzhang11@gmail.com
 *
 * Problem Statement
 *     
 * Manao has a matrix X with 10,000 rows and W columns. He likes to fill it with
 * characters; he even has developed an algorithm for this task. First, he
 * chooses a string S consisting of at most W lowercase letters. The string S is
 * called the generator. Then, he applies the algorithm described by the
 * following pseudocode:
 * cur := 0
 * for i := 0 to 9999
 *   for j := 0 to W - 1
 *       X[i][j] := S.charAt(cur)
 *           cur := (cur + 1) mod length(S)
 * Manao has recently found a matrix X in his notepad. He wonders
 * whether it was generated using the above algorithm. You are given:
 * a vector <string> fragment that contains a rectangular submatrix
 * of X,
 * the int W: the width of X,
 * and two ints i0 and j0: the coordinates of the upper left corner
 * of your submatrix within X.
 * In other words, for all valid i, j we have fragment[i][j] = X[i +
 * i0][j + j0]. Count how many different generators Manao could have
 * used to create a matrix X that contains the fragment you were
 * given. Return this number modulo 1,000,000,009.
 *
 * Definition
 *     
 * Class:
 * CharacterBoard2
 * Method:
 * countGenerators
 * Parameters:
 * vector <string>, int, int, int
 * Returns:
 * int
 * Method signature:
 * int countGenerators(vector <string> fragment, int W, int i0, int
 * j0)
 * (be sure your method is public)
 *     
 *
 * Constraints
 * - fragment will contain N elements, where N is between 1 and 10,
 *   inclusive.
 * - Each element of fragment will be M characters long, where M is
 *   between 1 and 10, inclusive.
 * - Each element of fragment will consist of lowercase letters
 *   ('a'-'z') only.
 * - W will be between M and 10,000, inclusive.
 * - i0 will be between 0 and 10,000 - N, inclusive.
 * - j0 will be between 0 and W - M, inclusive.
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

const int mod = 1000000009;
class CharacterBoard2 {
 public:
  bool construct(const vector<string> &fragment, string &s, int length) {
    for (int i = 0; i < fragment.size(); ++i) {
      for (int j = 0; j < fragment[0].size(); ++j) {
        int reali = i+i0_;
        int realj = j+j0_;
        int sp = (reali*w_+realj) % length;
        if (s[sp] != '?' && s[sp] != fragment[i][j]) return false;
        else s[sp] = fragment[i][j];
      }
    }
    return true;
  }
  int countGenerators(vector<string> fragment, int W, int i0, int j0) {
    i0_ = i0;
    j0_ = j0;
    w_ = W;
    long long ans = 0;
    for (int i = 1; i <= W; ++i) {
      string s(i, '?');
      if (construct(fragment, s, i)) {
        long long xcount = 1;
        for (int i = 0; i < s.size(); ++i) {
          if (s[i] == '?') xcount = (xcount*26) % mod;
        }
        ans += xcount;
        ans = ans % mod;
      }
    }
    return ans % mod;
  }
 private:
  int i0_;
  int j0_;
  int w_;
};

int main() {
  return 0;
}
