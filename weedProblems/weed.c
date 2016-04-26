#include <stdio.h>

void reverse(char s[]) {
  int i = 0;
  while (s[i+1]) {
    i++;
  }
  int j = 0;
  char temp;
  while (j <= i) {
    temp = s[j];
    s[j] = s[i];
    s[i] = temp;
    j++;
    i--;
  }
}


int fib(int n) {
  if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
}

void gradeSchoolMult() {
  for (int i = 1; i <= 12; i++) {
    for (int j = 1; j <= 12; j++) {
      printf("%-3d  ", i*j);
    }
    printf("\n");
  }
}

void printOddNumbers() {
  for (int i = 1; i <= 99; i++) {
    if ((i%2)) {
      printf("%d\n", i);
    }
  }
}

int maxInt(int arr[], int n) {
  int max = arr[0];
  for (int i = 0; i < n; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

int main() {
  char s[] = "karl";
  reverse(s);
  /*printf("%s\n", s);
    printf("%d\n", fib(5));
    gradeSchoolMult();
    printOddNumbers();*/
  int arr[] = {1,4,2,8,2};
  printf("%d\n", maxInt(arr, 5));
  return 0;
}
