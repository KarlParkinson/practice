#include <stdio.h>
#include <stdlib.h>

int main() {
  int sum = 0;
  int res;

  int in;

  for (;;) {
    res = scanf("%d", &in);
    if (res == EOF) {
      if (feof(stdin)) {
	break;
      } else {
	printf("Error occurred\n");
	return 1;
      }
    } else {
      sum = sum + in;
    }
  }

  printf("sum is: %d\n", sum);
  return 0;

}
