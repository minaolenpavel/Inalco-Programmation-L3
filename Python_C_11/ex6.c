#include <stdio.h>

int dec_bin(dec_num){
    if (dec_num == 0){
        return 0;
    }
    else{
        return (dec_num %2+10*dec_bin(dec_num/2));
    }
}

int main () {
    printf("%d\n", dec_bin(201));
    return 0;
}