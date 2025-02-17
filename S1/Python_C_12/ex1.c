#include <stdio.h>

int main () {
    int tableau[10];
    int total = 0;
    for(int i = 0; i<10; i++){
        tableau[i] = i;
        total+=i;
    }
    for(int i = 0; i<10; i++){
        printf("%d\n", i);
    }
    printf("moyenne = %d\ntotal = %d\n", total/10, total);
    return 0;
}