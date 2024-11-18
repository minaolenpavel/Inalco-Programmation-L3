#include <stdio.h>

int main(void) {
    float a = 5.0;
    float b = 2.0;
    int c = (int)(a / b);
    float d = a / b;

    printf("entier c: %d\n", c);
    printf("reel d: %f\n", d);
    
    return 0;
}
