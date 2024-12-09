#include <stdio.h>
#include <stdbool.h>

bool is_positive(int number){
    if (number >= 0){
        return true;
    }
    else{
        return false;
    }
}

bool is_even(int number){
    if (number%2==0){
        return true;
    }
    else{
        return false;
    }
}