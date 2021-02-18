#include <stdio.h>

int pregunta5(int n) {
  if (0 <= n && n <= 21)
    return n;
  
  return pregunta5(n-7) + pregunta5(n-14) + pregunta5(n-21);
}

int main() {
  int number;
  printf("Enter an integer: ");  
  
  // reads and stores input
  scanf("%d", &number);

  printf("Result: %d", pregunta5(number));
  return 0;
}
