#include<stdio.h>

int main ( void ) {
    int i = 3 ; 
    int j = 5 ; // Declaration of integer variables i and j, with initial values 3 and 5
    float x = 3.0 ; // Declaration of float variables with initial value 3.0
    printf ( " i = %d ; j = %d ; somme = %d ; \n" , i , j , i + j ) ; // Output of the text with the corresponding values 
    i = j / 2 ; // Reevaluation of i's value
    float y = x / 2 ; 
    float z = j / 2 ;
    printf ( " i = %d ; \n y = %f ; z = %f ; \n" , i , y , z ) ;
    return 0 ;
}
