#include <stdio.h>

int main() {

  int k = -16;
  k = k >> 1; /* should be -8 */
  printf("%d\n", k);
  k = k >> 1; /* should be -4 */
  k = k >> 1; /* should be -2 */
  k = k >> 1; /* should be -1 */
  printf("%d\n", k);
  k = k >> 1; /* should be -1 */
  printf("%d\n", k);
  k = k >> 8;
  printf("%d\n", k);

  int j = 16;
  j = j >> 4;
  printf("%d\n", j);
  j = j >> 1; /* should be 0 */
  printf("%d\n", j);
  j = j >> 1;
  printf("%d\n", j);


  k = k << 5; /* should be -32 */
  printf("%d\n", k);

  unsigned short a = 0xFFFF;
  printf("%d\n", a);
  a = a & 0x00FF;
  printf("%d\n", a);

  unsigned int b = 0x80000000;
  printf("%d\n", b);

  bool x = 1;
  x = x << 2;
  printf("%d\n", x);

}
