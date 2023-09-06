#include<stdio.h>
#include <stdlib.h>

struct node {
	int data;
    struct node *next;
};


struct node *add_node (struct node *p, int n){
	
	struct node *temp;
	temp=(struct node *) malloc ( sizeof(struct node));
	temp->data =n;
	temp->next=NULL;
	
	if (p==NULL)  return temp;
	
	struct node *current;   current=p;

	while ( current->next )  current=current->next;
	
	current->next=temp;
	return p;	
} 
 
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



	while(1){
		scanf("%d", &n);
		if ( n <0) break; // break the while loop 
		current= (struct node *) malloc ( sizeof(struct node));
		current->data=n;
		p->next=current;
		p=current;
	}
	
	p->next=NULL;
	
 	printf("enter a new value to be added \n");
	scanf("%d", &n);
	q= add_node (q,n);
	printf("the new list is : \n");
	
	while ( q ){
	   printf("%d \n", q->data);
	   q=q->next;   	
	} 
	return 0;
} 