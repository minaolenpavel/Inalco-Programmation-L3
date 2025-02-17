#include <stdio.h>
#include <stdbool.h>
#define ROCK 0
#define PAPER 1
#define SCISSORS 2

void print_rules(){
    printf("0 : pierre\n1 : papier\n2 : ciseaux\n");
}

bool check_rps(int rps){
    if (rps == ROCK || rps == PAPER || rps == SCISSORS)
    {
        return true;
    }
    else{
        return false;
    }
}

int arbitre(int j1, int j2){
    if(j1 == j2){
        return 0; //Match null, réponses identiques
    }
    else if((j1 == ROCK && j2 == SCISSORS)||
            (j1 == PAPER && j2 == ROCK)||
            (j1 == SCISSORS && j2 == PAPER)){
        return 1; // J1 gagne
    }
    else{
        return 2; // J2 gagne
    }
}

void game(){
    bool j1_played = false;
    bool j2_played = false;
    int j1;
    int j2;
    while (j1_played == false){
        print_rules();
        printf("Tour de J1 : ");
        scanf("%d", &j1);
        if(check_rps(j1) == true){
            j1_played = true;
        }
        else{
            printf("Je n'ai pas compris.");
        }
    }
    while (j2_played == false)
    {
        print_rules();
        printf("Tour de J2 : ");
        scanf("%d", &j2);
        if(check_rps(j2) == true){
            j2_played = true;
        }
        else{
            printf("Je n'ai pas compris.");
        }
    }
    if(arbitre(j1,j2) == 0){
        printf("Match nul\n");
    }
    else if (arbitre(j1,j2) == 1){
        printf("J1 gagne\n");
    }
    else{
        printf("J2 gagne\n");
    }
}

int main () {
    printf("Combien de tours souhaitez-vous jouer ? ");
    int turns;
    scanf("%d", &turns);
    for(int i = 0; i<turns; i++){
        game();
    }
    return 0;
}