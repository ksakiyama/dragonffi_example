const long long N = 1000;
long long MEMO[1000];

long long f(long long n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  }

  if (MEMO[n]) {
    return MEMO[n];
  }

  long long m = f(n-1) + f(n-2);
  MEMO[n] = m;
  return m; 
}
