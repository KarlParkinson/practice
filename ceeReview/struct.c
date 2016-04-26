#include <stdio.h>
#include <stdlib.h>

struct Point {
  int x;
  int y;
};

struct Point addPoints(struct Point p1, struct Point p2) {
  struct Point p3;
  p3.x = p1.x + p2.x;
  p3.y = p1.y+p2.y;
  return p3;
}

struct Point* addPoints2(struct Point* p1, struct Point* p2){
  struct Point* p3 = (struct Point*) malloc(sizeof(struct Point));
  p3 -> x = p1 -> x + p2 -> x;
  p3 -> y = p1 -> y + p2 -> y;
  return p3;
}

int main() {
  struct Point p;
  p.x = 2;
  p.y = 3;

  struct Point q = {25,35};

  printf("%d, %d\n", p.x, p.y);
  printf("%d, %d\n", q.x, q.y);
  
  struct Point r = addPoints(p,q);
  printf("%d, %d\n", r.x, r.y);

  struct Point *z = addPoints2(&p, &q);
  printf("%d, %d\n", z-> x, z-> y);
  return 0;
}
    
