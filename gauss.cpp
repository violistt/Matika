#include <bits/stdc++.h>

using namespace std;

vector<int> solve(vector<vector<int>> matrix) {
  int n = matrix.size();
  vector<int> finished(n, -1);
  for (int j = 0; j < n; j++) {
    for (int i = 0; i < n; i++) {
      if (matrix[i][j] && finished[i] == -1) {
        for (int ii = 0; ii < n; ii++) {
          if (ii == i) continue;
          if (matrix[ii][j] == 0) continue;
          for (int jj = j; jj <= n; jj++) {
            matrix[ii][jj] ^= matrix[i][jj];
          }
        }
        finished[i] = j;
        break;
      }
      if (i == n - 1) {
        for (int ii = 0; ii < n; ii++) matrix[ii][j] = 0;
      }
    }
  }
  vector<int> solutions(n, 0);
  for (int i = 0; i < n; i++) if (finished[i] != -1) solutions[finished[i]] = matrix[i][n];
  for (int i = 0; i < n; i++) {
    if (finished[i] == -1) {
      int x = 0;
      for (int j = 0; j < n; j++) x ^= (matrix[i][j] & solutions[j]);
      if (x != matrix[i][n]) return {}; 
    }
  }
  return solutions;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<vector<int>> matrix = {{1, 3, 2}, {0, 6, 0}};
  vector<int> sol = solve(matrix);
  for (auto i : sol) cout << i << " ";
  return 0;
}
