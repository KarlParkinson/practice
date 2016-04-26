#include <stdio.h>

int main() {
  const int N = 6;
  int A[N];
  int *a = A;

  for (int i = 0; i < N; i++) {
    *(a+i) = i*i;
  }

  for (int i = 0; i < N; i++){
    printf("%d\n", A[i]);
  }

  int **p;
  int *b = a+2;
  p = &b;
  printf("%d\n", **p);

}
