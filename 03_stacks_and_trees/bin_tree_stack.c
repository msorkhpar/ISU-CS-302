#include<stdio.h> 
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};
int stack_size;
int top;


struct node *insert_node(struct node *tree, int n) {
    if (tree == NULL) {
        // Create a new node when the tree is NULL
        tree = (struct node *) malloc(sizeof(struct node));
        tree->data = n;
        tree->left = tree->right = NULL;
    } else if (tree->data == n) {
        // If the value already exists, return the tree without changes
        return tree;
    } else if (tree->data < n) {
        // Insert into the right subtree
        tree->right = insert_node(tree->right, n);
    } else {
        // Insert into the left subtree
        tree->left = insert_node(tree->left, n);
    }

    return tree;
}

int push(struct node *Stack[], struct node *element) {
    if (top == stack_size) {
        printf("Stack overflow \n");
        return 0;
    }
    Stack[top] = element;
    top++;
    return 1;
}

struct node *get_top(struct node *Stack[]) {
    if (top == -1) return NULL;
    return Stack[top - 1];
}

struct node *pop(struct node *Stack[]) {
    if (top == -1) return NULL;
    else {
        top--;
        return Stack[top];
    }
}


void Pre_order_Stack(struct node *Stack[], struct node *tree) {
    struct node *temp;
    printf("the Pre-order traversal using stack is \n");
    int flag;
    flag = push(Stack, tree);
    if (!flag) {
        printf("Tree is empty \n");
        return;
    }
    while (top > 0) {
        temp = pop(Stack);
        printf("%d \n", temp->data);
        if (temp->right) {
            flag = push(Stack, temp->right);
            if (!flag) break;
        }
        if (temp->left) {
            flag = push(Stack, temp->left);
            if (!flag) break;
        }
    }
    while (top > 0) {
        temp = pop(Stack);
        if(!temp) {
            break;
        }
        else { printf("%d \n", temp->data); }
    }
}

void In_order_Stack(struct node *Stack[], struct node *tree) {
    struct node *current;
    printf("the in-order traversal using stack is \n");
    int flag;
    current = tree;
    while (current || top > 0) {
        while (current) {
            flag = push(Stack, current);
            current = current->left;
        }
        current = pop(Stack);
        printf("%d \n", current->data);
        current = current->right;
    }
}


int main() {
    int n;
    printf("enter a number for the size of the Stack \n");
    scanf("%d", &stack_size);
    struct node *Stack[stack_size];
    for (int i = 0; i < stack_size; i++) {
        Stack[i] = (struct node *) malloc(sizeof(struct node));
        Stack[i]->right = Stack[i]->left = NULL;
    }
    top = 0;
    struct node *tree, *root;
    root = NULL;
    printf("enter the integers elements of the tree -1 for exit \n");
    while (1) { // we read some elements from the user and create a binary search tree
        scanf("%d", &n);
        if (n < 0) {
            break;
        }
        root = insert_node(root, n);
    }
    Pre_order_Stack(Stack, root);
    In_order_Stack(Stack, root);
    return 0;
}