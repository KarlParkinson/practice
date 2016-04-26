#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  const int N = 4;
  char inp[N];

  fgets(inp, N, stdin);
  printf ("Read in: %s\n", inp);
}
