#include <stdio.h>
#include <stdbool.h>

int main() {
  int i;
  double j;
  float f;
  short s;
  bool flag;
  char c;

  printf("%d\n", sizeof(i));
  printf("%d\n", sizeof(j));
  printf("%d\n", sizeof(f));
  printf("%d\n", sizeof(s));
  printf("%d\n", sizeof(flag));
  printf("%d\n", sizeof(c));

  return 0;
}
