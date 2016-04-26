#include <stdio.h>
#include <stdlib.h>

int main() {
  const int N = 1000;
  int *arr = malloc(N * sizeof(int));
  for (int i = 0; i < N; i++){
    arr[i] = i+1;
  }

  for (int i = 0; i < N; i++){
    printf("%d\n", arr[i]);
  }

  free(arr);
  arr = 0;
  arr[4] = 7;
  return 0;
}
