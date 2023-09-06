#include<stdio.h>
#include <stdlib.h>

struct node {
	int data;
    struct node *next;
};

int main() {	
	int n,data;
	struct node *p,*q,*current;
	printf("enter data to put int the link list negative number to stop \n");
	
	scanf("%d", &n);
	if ( n < 0 ) return 0;
	else {
		p=(struct node *) malloc ( sizeof(struct node));
		p->data=n;
		q=p;
	}
	
	while(1 ){
		scanf("%d", &n);
		if ( n <0) break; // break the while loop 
		current= (struct node *) malloc ( sizeof(struct node));
		current->data=n;
		p->next=current;
		p=current;
	}
	
	p->next=NULL;
 	printf("here is the list \n");
	while ( q ){	
	   printf("%d \n", q->data);
	   q=q->next;   	
	} 
	return 0;
} 