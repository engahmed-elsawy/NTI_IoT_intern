#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x, y;
    int *ptr1, *ptr2;

    // Read two integers
    printf("Enter first number: ");
    scanf("%d", &x);
    
    printf("Enter second number: ");
    scanf("%d", &y);

    // Assign pointers
    ptr1 = &x;
    ptr2 = &y;

    // Swap using pointers
    swap(ptr1, ptr2);

    // Calculate sum using pointers
    int sum = *ptr1 + *ptr2;

    // Print results
    printf("\nAfter swapping:\n");
    printf("First number = %d\n", *ptr1);
    printf("Second number = %d\n", *ptr2);
    printf("Sum = %d\n", sum);

    return 0;
}


