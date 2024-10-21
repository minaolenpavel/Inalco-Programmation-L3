#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) {
    int num = 0;
    scanf("%d", &num);
    char line[100] = "";
    for(int i = 0; i<num; i++){
        strcat(line, "*");
    }
    for (int i = 0; i<num; i++){
        line[-1+i] = ' '; // Double quotes are used to replace whole strings and double quotes are used for single chars
        line[strlen(line)-1-i] = ' ';
        printf("%s\n", line);
    }
    return 0;
}