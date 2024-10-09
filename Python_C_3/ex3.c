#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int int_pow(int base, int exponent) {
    int result = 1;
    for(int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

// Function to get the length of an integer
int length_int(int i){
    int length = 0;
    bool done = 0;
    // Each iteration the int is divided by 10 and we increment length
    // When i is equal to 0, we're done, it means that there is enough decimals to have only 0, 
    // ex : 453 => 0.453, 3 decimals so length is 3
    while (!done){
        i = i/10;
        length++;
        if(i==0){
            done = 1;
        }
    }
    return length;
}

int length_array(int* array){
    int length = sizeof(array)/sizeof(array[0]);
    return length+1;
}

int* split_numbers(int num) {
    int length = length_int(num);
    // Allocation of memory to the array, equivalent to defining array length in C#
    int* numbers = malloc(length * sizeof(int));
    // Error handling for memory
    if (numbers == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    // Copy of num in order to avoid modify the original
    int temp_num = num;
    // Backwards iteration which removes the last digit with modulo
    // Extracts the last digit dividing by ten
    for(int i = length - 1; i >= 0; i--) {
        // Last digit extracted with modulo
        numbers[i] = temp_num % 10;
        // Then we divide the number by ten
        // And the quotient is used recursively with modulo
        temp_num = temp_num/10;
    }
    return numbers;
}

bool is_narcissistic(int num){
    if(num >= 1 && num<=9){
        return 1;
    }
    else{
        int* numbers = split_numbers(num);
        int length = length_array(numbers);
        int result = 0;
        for(int i = 0; i<length; i++){
            result += int_pow(numbers[i], length);
        }
        if (result == num){
            return 1;
        }
        else{
            return 0;
        }
    }
}

int main (void) {
    printf("Entrez un nombre et découvrez si il est narcissique : ");
    int num;
    scanf("%d", &num);
    if (is_narcissistic(num) == 1){
        printf("%d est narcissique !\n", num);
    }
    else{
        printf("%d n'est pas narcissique.\n", num);
    }
    return 0;
}