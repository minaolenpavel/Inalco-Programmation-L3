#include <stdio.h>
// Pair ou impair
int main (void) {
    int num;
    printf("Entrez un nombre et découvrez s'il est pair ou impair : ");
    scanf("%d", &num);
    if(num%2 == 0){
        printf("%d est pair !\n", num);
    }
    else{
        printf("%d est impair !\n", num);
    }
    return 0;
}