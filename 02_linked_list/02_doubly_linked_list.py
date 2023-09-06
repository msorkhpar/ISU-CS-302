from __future__ import annotations

from utils.loader import load_base_configs


class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node

    def remove(self, val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next_node
            if self.head:
                self.head.prev_node = None
            return
        curr = self.head
        while curr is not None:
            if curr.val == val:
                if curr.prev_node:
                    curr.prev_node.next_node = curr.next_node
                if curr.next_node:
                    curr.next_node.prev_node = curr.prev_node
                if self.tail == curr:
                    self.tail = curr.prev_node
                return
            curr = curr.next_node

    def __str__(self):
        current = self.head
        res = []
        while current is not None:
            res.append(str(current.val))
            current = current.next_node
        return "[" + " <-> ".join(res) + "]"


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    logger.info(f"Input Array: {arr}")
    dll = DoublyLinkedList()
    for element in arr:
        dll.add(element)

    logger.info(f"Linked List: {dll}")
    dll.remove(arr[0])
    logger.info(f"After removing the head: {dll}")
    dll.remove(arr[-1])
    logger.info(f"After removing the tail: {dll}")
    if dll.head:
        logger.info(f"Head is: {dll.head.val}")
    if dll.tail:
        logger.info(f"Tail is: {dll.tail.val}")
