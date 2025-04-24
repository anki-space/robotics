#include <stdio.h>

// Function to print bit sequence of a byte
void printBits(unsigned char byte) {
    for (int i = 7; i >= 0; i--) {
        printf("%d", (byte >> i) & 1);
    }
    printf("\n");
}

int main() {
    unsigned char num;
    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);  // %hhu is for unsigned char input
    printf("Bit sequence: ");
    printBits(num);
    return 0;
}
