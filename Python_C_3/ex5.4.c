#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool checkStar(char *line){
    for(int i = 0; i<strlen(line); i++){
        if(line[i] == '*'){
            return 1;
            break;
        }
    }
    return 0;
}

void bottom(void){
    int num = 5;
    int width = 2 * num - 1; // width of each line in the pyramid, it's num * 2 so there is no problem of width or height
    char line[(num*2) + 1]; // Create an array of size num + 1 not to forget the null terminator
    memset(line, ' ', num*2); // Fill the array with spaces
    line[num*2] = '\0'; 
    line[num-1] = '*';
    for (int i = 0; i < num; i++) {
        int center = width / 2; // Recalculate each iteration the center 
        line[center - i] = '*';
        line[center + i] = '*';
        printf("%s\n", line);
    }
}

void top(void){
    int num = 10;
    char line[100] = "";
    for(int i = 0; i<num; i++){
        strcat(line, "*");
    }
    for (int i = 0; i<num; i++){
        if(checkStar(line) == 0){
            break;
        }
        else{
            line[-1+i] = ' '; // Double quotes are used to replace whole strings and double quotes are used for single chars
            line[strlen(line)-1-i] = ' ';
            printf("%s\n", line);
        }
    }
}

int main (void) {
    top();
    bottom();
    return 0;
}