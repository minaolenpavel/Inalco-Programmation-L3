#include <stdio.h>
#include <string.h>

char* reverse_word (char* word, char* reversed_word){
    int length = strlen(word);
    int y = 0;
    // We start the loop at length-1, so we don't count the null character in the end that says it's the end of the string
    for(int i = length - 1; i >= 0; i--){
        reversed_word[y] = word[i];
        y++;
    }
    reversed_word[length] = '\0'; // Add null terminator
    return reversed_word;
}

int main (void) {
    char word[100]; // Leave space for 99 char + the \0 that indicates the end of the word
    printf("Entrez un mot ou un nombre et découvrez si c'est un palindrome : ");
    fgets(word, sizeof(word), stdin);
    // Deletes the newline character that fgets catches
    word[strcspn(word, "\n")] = 0;
    char reversed_word[100];
    // Copy of the original word
    // We make the copy here because if the copy is done in the function reverse_array, then the memory allocated for the returned copy
    // ... will not be available at the end of the function, so it will point to an empty place in the memory, and cause segmentation fault
    strcpy(reversed_word, reverse_word(word, reversed_word));
    // In C we need to use a special function to compare two strings
    if (strcmp(reversed_word, word) == 0){
        printf("%s est un palindrome !\n", word);
    }
    else{
        printf("%s n'est pas un palindrome !\n", word);
    }
    return 0;
}