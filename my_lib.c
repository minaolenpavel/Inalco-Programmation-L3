#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define TRUE true

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

// Function to get the length of an integer
int length_int(int i){
    int length = 0;
    bool done = false;
    // Each iteration the int is divided by 10 and we increment length
    // When i is equal to 0, we're done, it means that there is enough decimals to have only 0, 
    // ex : 453 => 0.453, 3 decimals so length is 3
    while (done == false){
        i = i/10;
        length++;
        if(i==0){
            done = true;
        }
    }
    return length;
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

int int_array_last_element(int* array){
    int* ptr = array;
    int length = sizeof(array) / sizeof(array[0]);
    int last_element = *(ptr + length -1);
    return last_element;
}