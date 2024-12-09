#include <stdio.h>
#include "../my_lib.c"

int main () {
    int tableau[100];
    for(int i = 0; i<100; i++){
        tableau[i] = i;
    }
    for(int i = 0; i<100; i++){
        if(int_array_last_element(split_numbers(tableau[i])) == 9){
            printf("%d\n", tableau[i]);
        }
        else if(tableau[i] == 9){
            printf("%d\n", tableau[i]);
        }
        else{
            printf("%d, ", tableau[i]);
        }
    }
    return 0;
}