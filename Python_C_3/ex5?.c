#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) {
    int num = 0;
    scanf("%d", &num);
    char line[100] = "";
    for(int i = 0; i<num; i++){
        strcat(line, " ");
        if(i == num-1){
            strcat(line, "*");
            break;
        }
    }
    for (int i = num; i>=0; i--){
        line[-1+i] = '*';
        line[strlen(line)-1-i] = '*';
        printf("%s\n", line);
    }
    return 0;
}