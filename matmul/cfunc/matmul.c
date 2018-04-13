void matmul(double *A, double *B, double *C, int N) {
  int i, j, k;
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      for (k = 0; k < N; k++) {
        C[i * N + j] += A[i * N + k] * B[k * N + j];
      }
    }
  }
}

// optimize a little bit
void matmul_opt(double *A, double *B, double *C, int N) {
  int i, j, k;
  for (i = 0; i < N; i++) {
    for (k = 0; k < N; k++) {
      for (j = 0; j < N; j++) {
        C[i * N + j] += A[i * N + k] * B[k * N + j];
      }
    }
  }
}