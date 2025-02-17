#include <stdio.h>

int main() {
    char c;
    for(c="A"; c<="Z"; c++){
        // Converting a char to an int gives out its ASCII value, substracting 32 to it gives out the value of the cap.
        printf("caractère %c ASCII %d\n", c, c);
    }
    int i;
    for(i=0; i<=9;i++){
        printf("chiffre %d ASCII %d\n",i ,i+'0');
    }
}