#include <stdio.h>

// Function to get the n-th bit of a byte
int getBit(unsigned char byte, int n) {
    return (byte >> n) & 1;
}

int main() {
    unsigned char num;
    int n;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    printf("Enter bit position (0-7): ");
    scanf("%d", &n);

    if (n >= 0 && n < 8) {
        printf("Bit at position %d: %d\n", n, getBit(num, n));
    } else {
        printf("Invalid bit position!\n");
    }

    return 0;
}
 