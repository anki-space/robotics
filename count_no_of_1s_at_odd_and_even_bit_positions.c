#include <stdio.h>

// Function to count 1s at even and odd positions
void count_ones_positions(unsigned char byte, int *even, int *odd) {
    *even = 0;
    *odd = 0;
    for (int i = 0; i < 8; i++) {
        if ((byte >> i) & 1) {
            if (i % 2 == 0)
                (*even)++;
            else
                (*odd)++;
        }
    }
}
int main() {
    unsigned char num;
    int even_count, odd_count;

    printf("Enter a number (0-255): ");
    scanf("%hhu", &num);

    count_ones_positions(num, &even_count, &odd_count);

    printf("Number of 1s at even positions: %d\n", even_count);
    printf("Number of 1s at odd positions : %d\n", odd_count);

    return 0;
}
