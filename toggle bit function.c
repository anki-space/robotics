#include <stdio.h>

// Function to toggle the n-th bit of a byte
unsigned char toggle_bit(unsigned char byte, int n) {
    return byte ^ (1 << n);
}

int main() {
    unsigned char num;
    int n;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    printf("Enter bit position to toggle (0-7): ");
    scanf("%d", &n);

    if (n >= 0 && n < 8) {
        unsigned char result = toggle_bit(num, n);
        printf("New value after toggling bit %d: %d\n", n, result);
    } else {
        printf("Invalid bit position!\n");
    }

    return 0;
}