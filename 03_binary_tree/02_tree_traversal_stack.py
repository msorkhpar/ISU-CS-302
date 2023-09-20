from __future__ import annotations

from utils.loader import load_base_configs


class Node:
    def __init__(self, data):
        self.data:int  = data
        self.left: Node | None = None
        self.right: Node | None = None


def insert_node(tree, n):
    if tree is None:
        tree = Node(n)
        return tree
    if tree.data == n:
        return tree
    if tree.data < n:
        tree.right = insert_node(tree.right, n)
    else:
        tree.left = insert_node(tree.left, n)
    return tree


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack: list[Node] = [None] * size
        self.top = 0

    def push(self, element) -> bool:
        '''
        if (top == stack_size) {
            printf("Stack overflow \n");
            return 0;
        }
        Stack[top] = element;
        top++;
        return 1;
        '''
        if self.top == self.size:
            print("Stack overflow")
            return False
        self.stack[self.top] = element
        self.top += 1
        return True

    def get_top(self) -> Node | None:
        '''
        if (top == -1){
            return NULL;
        }
        return Stack[top - 1];
        '''
        if self.top == 0:
            return None
        return self.stack[self.top - 1]

    def pop(self) -> Node | None:
        ''''
        if (top == -1){
         return NULL;
        }
        else {
            top--;
        }
        return Stack[top];
    }
        '''
        if self.top == 0:
            return None
        self.top -= 1
        return self.stack[self.top]


def pre_order_stack(stack: Stack, tree: Node, logger):
    '''
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
        if {
            (!temp)
            break;
        }
        else { printf("%d \n", temp->data); }
    }
    '''

    logger.info("The Pre-order traversal using stack is:")
    if not stack.push(tree):
        logger.info("Tree is empty")
        return
    while stack.top > 0:
        temp = stack.pop()
        logger.info(temp.data)
        if temp.right:
            if not stack.push(temp.right):
                break
        if temp.left:
            if not stack.push(temp.left):
                break


def in_order_stack(stack: Stack, tree: Node, logger):
    '''
    void In_order_Stack(struct node *Stack[], struct node *tree) {
        struct node *current;
        printf("the pre-order travesral using stack is \n");
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
    '''

    logger.info("The In-order traversal using stack is:")
    current = tree
    while current or stack.top > 0:
        while current:
            stack.push(current)
            current = current.left
        current = stack.pop()
        logger.info(current.data)
        current = current.right


def main():
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    stack = Stack(len(arr))
    root = None
    for n in arr:
        root = insert_node(root, n)
    pre_order_stack(stack, root, logger)
    in_order_stack(stack, root, logger)


if __name__ == "__main__":
    main()
