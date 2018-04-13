#include <stdio.h>

const int N = 2;

float f(float *A) {
  printf("%f, %f\n", A[0], A[1]);
  A[0] = 1.2345f;
  return 0.0f;
}

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

int main() {
  float A[N] = {1.0f, 2.0f};
  f(A);
  return 0;
}