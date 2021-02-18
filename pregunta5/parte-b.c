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
  metodo auxiliar que corre una ventana con las ultimas 22 solciones para
  calcular la solucion que se necesita.
*/
int pregunta5_aux(int *respuestas, int i, int n) {
  if (n == i)
    return *respuestas;

  shift_izquierda(respuestas);

  return pregunta5_aux(respuestas, i + 1, n);
}

/*
  Iniciaizador de los 22 casos base.
*/
int pregunta5(int n) {

  int respuestas5[22];

  for (int i = 0; i < 22; i++)
    respuestas5[i] = i;

  return pregunta5_aux(respuestas5, 0, n);
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
