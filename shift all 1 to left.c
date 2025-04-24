#include <stdio.h>

// Function to shift all 1s to the left
unsigned char shift_ones_left(unsigned char byte) {
    int count = 0;

    // Count number of 1s
    for (int i = 0; i < 8; i++) {
        if ((byte >> i) & 1)
            count++;
    }

    // Create new byte with all 1s shifted to left
    unsigned char result = 0;
    for (int i = 7; count > 0; i--, count--) {
        result |= (1 << i);
    }

    return result;
}
int main() {
    unsigned char num;
    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    unsigned char shifted = shift_ones_left(num);

    printf("Modified byte (shifted 1s left): %d\n", shifted);

    return 0;
}
