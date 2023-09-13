#include<stdio.h> 
#include <stdlib.h>

// Tree node struct
struct node {
    int data;
    struct node *left;
    struct node *right;
};
// Stack variables
int stack_size;
int top;

// Tree insert function
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

// Stack push function, returns 1 on success
int push(struct node *Stack[], struct node *element) {
    if (top == stack_size) {
        printf("Stack overflow \n");
        return 0;
    }
    Stack[top] = element;
    top++;
    return 1;
}

// Stack peek function, returns value at the top of stack
struct node *get_top(struct node *Stack[]) {
    if (top == -1) return NULL;     // Empty stack case
    return Stack[top - 1];
}

// Stack pop function
struct node *pop(struct node *Stack[]) {
    if (top == -1) return NULL;     // Empty stack case
    else {
        top--;
        return Stack[top];
    }
}

// Preorder using a stack (root, left, right)
void Pre_order_Stack(struct node *Stack[], struct node *tree) {
    struct node *temp;
    printf("the Pre-order traversal using stack is \n");
    int flag;
    flag = push(Stack, tree);
    // The tree is empty if the push fails
    if (!flag) {
        printf("Tree is empty \n");
        return;
    }
    // while there are elements in the stack
    while (top > 0) {
        // print root
        temp = pop(Stack);
        printf("%d \n", temp->data);

        // add right to the stack, right before left because stacks are First-In-Last-Out (FILO)
        if (temp->right) {
            flag = push(Stack, temp->right);
            if (!flag) break;   // break if stack overflow
        }

        // add left to the stack
        if (temp->left) {
            flag = push(Stack, temp->left);
            if (!flag) break;   // break if stack overflow
        }
    }

    // while there are elements in the stack
    //  The first loop had to break early to enter this loop
    while (top > 0) {
        temp = pop(Stack);

        // break on an empty pop
        if(!temp) {
            break;
        }
        // print on valaid pop
        else { printf("%d \n", temp->data); }
    }
}

// Inorder using a stack (left, root, right)
void In_order_Stack(struct node *Stack[], struct node *tree) {
    struct node *current;
    printf("the pre-order traversal using stack is \n");
    int flag;
    current = tree;

    // while current isn't NULL and the stack isn't empty
    while (current || top > 0) {
        // Push every node going left until we reach a leaf node
        while (current) {
            flag = push(Stack, current);
            current = current->left;
        }

        // Pop and print root
        current = pop(Stack);
        printf("%d \n", current->data);
        // Set current to its right node
        current = current->right;
    }
}


int main() {
    // Node input value
    int n;

    // Get stack size
    printf("enter a number for the size of the Stack \n");
    scanf("%d", &stack_size);
    
    // Initialize the stack
    struct node *Stack[stack_size];
    for (int i = 0; i < stack_size; i++) {
        Stack[i] = (struct node *) malloc(sizeof(struct node));
        Stack[i]->right = Stack[i]->left = NULL;
    }
    top = 0;

    // Initialize and build tree from input
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

    // Print our tree
    Pre_order_Stack(Stack, root);
    In_order_Stack(Stack, root);
    return 0;
}