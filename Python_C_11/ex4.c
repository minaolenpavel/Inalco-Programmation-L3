#include <stdio.h>

int fib(int num){
    if(num <= 1){
        return num;
    }
    else if (num > 1){
        return fib(num-1)+fib(num-2);
    }
}

int main () {   
    int result = fib(10);
    printf("%d\n", result);
    return 0;
}