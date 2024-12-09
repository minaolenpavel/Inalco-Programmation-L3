#include <stdio.h>
#include "../my_lib.c"

int sum(int num){
    if(num <= 1){
        return num;
    }
    else{
        return num + sum(num-1);
    }
}

int sum_pair(int num){
    if(num == 1){
        return 0;
    }
    else if(is_even(num) == false){
        return sum_pair(num-1);
    }
    else{
        return num + sum_pair(num-1);
    }
}

int main () {
    printf("%d\n", sum_pair(7));
    return 0;
}