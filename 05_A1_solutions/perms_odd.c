#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Prints all the permutations from 1, 2,...,n in which every odd number appears before every even number.
// Compile with -lm when using the CS server for math.h to be included.

// Odds first permutation
void permutation(int *Array, int i, int n)
{
    // Only odds in first half
    if (i <= ceil(n/2.0))
    {
        // Check for even numbers in the first i elements
        for(int j = 0; j < i; j++)
            if (Array[j] % 2 == 0) return;
    }

    // End of permutation, print it
    if (i == n)
    {
        for (int j = 0; j < n; j++)
            printf("%d,", Array[j]);
        printf("\n");
        return;
    }

    // Generate permutations
    int temp;
    int t;
    for (t = i; t < n; t++)
    {
        // Exchange Array[i],Array[t]
        temp = Array[i];
        Array[i] = Array[t];
        Array[t] = temp;

        // Recursive generation
        permutation(Array, i + 1, n);
        
        // Exchange back Array[t],Array[i]
        temp = Array[i];
        Array[i] = Array[t];
        Array[t] = temp;
    }
}

int main()
{
    // Gather input
    int n;
    printf("enter a non-negative number\n");
    scanf("%d", &n);
    if (n < 0)
        return 0;

    // Build Array
    int *Array; // allocate memory for Array
    Array = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        Array[i] = i + 1;
    
    // Generate and print permutations
    permutation(Array, 0, n);
    
    return 0;
}