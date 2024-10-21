#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int firstOccurrence(char *line){
    for(int i = 0; i<strlen(line); i++){
        if(line[i] == '*'){
            return i;
            break;
        }
    }
    return -1;
}

int main (void) {
    int num = 0;
    scanf("%d", &num);
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
    return 0;
}