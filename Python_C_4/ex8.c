#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846

double perimetre(int r){
    return r*2*M_PI;
}

double aire(int r){
    return pow(r, 2)*M_PI;
}

int main () {
    printf("Indiquer le rayon du disque : ");
    int r;
    scanf("%d", &r);
    printf("\n");
    printf("Le perimètre d'un disque d'aire %d est de %f et son aire est de %f\n", r, perimetre(r), aire(r));
    return 0;
}