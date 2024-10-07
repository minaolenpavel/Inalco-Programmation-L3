#include <stdio.h>
#include <stdbool.h>

// Function to get the length of an integer
int lengthof(int i){
    int length = 0;
    bool done = 0;
    // Each iteration the int is divided by 10 and we increment length
    // When i is equal to 0, we're done, it means that there is enough decimals to have only 0, 
    // ex : 453 => 0.453, 3 decimals so length is 3
    while (!done){
        i = i/10;
        length++;
        if(i==0){
            done = 1;
        }
    }
    return length;
}


int main (void) {
    printf("Entrez un nombre et découvrez si il est narcissique : ");
    int num;
    scanf("%d\n", num);

    if(num >= 1 && num<=9){
        printf("%d est un nombre narcissique !\n");
    }
    else{
        int length = lengthof(num);
        int* numbers = malloc(length*sizeof(int));
        for(int i = 0; i<=length; i++){
            // Algo with module and division, modulo for two digit numbers and division for more, till the number gets to a two num digit
        }
    }
    return 0;
}