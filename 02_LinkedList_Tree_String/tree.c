#include<stdio.h>
#include <stdlib.h>

struct node {
	int data;
    struct node *left;
	struct node *right;	
};



void pre_order (struct node *tree){ // The same as Depth First Search
	
	if ( tree == NULL )
		return;
	else 
	{
		printf("%d , ",tree->data );
        pre_order(tree->left);
		pre_order(tree->right);	
		return ;
	}
	
}

void in_order (struct node *tree){
	
	if ( tree == NULL )
		return;
	else 
	{
		
        in_order(tree->left);
		printf("%d , ",tree->data );
		in_order(tree->right);	
		return ;
	}
	
}

void post_order (struct node *tree){
	
	if ( tree == NULL )
		return;
	else 
	{
		
        post_order(tree->left);
		
		post_order(tree->right);	
		printf("%d , ",tree->data );
		
		return ;
	}
	
}

void BFS_order (struct node *tree, int n){
	
	if ( tree == NULL )
		return;
	
	struct node *queue_list[n]; // assuming tree has n element
	int begin,end;
	begin=end=0;
	struct node *temp; 
	queue_list[end]=tree; end++;
	
	while ( begin< end ){
	  temp=queue_list[begin];
	  printf("%d, ",temp->data);
	  if (temp->left) { 
		  queue_list[end]=temp->left;
		  end++;
	  }
	  if (temp->right) { 
		  queue_list[end]=temp->right;
		  end++;
	  }
	  begin++;	
		
	}
	

}


int main() {	
	int i,n,data;
	printf("enter a number for the length of the array \n");
	scanf("%d", &n);
	int *Array;  // allocate memory for Array 
	Array = (int*)malloc(n * sizeof(int));
	
	
	printf("enter the numbers \n");
	for (i=0; i<n; i++)
		scanf("%d",&Array[i]);
	
	struct node *elements[n];
	
	for ( i=0; i < n ;i++){
		elements[i]= (struct node *) malloc ( sizeof(struct node));
		elements[i]->data=Array[i];	
		elements[i]->left=elements[i]->right=NULL;	
	}
	
	
	for ( i=0; i <n/2 ;i++){
		elements[i]->left=elements[2*i+1];
		if (2*i+2 < n) 
			elements[i]->right=elements[2*i+2];	
		else 
			elements[i]->right=NULL;
	}
	
	for ( i=n/2; i <n ;i++)		
		elements[i]->left=elements[i]->right=NULL;
		
	//BFS_order(elements[0],n);
	post_order(elements[0]);
	//pre_order(elements[0]);
	
	printf("\n");
	return 0;
} 