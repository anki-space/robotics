#include <stdio.h>

// Function to reverse bits in a byte
unsigned char reverse_bits(unsigned char byte) {
    unsigned char result = 0;
    for (int i = 0; i < 8; i++) {
        result <<= 1;              // Shift result to the left
        result |= (byte & 1);      // Copy LSB from byte
        byte >>= 1;                // Shift byte to the right
    }
    return result;
}

int main() {
    unsigned char num;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    unsigned char reversed = reverse_bits(num);

    printf("Reversed bits value: %d\n", reversed);

    return 0;
}
