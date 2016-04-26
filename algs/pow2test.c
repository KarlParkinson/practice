#include <stdio.h>


bool pow2test(unsigned int x) {
  return (x == (~x)^0xFFFFFFFF);
}


int main() {
  int x = 0;
  if (pow2test(x)) {
    printf("Hell yes!\n");
  } else {
    printf("Hell no!\n");
  }
  return 0;
}
