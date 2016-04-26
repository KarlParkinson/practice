#include <stdio.h>
#include <stdlib.h>

int main() {
  char c;

  while ((c = getchar()) != EOF) {
    printf ("%c", c);
  }
  return 0;
}
