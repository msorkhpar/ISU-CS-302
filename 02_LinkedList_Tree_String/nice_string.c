#include<stdio.h>
#include <stdlib.h>

void nice_string( int *Array, int i, int difference, int n) 
{ 
	if (i==n){
		if ( difference == 0) 
		{ 
		   for (int j=0; j < n; j++)
 		    printf("%d,", Array[j]);
		   printf("\n");
	   	}
	 	return;
	}
	if ( difference < 0 ) return;
	if ( difference > n-i) return; 
	Array[i]=0;
	nice_string (Array,i+1,difference-1,n); 
	Array[i]=1;
	nice_string (Array,i+1,difference+1,n); 
    return; 
}
 
int main() {	
	int n;
	printf("enter a non-negative number\n");
	scanf("%d", &n);
	if ( n < 0)  return 0; 
	int *Array;  // allocate memory for Array 
	Array = (int*)malloc(n * sizeof(int));
    nice_string(Array,0,0,n);
	return 0;
} 