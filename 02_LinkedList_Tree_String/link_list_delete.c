#include<stdio.h>
#include <stdlib.h>

struct node {
	int data;
    struct node *next;
};

struct node *reverse_list(struct node *head){
	
	if ( head == NULL || head->next==NULL) 
		return head;
	
	
	struct node *before, *current, *after;
	before=head;
	current=head->next;
	after= current->next;
	if (after==NULL){
		current->next=before;
		before->next=NULL;
		return current;
	}
	while (after) {
		
	  current->next=before;
	  before=current;
	  current=after;
	  after=after->next;	
		
	}
	current->next=before;
	head->next=NULL;
	return current;

	
}
struct node *delete_node (struct node *p, int n){
	
	struct node *temp,*current;
	
	if (p==NULL)  return NULL;
	
	if( p->next == NULL && p->data==n) {
		p=NULL; return p;
	}
	  
	current=p->next; temp=p;
    
	while ( current )  {
		
		if (current->data ==n)  {
			current=current->next;
		    temp->next=current;
		}
		else { 
			temp=current;
			current=current->next;
		}
		
	}
	
	if (p->data == n)
	  p=p->next;
	
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
	
 	//printf("enter a new value to be delete \n");
	//scanf("%d", &n);
	q= reverse_list (q);
	printf("the reverse list is : \n");
	
	while ( q ){
	   printf("%d \n", q->data);
	   q=q->next;   	
	} 
	return 0;
} 