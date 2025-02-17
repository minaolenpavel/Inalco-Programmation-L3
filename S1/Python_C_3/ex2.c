#include <stdio.h>
#include <stdbool.h>

int main (void) {
    printf("Choisissez une des options ci-dessous :\n");
    printf ("b : bleu\n");
    printf ("n : noir\n");
    printf ("r : rouge\n");
    printf ("v : vert\n");
    printf("q : quitter\n");

    bool answered = 0;
    while(!answered){
        char a;
        scanf("%c", &a);
        if(a == 'b'){
            printf("L'utilisateur a choisi le bleu !\n");
            break;
        }
        else if(a=='n'){
            printf("L'utilisateur a choisi le noir !\n");
            break;
        }
        else if(a=='r'){
            printf("L'utilisateur a choisi le rouge !\n");
            break;
        }
        else if(a=='v'){
            printf("L'utilisateur a choisi le vert !\n");
            break;
        }
        else if(a=='q'){
            printf("au revoir !\n");
            break;
        }
        else{
            printf("Je n'ai pas compris, veuillez réessayer !");
        }
    }
    return 0;
}