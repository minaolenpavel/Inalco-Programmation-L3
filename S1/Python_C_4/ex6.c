#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main () {
    srand(time(NULL));
    int r = (rand() % 10) + 1;
    printf("Essayez de deviner le nombre auquel je pense\n");
    int attempts = 0;
    while(1==1){
        int guess = 0;
        scanf("%d", &guess);
        if(guess == r){
            attempts++;
            printf("Féliciations, vous avez gagné en %d essais !\n", attempts);
            break;
        }
        else if (guess > r)
        {
            attempts++;
            printf("Trop grand\n");
        }
        else if (guess < r)
        {
            attempts++;
            printf("Trop petit\n");
        }
        if(attempts == 2){
            printf("Vous avez perdu ! Le nombre était %d\n", r);
            break;
        }
    }
    
    return 0;
}