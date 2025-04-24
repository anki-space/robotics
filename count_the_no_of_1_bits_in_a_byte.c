#include <stdio.h>

// Function to count number of 1-bits in a byte
int count_ones(unsigned char byte) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        if ((byte >> i) & 1)
            count++;
    }
    return count;
}

int main() {
    unsigned char num;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    printf("Number of 1-bits: %d\n", count_ones(num));

    return 0;
}
