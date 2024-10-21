#include <stdio.h>
#include <string.h>

int main (void) {
    int num = 0;
    scanf("%d", &num);
    char line[100] = "";
    for(int i = 0; i<num; i++){
        strcat(line, "*");
    }
    for(int i =0; i<num; i++){
    printf("%s\n", line);
    }
    return 0;
}