#include <stdio.h>

// Function to swap odd and even bits
unsigned int swap_odd_even_bits(unsigned int num) {
    unsigned int even = num & 0xAAAAAAAA; // Mask even bits
    unsigned int odd  = num & 0x55555555; // Mask odd bits

    even >>= 1; // Shift even bits right
    odd  <<= 1; // Shift odd bits left

    return (even | odd); // Combine swapped bits
}

int main() {
    unsigned int num;

    printf("Enter an integer: ");
    scanf("%u", &num);

    unsigned int swapped = swap_odd_even_bits(num);
    printf("Swapped number: %u\n", swapped);

    return 0;
}
