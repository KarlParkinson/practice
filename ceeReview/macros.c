#include <stdio.h>

int main() {
#define FOR(i,n) for (i = 0; i < n; i++)

  int i;
  FOR(i,12) {
    printf("%d\n", i);
  }
  return 0;


}
