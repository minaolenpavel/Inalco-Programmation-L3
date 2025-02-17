#include <stdio.h>


int main () {
    // Creation of array size 8, considering the \0 char
    // Max size of each string in the array is 10
    char days[8][10] = {"lundi", "mardi","mercredi", "jeudi", "vendredi", "samedi", "dimanche"};
    int currentNbDay = 5;
    int currentDateDay = 1;
    int currentDateMonth = 1;
    char* currentDay = days[currentNbDay];

    while(!(currentDateDay == 7 && currentDateMonth == 2)){
        currentDay = days[currentNbDay];  
        printf("%s %d\n", currentDay, currentDateDay);
        currentNbDay++;
        currentDateDay++;
        if(currentNbDay == 7){
            currentNbDay = 0;
        }
        if(currentDateDay == 32){
            currentDateDay = 1;
            currentDateMonth++;
        }
    }
    currentDay = days[currentNbDay];
    printf("le %d février est un %s !\n", currentDateDay, currentDay);
    return 0;
}

