#include <stdio.h>

int main (void) {
    float fahrenheit;
    scanf("%f", &fahrenheit);
    float celsius = (fahrenheit-32)* 0.55556;
    printf("%fF est égal à %fC \n", fahrenheit, celsius);
    return 0;
}