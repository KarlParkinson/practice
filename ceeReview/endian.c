#include <stdio.h>
#include <stdlib.h>

void reverse_bytes(int *p) {
  char *y = (char*) p;
  char *t;
  t = y[0];
  y[0] = y[3];
  y[3] = t;
  t = y[1];
  y[1] = y[2];
  y[2] = t;

}

int main() {
  int *x = malloc(1*sizeof(int));
  *x = 1;
  char *y = (char*) x;
  printf("%d\n", y[0]);
  free(x);
  
  int z = 256;
  reverse_bytes(&z);
  printf("%d\n", z);

}
