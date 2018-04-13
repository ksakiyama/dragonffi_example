#include <stdio.h>

const int N = 100; // 最大で100まで
int MEMO[100];

int f(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  }

  if (MEMO[n]) {
    return MEMO[n];
  }

  int m = f(n-1) + f(n-2);
  MEMO[n] = m;
  return m; 
}

int main() {
  printf("%d\n", f(10));
}