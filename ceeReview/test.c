#include "test.h"
#include <stdio.h>

int foo (int x) {
  return x*2;
}

int bar (int y) {
  return y+7;
}

int main() {

  printf("%d\n", foo(8));
  printf("%d\n", bar(5));
  
}
  
