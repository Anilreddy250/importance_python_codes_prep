#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;
    char temp;

    while (start < end) {
        // Swap characters
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        // Move pointers toward the middle
        start++;
        end--;
    }
}

int main() {
    char myString[] = "Anil";
    
    printf("Original: %s\n", myString);
    
    reverseString(myString);
    
    printf("Reversed: %s\n", myString);
    
    return 0;
}