#include <stdio.h>

// Function to count 0s at even and odd positions
void count_zeros_positions(unsigned char byte, int *even, int *odd) {
    *even = 0;
    *odd = 0;
    for (int i = 0; i < 8; i++) {
        if (!((byte >> i) & 1)) {
            if (i % 2 == 0)
                (*even)++;
            else
                (*odd)++;
        }
    }
}
int main() {
    unsigned char num;
    int even_zeros, odd_zeros;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    count_zeros_positions(num, &even_zeros, &odd_zeros);

    printf("Number of 0s at even positions: %d\n", even_zeros);
    printf("Number of 0s at odd positions : %d\n", odd_zeros);

    return 0;
}
