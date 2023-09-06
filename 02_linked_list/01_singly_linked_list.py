from __future__ import annotations

from utils.loader import load_base_configs


class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node

    def remove(self, val):

        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next_node
            return
        prev = self.head
        curr = self.head.next_node
        while curr is not None:
            if curr.val == val:
                prev.next_node = curr.next_node
                return
            prev = curr
            curr = curr.next_node

    def revers(self):
        """
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
    }"""
        if self.head is None or self.head.next_node is None:
            return
        before = None
        current = self.head
        while current is not None:
            after = current.next_node
            current.next_node = before
            before = current
            current = after
        self.head = before

    def __str__(self):
        current = self.head
        res = []
        while current is not None:
            res.append(str(current.val))
            current = current.next_node
        return "[" + " -> ".join(res) + "]"


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f"Input Array: {arr}")
    sll = SinglyLinkedList()
    for element in arr:
        sll.add(element)

    logger.info(f"Linked List: {sll}")
    sll.remove(arr[0])
    logger.info(f"After removing the head: {sll}")
    sll.remove(arr[-1])
    logger.info(f"After removing the tail: {sll}")

    sll.revers()
    logger.info(f"After reversing the list: {sll}")
