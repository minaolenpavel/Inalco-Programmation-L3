#include <stdio.h>
#include <stdbool.h>
#define LEN 4

bool is_positive(int number){
    if (number >= 0){
        return true;
    }
    else{
        return false;
    }
}

int positive(){
    bool ok = false;
    int num;
    while(ok == false){
        printf("Entrez un nombre positif : ");
        scanf("%d", &num);
        ok = is_positive(num);
    }
    return num;
}

float average(int* numbers){
    float avg;
    for(int i = 0; i<LEN; i++){
        avg+=numbers[i];
    }
    avg = avg/LEN;
    return avg;
}

int main () {
    int array[4];
    for(int i =0; i<LEN; i++){
        array[i] = positive();
    }
    printf("%.2f\n", average(array));
    return 0;
}