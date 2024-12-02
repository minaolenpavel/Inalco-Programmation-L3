#include <stdio.h>

int main () {
    int tableau[2][5] = {{0,1,2,3,4},
                         {5,6,7,8,9}};
    int array[5][2];

    for (int i = 0; i < 5; i++) {
        for (int y = 0; y < 2; y++) {
            array[i][y] = tableau[y][i];
        }
    }

    for (int i = 0; i < 5; i++) {      
        for (int y = 0; y < 2; y++) {  
            printf("%d", array[i][y]); 
        }
        printf("\n");
    }

    return 0;
}
