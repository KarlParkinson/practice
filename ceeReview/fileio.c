#include <stdio.h>
#include <stdlib.h>

int main() {
  int N = 100;
  FILE *fp = fopen("number.txt", "w");
  if (!fp) {
    perror("file open error");
    exit(10);
  }
  for (int i = 0; i <= N; i++) {
    fprintf(fp, "%d\n", i);
  }

  fclose(fp);

  fp = fopen("number.txt", "r");
  int s = 0;
  for (int i = 0; i <= N; i++) {
    int x;
    fscanf(fp, "%d", &x);
    s += x;
  }
  fclose(fp);
  printf("%d\n", s);

  int a[] = {1,2,3};
  fp = fopen("test.txt", "w");
  fwrite(a, sizeof(int), 3, fp);
  fclose(fp);
  fp = fopen("test.txt", "r");
  int b[3];
  fread(b, sizeof(int), 3, fp);
  fclose(fp);
  for (int i = 0; i < 3; i++) {
    fprintf(stdout, "%d\n", b[i]);
  }
  return 0;
}
