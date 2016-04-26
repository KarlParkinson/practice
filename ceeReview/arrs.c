#include <stdio.h>
#include <stdlib.h>

int main() {

  int A[7];

  for (int i = 0; i < 7; i++) {
    A[i] = i*i;
  }

  for (int i = 0; i <= 7; i++) {
    printf("%d\n", A[i]);
  }

  printf("%p\n", A);
}
