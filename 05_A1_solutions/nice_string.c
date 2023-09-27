#include<stdio.h>
#include <stdlib.h>

// Prints all the balanced binary sequences of length n

/*
 A sequence S is balanced, if the number of ones is the same as the number of zeros in S.
  Moreover, in every prefix of S, the number of ones is not less than number of zeros.
*/

void nice_string(int *Array, int i, int difference, int n)
{
	// Reached full length
	if (i==n){
		// Print if balanced
		if (difference == 0) 
		{ 
			for (int j=0; j < n; j++)
 				printf("%d,", Array[j]);
			printf("\n");
	   	}
	 	return;
	}

	// Stop recursion if the difference goes negative
	if (difference < 0) return;

	// Stop recursion if remaining elements can't compensate the difference
	if (difference > n-i) return; 
	
	// Set current element to 0, continue recursion
	Array[i]=0;
	nice_string (Array,i+1,difference-1,n);

	// Set current element to 1, continue recursion
	Array[i]=1;
	nice_string (Array,i+1,difference+1,n);

    return; 
}
 
int main() {	
	// Gather input
	int n;
	printf("enter a non-negative number\n");
	scanf("%d", &n);
	if ( n < 0)  return 0; 

	// Generate nice strings
	int *Array;  // allocate memory for Array 
	Array = (int*)malloc(n * sizeof(int));
    nice_string(Array,0,0,n);

	return 0;
} 