#include <stdio.h>

int min_two(int num1, int num2){
    if(num1> num2){
        return num2;
    }
    else{
        return num1;
    }
}

int min_three(int num1, int num2, int num3){
    int min = num1;
    if(min> num3){
        min = num3;
        if(min>num2){
            min = num2;
        }
    }
    else if (min>num2)
    {
        min = num2;
        if(min> num3){
            min = num3;
        }
    }
    return min;
}


int main () {
    printf("%d\n", min_three(1,2,3));
    return 0;
}

