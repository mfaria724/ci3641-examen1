#include <stdio.h>

/*
  Realiza el "shift" del resultado de los ultimos 22 elementos
*/
void shift_izquierda(int *arr) {  

  int temp = *(arr + 1) + *(arr + 8) + *(arr + 15);
  for(int i=0; i < 21; i++) {
    *arr=*(arr + 1);
    arr = arr + 1;
  }
  *arr = temp;
}

/*
  Iniciaizador de los 22 casos base.
*/
int pregunta5(int n) {

  int respuestas5[22];

  for (int i = 0; i < 22; i++)
    respuestas5[i] = i;

  int j = 0;

  while (n != j)
  {
    shift_izquierda(respuestas5);
    j++;
  }

  return *respuestas5;
}

/*
  Cliente
*/
int main() {
  int number;
  printf("Enter an integer: ");  
  
  // reads and stores input
  scanf("%d", &number);

  printf("\nResult: %d\n", pregunta5(number));
  return 0;
}
